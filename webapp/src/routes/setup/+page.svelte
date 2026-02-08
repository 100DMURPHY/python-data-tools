<script>
    import { base } from "$app/paths";
</script>

<div class="page">
    <h1>🚀 Get Started with UV</h1>

    <p class="intro">
        The biggest hurdle for beginners starting with Python is managing
        environments and dependencies. This project uses <strong>uv</strong>,
        the fastest and most reliable Python tool in the ecosystem.
    </p>

    <section class="setup-step">
        <h2>1. Install UV</h2>
        <p>Run this in your terminal (Linux/macOS):</p>
        <pre><code>curl -LsSf https://astral.sh/uv/install.sh | sh</code></pre>
        <p>Windows (PowerShell):</p>
        <pre><code
                >powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"</code
            ></pre>
    </section>

    <section class="setup-step">
        <h2>2. Run Any Example Instantly</h2>
        <p>
            One of the best features of <code>uv</code> is running scripts directly
            from a URL without needing to "install" anything first.
        </p>
        <p>Try it now with our Pandas example:</p>
        <pre><code
                >uv run https://raw.githubusercontent.com/pythondatatools/python-data-tools/main/chapters/load/csv_pandas.py</code
            ></pre>
        <div class="tip">
            <span class="icon">✨</span>
            <p>
                <strong>Why this is awesome:</strong> UV will automatically
                download a temporary Python version, install
                <code>pandas</code>, and run the script. It leaves your system
                clean!
            </p>
        </div>
    </section>

    <section class="setup-step">
        <h2>3. Local Development</h2>
        <p>
            If you've cloned this repository, setting up your environment is a
            single command:
        </p>
        <pre><code>uv sync</code></pre>
        <p>
            This will create a <code>.venv</code> folder with everything you need
            to follow along.
        </p>
    </section>

    <div class="cta-row">
        <a href="{base}/load/csv" class="btn primary">Start Wrangling</a>
    </div>
</div>

<style>
    .page {
        max-width: 800px;
        margin: 0 auto;
    }

    h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .intro {
        font-size: 1.2rem;
        color: var(--text-secondary);
        margin-bottom: 3rem;
        line-height: 1.6;
    }

    .setup-step {
        margin-bottom: 3rem;
        padding-bottom: 2rem;
        border-bottom: 1px solid var(--border-color);
    }

    .setup-step h2 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: var(--accent-blue);
    }

    pre {
        background: var(--bg-tertiary);
        padding: 1rem;
        border-radius: 8px;
        overflow-x: auto;
        border: 1px solid var(--border-color);
        margin: 1rem 0;
    }

    code {
        font-family: "JetBrains Mono", monospace;
        font-size: 0.9rem;
        color: var(--text-primary);
    }

    .tip {
        display: flex;
        gap: 1rem;
        padding: 1rem;
        background: var(--bg-secondary);
        border-radius: 8px;
        margin-top: 1.5rem;
    }

    .tip .icon {
        font-size: 1.2rem;
    }
    .tip p {
        margin: 0;
        font-size: 0.9rem;
        color: var(--text-muted);
    }

    .cta-row {
        text-align: center;
        margin-top: 2rem;
    }

    .btn {
        display: inline-block;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        transition: transform 0.2s;
    }

    .btn.primary {
        background: var(--accent-blue);
        color: white;
    }

    .btn:hover {
        transform: translateY(-2px);
    }
</style>
