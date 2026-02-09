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
            <span class="current">Parquet</span>
        </div>
        <h1>Load Parquet Files</h1>
        <p class="intro">
            Parquet is a columnar format optimized for analytics. It's smaller,
            faster, and preserves data types — perfect for larger datasets.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <code>pd.read_parquet("file.parquet")</code>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <code>pl.read_parquet("file.parquet")</code>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <code>duckdb.read_parquet("file.parquet")</code>
            </div>
            <div class="ref-card bigquery">
                <Icon name="cloud" size={20} color="var(--bigquery-color)" />
                <code>load_table_from_uri()</code>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Click each tab to see the complete, runnable code for each library.
        </p>
        <CodeTabs {examples} task="load_parquet" section="load" />
    </section>

    <section class="when-to-use">
        <h2>When to Use Parquet</h2>
        <div class="info-cards">
            <div class="info-card">
                <h3>✓ Use Parquet When</h3>
                <ul>
                    <li>Dataset is larger than a few hundred MB</li>
                    <li>You need to preserve data types exactly</li>
                    <li>Reading only certain columns (columnar efficiency)</li>
                    <li>Working with cloud storage (S3, GCS)</li>
                </ul>
            </div>
            <div class="info-card warning">
                <h3>✗ Stick with CSV When</h3>
                <ul>
                    <li>You need human-readable files</li>
                    <li>Sharing with non-technical users</li>
                    <li>Dataset is small (&lt;10MB)</li>
                    <li>Editing files manually</li>
                </ul>
            </div>
        </div>
    </section>
</div>

<style>
    .page {
        max-width: 900px;
    }

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

    .ref-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
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

    .info-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: var(--space-4);
    }

    .info-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
        border-left: 3px solid var(--accent-success);
    }

    .info-card.warning {
        border-left-color: var(--accent-warning);
    }

    .info-card h3 {
        font-size: 1rem;
        margin-bottom: var(--space-4);
    }

    .info-card ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .info-card li {
        font-size: 0.85rem;
        color: var(--text-secondary);
        padding: var(--space-1) 0;
        padding-left: var(--space-4);
        position: relative;
    }

    .info-card li::before {
        content: "•";
        position: absolute;
        left: 0;
        color: var(--accent-primary);
    }

    @media (max-width: 600px) {
        h1 {
            font-size: 1.75rem;
        }
        .intro {
            font-size: 1rem;
        }
    }
</style>
