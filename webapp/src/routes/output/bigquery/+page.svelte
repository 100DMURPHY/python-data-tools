<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <div class="page-header">
        <div class="breadcrumb">
            <span>Output</span>
            <span class="sep">/</span>
            <span class="current">BigQuery</span>
        </div>
        <h1>Export to BigQuery</h1>
        <p class="intro">
            Load your local data into BigQuery for enterprise-scale analytics.
            Choose the right pattern based on your data volume and library.
        </p>
    </div>

    <section class="quick-ref">
        <h2>BigQuery Loading Patterns</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.to_gbq('table', project_id)</code>
                    <span class="ref-note">Easiest for small/medium data</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>Write to Parquet ➔ BQ Load</code>
                    <span class="ref-note"
                        >Most efficient for large datasets</span
                    >
                </div>
            </div>
            <div class="ref-card gcloud">
                <Icon name="bigquery" size={20} color="var(--bigquery-color)" />
                <div class="ref-content">
                    <code>client.load_table_from_uri()</code>
                    <span class="ref-note"
                        >The "Cloud Native" gold standard</span
                    >
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Ingestion Architectures</h2>
        <div class="arch-visual">
            <div class="arch-lane">
                <div class="arch-title">Direct Upload</div>
                <div class="arch-items">
                    <div class="arch-item memory">Pandas Memory</div>
                    <div class="arch-arrow">➔</div>
                    <div class="arch-item bq">BigQuery</div>
                </div>
                <div class="arch-note">
                    Best for: Rapid prototyping, small data
                </div>
            </div>

            <div class="arch-lane alternate">
                <div class="arch-title">Staged Loading (GCS)</div>
                <div class="arch-items">
                    <div class="arch-item polars">Local Parquet</div>
                    <div class="arch-arrow">➔</div>
                    <div class="arch-item gcs">Cloud Storage</div>
                    <div class="arch-arrow">➔</div>
                    <div class="arch-item bq">BigQuery</div>
                </div>
                <div class="arch-note">
                    Best for: Production ETL, Big Data, Polars/DuckDB
                </div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Demonstrating various ways to push data into the cloud.
        </p>
        <CodeTabs {examples} task="output_bigquery" section="output" />
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

    /* Quick Ref Grid */
    .ref-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: var(--space-3);
    }

    .ref-card {
        display: flex;
        align-items: flex-start;
        gap: var(--space-3);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-4);
    }

    .ref-content {
        display: flex;
        flex-direction: column;
        gap: var(--space-1);
    }

    .ref-card code {
        font-size: 0.8rem;
        color: var(--text-primary);
        background: transparent;
        padding: 0;
    }

    .ref-note {
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    .ref-card.pandas {
        border-left: 3px solid var(--pandas-color);
    }
    .ref-card.polars {
        border-left: 3px solid var(--polars-color);
    }
    .ref-card.gcloud {
        border-left: 3px solid var(--bigquery-color);
    }

    /* Arch Visual */
    .arch-visual {
        display: flex;
        flex-direction: column;
        gap: var(--space-4);
    }

    .arch-lane {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-6);
    }

    .arch-title {
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: var(--space-4);
        color: var(--accent-primary);
    }

    .arch-items {
        display: flex;
        align-items: center;
        gap: var(--space-4);
        margin-bottom: var(--space-4);
    }

    .arch-item {
        padding: var(--space-3) var(--space-4);
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-sm);
        font-size: 0.75rem;
        font-weight: 600;
    }

    .arch-item.bq {
        border-color: var(--bigquery-color);
        color: var(--bigquery-color);
    }
    .arch-item.gcs {
        border-color: #ffca28;
        color: #ffca28;
    }
    .arch-item.polars {
        border-color: var(--polars-color);
        color: var(--polars-color);
    }

    .arch-arrow {
        color: var(--text-muted);
    }

    .arch-note {
        font-size: 0.7rem;
        color: var(--text-muted);
        font-style: italic;
    }
</style>
