<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import VersionBadge from "$lib/components/VersionBadge.svelte";
    import { base } from "$app/paths";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <h1>Load JSON / NDJSON</h1>

    <p class="intro">
        JSON is the primary format for web data and semi-structured documents.
        <strong>NDJSON</strong> (Newline Delimited JSON) is preferred for large datasets
        and streaming due to its line-by-line processing capability.
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
                    <th>Standard JSON</th>
                    <th>NDJSON (Lines)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>🐼 Pandas</td>
                    <td><code>pd.read_json("f.json")</code></td>
                    <td><code>pd.read_json("f.jsonl", lines=True)</code></td>
                </tr>
                <tr>
                    <td>🐻‍❄️ Polars</td>
                    <td><code>pl.read_json("f.json")</code></td>
                    <td><code>pl.read_ndjson("f.jsonl")</code></td>
                </tr>
                <tr>
                    <td>🦆 DuckDB</td>
                    <td><code>read_json_auto("f.json")</code></td>
                    <td><code>read_json_auto("f.jsonl")</code></td>
                </tr>
                <tr>
                    <td>☁️ BigQuery</td>
                    <td>-</td>
                    <td><code>format="NEWLINE_DELIMITED_JSON"</code></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="note">
        <span class="icon">💡</span>
        <p>
            <strong>Performance Tip:</strong> NDJSON is significantly faster for
            high-volume loading as it avoids the memory overhead of parsing a single
            giant JSON array.
        </p>
    </div>

    <h2>Full Examples</h2>

    <CodeTabs {examples} task="load_json" />

    <h2>When to Use Which</h2>

    <div class="when-cards">
        <div class="card pandas">
            <h3>🐼 Pandas</h3>
            <p>
                Best for complex, nested JSON where you need the <code
                    >json_normalize</code
                >
                utility to flatten structured data into a table.
            </p>
        </div>
        <div class="card polars">
            <h3>🐻‍❄️ Polars</h3>
            <p>
                Extremely fast for NDJSON. If you have gigabytes of logs in
                JSONL format, Polars is the clear winner.
            </p>
        </div>
        <div class="card duckdb">
            <h3>🦆 DuckDB</h3>
            <p>
                Great for ad-hoc SQL queries on JSON files. Auto-detection of
                types and nesting is very robust.
            </p>
        </div>
        <div class="card bigquery">
            <h3>☁️ BigQuery</h3>
            <p>
                Standard format for BigQuery batch loads. Requires NDJSON format
                for direct file uploads.
            </p>
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

    .note {
        display: flex;
        gap: 1rem;
        padding: 1rem;
        background: color-mix(in srgb, var(--accent-orange) 10%, transparent);
        border: 1px solid
            color-mix(in srgb, var(--accent-orange) 20%, transparent);
        border-radius: 8px;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    .note .icon {
        font-size: 1.25rem;
    }

    .note p {
        margin: 0;
        font-size: 0.9rem;
        color: var(--text-secondary);
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
