<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import VersionBadge from "$lib/components/VersionBadge.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <h1>Load CSV / Text Files</h1>

    <p class="intro">
        Loading CSV files is the most common entry point for data analysis. Each
        library offers different trade-offs between simplicity and performance.
    </p>

    <div class="version-row">
        <VersionBadge library="pandas" version="2.2" />
        <VersionBadge library="polars" version="1.x" />
        <VersionBadge library="duckdb" version="1.1" />
        <VersionBadge library="bigquery" version="3.x" />
    </div>

    <h2>Quick Reference</h2>

    <div class="table-container">
        <table class="reference-table">
            <thead>
                <tr>
                    <th>Library</th>
                    <th>Syntax</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>🐼 Pandas</td>
                    <td><code>pd.read_csv("file.csv")</code></td>
                </tr>
                <tr>
                    <td>🐻‍❄️ Polars</td>
                    <td><code>pl.read_csv("file.csv")</code></td>
                </tr>
                <tr>
                    <td>🦆 DuckDB</td>
                    <td><code>duckdb.read_csv("file.csv")</code></td>
                </tr>
                <tr>
                    <td>☁️ BigQuery</td>
                    <td
                        ><code
                            >client.load_table_from_file(..., format="CSV")</code
                        ></td
                    >
                </tr>
            </tbody>
        </table>
    </div>

    <h2>Full Examples</h2>

    <CodeTabs {examples} task="load_csv" />

    <h2>When to Use Which</h2>

    <div class="when-cards">
        <div class="card pandas">
            <h3>🐼 Pandas</h3>
            <p>
                Small to medium files (&lt;1GB). Quick prototyping. Broad
                ecosystem compatibility.
            </p>
        </div>
        <div class="card polars">
            <h3>🐻‍❄️ Polars</h3>
            <p>
                Large files. Memory-constrained environments. When speed
                matters.
            </p>
        </div>
        <div class="card duckdb">
            <h3>🦆 DuckDB</h3>
            <p>
                SQL preference. Ad-hoc queries. Querying files without loading
                fully.
            </p>
        </div>
        <div class="card bigquery">
            <h3>☁️ BigQuery</h3>
            <p>Cloud data pipelines. Production ETL. Data already in GCS.</p>
        </div>
    </div>
</div>

<style>
    .page {
        max-width: 900px;
    }

    h1 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: var(--text-primary);
    }

    .intro {
        color: var(--text-secondary);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .version-row {
        display: flex;
        gap: 0.75rem;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        scrollbar-width: none;
    }

    .version-row::-webkit-scrollbar {
        display: none;
    }

    h2 {
        font-size: 1.25rem;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        color: var(--text-primary);
    }

    .reference-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 2rem;
    }

    .reference-table th,
    .reference-table td {
        padding: 0.75rem 1rem;
        text-align: left;
        border-bottom: 1px solid var(--border-color);
    }

    .reference-table th {
        background: var(--bg-secondary);
        font-weight: 500;
        color: var(--text-muted);
        font-size: 0.75rem;
        text-transform: uppercase;
    }

    .reference-table code {
        background: var(--bg-tertiary);
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.875rem;
    }

    .when-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }

    .card {
        padding: 1.25rem;
        border-radius: 8px;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
    }

    .card h3 {
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }

    .card p {
        font-size: 0.875rem;
        color: var(--text-secondary);
        margin: 0;
    }

    .card.pandas {
        border-left: 3px solid #150458;
    }
    .card.polars {
        border-left: 3px solid #cd792c;
    }
    .card.duckdb {
        border-left: 3px solid #fff000;
    }
    .card.bigquery {
        border-left: 3px solid #4285f4;
    }
</style>
