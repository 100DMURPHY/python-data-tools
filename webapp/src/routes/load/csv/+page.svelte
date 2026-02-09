<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <div class="page-header">
        <div class="breadcrumb">
            <span>Load</span>
            <span class="sep">/</span>
            <span class="current">CSV Files</span>
        </div>
        <h1>Load CSV Files</h1>
        <p class="intro">
            CSV (Comma-Separated Values) is the most common data format you'll
            encounter. Every library handles it slightly differently — see how
            each one works below.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <code>pd.read_csv("file.csv")</code>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <code>pl.read_csv("file.csv")</code>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <code>duckdb.read_csv("file.csv")</code>
            </div>
            <div class="ref-card bigquery">
                <Icon name="cloud" size={20} color="var(--bigquery-color)" />
                <code>load_table_from_file()</code>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Click each tab to see the complete, runnable code for each library.
        </p>
        <CodeTabs {examples} task="load_csv" section="load" />
    </section>

    <section class="when-to-use">
        <h2>When to Use Each</h2>
        <div class="when-grid">
            <div class="when-card">
                <div class="when-header">
                    <Icon name="pandas" size={24} color="var(--pandas-color)" />
                    <h3>Pandas</h3>
                </div>
                <ul>
                    <li>Small to medium files (&lt;1GB)</li>
                    <li>Quick prototyping and exploration</li>
                    <li>Broad ecosystem compatibility</li>
                    <li>Learning and tutorials</li>
                </ul>
            </div>
            <div class="when-card">
                <div class="when-header">
                    <Icon name="polars" size={24} color="var(--polars-color)" />
                    <h3>Polars</h3>
                </div>
                <ul>
                    <li>Large files (GB-scale)</li>
                    <li>Memory-constrained environments</li>
                    <li>When speed matters</li>
                    <li>Production data pipelines</li>
                </ul>
            </div>
            <div class="when-card">
                <div class="when-header">
                    <Icon name="duckdb" size={24} color="var(--duckdb-color)" />
                    <h3>DuckDB</h3>
                </div>
                <ul>
                    <li>SQL preference</li>
                    <li>Ad-hoc queries on files</li>
                    <li>Querying without loading</li>
                    <li>Analytical workloads</li>
                </ul>
            </div>
            <div class="when-card">
                <div class="when-header">
                    <Icon
                        name="cloud"
                        size={24}
                        color="var(--bigquery-color)"
                    />
                    <h3>BigQuery</h3>
                </div>
                <ul>
                    <li>Cloud data pipelines</li>
                    <li>Data already in GCS</li>
                    <li>Production ETL systems</li>
                    <li>Team collaboration</li>
                </ul>
            </div>
        </div>
    </section>
</div>

<style>
    .page {
        max-width: 900px;
    }

    /* Page Header */
    .page-header {
        margin-bottom: var(--space-8);
    }

    .breadcrumb {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-bottom: var(--space-3);
    }

    .breadcrumb .sep {
        color: var(--border-color);
    }

    .breadcrumb .current {
        color: var(--accent-primary);
    }

    h1 {
        font-size: 2.25rem;
        margin-bottom: var(--space-3);
    }

    .intro {
        font-size: 1.1rem;
        color: var(--text-secondary);
        max-width: 650px;
    }

    /* Sections */
    section {
        margin-bottom: var(--space-10);
    }

    h2 {
        font-size: 1.25rem;
        margin-bottom: var(--space-4);
        margin-top: 0;
    }

    .section-intro {
        font-size: 0.9rem;
        color: var(--text-muted);
        margin-bottom: var(--space-4);
    }

    /* Quick Reference */
    .ref-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: var(--space-3);
    }

    .ref-card {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-4);
    }

    .ref-card code {
        font-size: 0.8rem;
        color: var(--text-primary);
        background: transparent;
        padding: 0;
    }

    .ref-card.pandas {
        border-left: 3px solid var(--pandas-color);
    }
    .ref-card.polars {
        border-left: 3px solid var(--polars-color);
    }
    .ref-card.duckdb {
        border-left: 3px solid var(--duckdb-color);
    }
    .ref-card.bigquery {
        border-left: 3px solid var(--bigquery-color);
    }

    /* When to Use */
    .when-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: var(--space-4);
    }

    .when-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
    }

    .when-header {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        margin-bottom: var(--space-4);
    }

    .when-header h3 {
        font-size: 1rem;
        margin: 0;
    }

    .when-card ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .when-card li {
        font-size: 0.85rem;
        color: var(--text-secondary);
        padding: var(--space-1) 0;
        padding-left: var(--space-4);
        position: relative;
    }

    .when-card li::before {
        content: "•";
        position: absolute;
        left: 0;
        color: var(--accent-primary);
    }

    /* Responsive */
    @media (max-width: 600px) {
        h1 {
            font-size: 1.75rem;
        }

        .intro {
            font-size: 1rem;
        }
    }
</style>
