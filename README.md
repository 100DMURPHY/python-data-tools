# Python Data Tools

A multi-platform comparison of data wrangling techniques from **"Python for Data Analysis, 3rd Edition"** by Wes McKinney.

**Compare the same operations across:**
- 🐼 **Pandas** - Original book examples (baseline)
- 🦆 **DuckDB** - In-process SQL analytics
- ☁️ **BigQuery SQL** - Cloud data warehouse
- 🐻‍❄️ **Polars** - High-performance DataFrames

*Designed for extensibility—future support for ibis, chdb, and more.*

## 📖 Chapters

| Chapter | Topic | Status |
|---------|-------|--------|
| 4 | NumPy Basics | ⬜ Planned |
| 5 | Getting Started with pandas | 🟡 In Progress |
| 6 | Data Loading, Storage, File Formats | ⬜ Planned |
| 7 | Data Cleaning and Preparation | ⬜ Planned |
| 8 | Data Wrangling (Join, Combine, Reshape) | ⬜ Planned |
| 10 | Data Aggregation and Group Operations | ⬜ Planned |
| 11 | Time Series | ⬜ Planned |
| 13 | Data Analysis Examples | ⬜ Planned |

## 🚀 Quick Start

```bash
git clone https://github.com/pythondatatools/python-data-tools.git
cd python-data-tools

# Install Python dependencies
pip install -e .

# Run the web app
cd webapp && npm install && npm run dev
```

## 📁 Project Structure

```
python-data-tools/
├── chapters/           # Source code by chapter (4 platforms each)
├── datasets/           # Sample datasets
├── benchmarks/         # Performance comparisons
└── webapp/             # SvelteKit comparison app
```

## 📜 License

MIT License - Based on examples from [wesm/pydata-book](https://github.com/wesm/pydata-book)
