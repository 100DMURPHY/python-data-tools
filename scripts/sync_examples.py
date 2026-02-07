"""
Sync Examples Script - API-Centric Structure

Extracts marked code blocks from chapters/ and generates examples.json
for the Svelte frontend.

New structure:
- chapters/load/*.py -> load_csv_pandas, load_csv_polars, etc.
- chapters/transform/*.py -> filter_pandas, join_polars, etc.
- chapters/output/*.py -> write_csv_pandas, etc.
"""
import os
import re
import json
import subprocess
from collections import defaultdict

# Determine project root relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, "chapters")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "webapp/src/data/examples.json")
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "webapp/static/notebooks")

# Regex for markers:
# Python: # <key> ... # </key>
# SQL: -- <key> ... -- </key>
MARKER_REGEX = re.compile(r'^\s*(?:#|--)\s*<(\w+)>\s*$')
END_MARKER_REGEX = re.compile(r'^\s*(?:#|--)\s*</(\w+)>\s*$')


def get_language(filename):
    if filename.endswith(".sql"):
        return "sql"
    return "python"


def parse_file(filepath):
    """Extract all marked code blocks from a file."""
    results = {}
    current_key = None
    buffer = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # Check for start marker
        start_match = MARKER_REGEX.match(line)
        if start_match:
            current_key = start_match.group(1)
            buffer = []
            continue
            
        # Check for end marker
        end_match = END_MARKER_REGEX.match(line)
        if end_match:
            if current_key == end_match.group(1):
                code_block = "".join(buffer).strip()
                results[current_key] = code_block
                current_key = None
            continue
            
        if current_key:
            buffer.append(line)
            
    return results


def convert_to_notebook(filepath, relative_path):
    """Convert a .py script to .ipynb using jupytext."""
    # Create output filename
    filename = os.path.basename(filepath)
    notebook_name = filename.replace(".py", ".ipynb")
    
    # Preserve subdirectory structure: load/csv_pandas.py -> load/csv_pandas.ipynb
    relative_dir = os.path.dirname(relative_path)
    target_dir = os.path.join(NOTEBOOKS_DIR, relative_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    target_path = os.path.join(target_dir, notebook_name)
    
    print(f"Generating Notebook: {relative_path.replace('.py', '.ipynb')} ...", end=" ", flush=True)
    try:
        subprocess.run(
            ["uv", "run", "--with", "jupytext", "jupytext", "--to", "notebook", filepath, "-o", target_path],
            capture_output=True,
            check=True
        )
        print("✅")
        return True
    except Exception as e:
        print(f"❌ ({str(e)})")
        return False


def main():
    """
    New output structure:
    {
        "load_csv_pandas": { "code": "...", "language": "python" },
        "load_csv_polars": { "code": "...", "language": "python" },
        ...
    }
    """
    all_examples = {}
    
    # Ensure Notebooks dir exists
    os.makedirs(NOTEBOOKS_DIR, exist_ok=True)
    
    # Walk through all directories in chapters/
    for root, dirs, files in os.walk(CHAPTERS_DIR):
        for file in files:
            if not (file.endswith(".py") or file.endswith(".sql")):
                continue
                
            language = get_language(file)
            filepath = os.path.join(root, file)
            relative_path = os.path.relpath(filepath, CHAPTERS_DIR)
            
            snippets = parse_file(filepath)
            
            # For Python files, we capture output AND generate notebooks
            file_output = ""
            if language == "python":
                print(f"Executing {file} ...", end=" ", flush=True)
                try:
                    res = subprocess.run(
                        ["uv", "run", filepath],
                        capture_output=True,
                        text=True,
                        check=True,
                        timeout=30
                    )
                    file_output = res.stdout
                    print("✅")
                except subprocess.CalledProcessError as e:
                    print("❌ (Execution failed)")
                    file_output = f"Execution failed (Exit {e.returncode}):\n{e.stderr}"
                except Exception as e:
                    print("❌ (System error)")
                    file_output = f"System error: {str(e)}"
                
                # Jupytext Conversion
                convert_to_notebook(filepath, relative_path)

            for key, code in snippets.items():
                all_examples[key] = {
                    "code": code,
                    "language": language,
                    "output": file_output
                }

    # Ensure output dir exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_examples, f, indent=2)
    
    print(f"Generated {OUTPUT_FILE} with {len(all_examples)} examples.")


if __name__ == "__main__":
    main()
