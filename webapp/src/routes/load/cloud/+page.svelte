<script>
    import { onMount } from "svelte";
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";

    let activeTab = "pandas";
</script>

<svelte:head>
    <title>Cloud Storage | Python Data Tools</title>
    <meta
        name="description"
        content="Load data from AWS S3, Google Cloud Storage (GCS), and Azure using Pandas, Polars, and DuckDB."
    />
</svelte:head>

<div class="page-container">
    <h1><Icon name="cloud" size={40} /> Load from Cloud Storage</h1>
    <p class="intro">
        Efficiently read parquet, csv, and json files directly from object
        storage (S3, GCS, Azure) without downloading them locally first.
    </p>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="card-grid">
            <div class="card">
                <div class="card-header">
                    <Icon name="pandas" size={24} />
                    <h3>Pandas</h3>
                </div>
                <code>pd.read_parquet("s3://bucket/file.parquet")</code>
                <p>Requires <code>s3fs</code>, <code>gcsfs</code></p>
            </div>
            <div class="card">
                <div class="card-header">
                    <Icon name="polars" size={24} />
                    <h3>Polars</h3>
                </div>
                <code>pl.scan_parquet("s3://bucket/file.parquet")</code>
                <p>Lazy loading optimized for cloud</p>
            </div>
            <div class="card">
                <div class="card-header">
                    <Icon name="duckdb" size={24} />
                    <h3>DuckDB</h3>
                </div>
                <code>SELECT * FROM read_parquet('s3://...')</code>
                <p>Streaming execution via HTTP</p>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <CodeTabs {examples} task="load_cloud" section="load" />
    </section>

    <section class="credentials">
        <h2><Icon name="key" size={24} /> Managing Credentials</h2>
        <div class="cred-grid">
            <div class="cred-card">
                <h3>AWS S3</h3>
                <p>
                    Libraries usually look for standard environment variables:
                </p>
                <div class="env-vars">
                    <code>export AWS_ACCESS_KEY_ID=...</code>
                    <code>export AWS_SECRET_ACCESS_KEY=...</code>
                    <code>export AWS_REGION=us-east-1</code>
                </div>
            </div>
            <div class="cred-card">
                <h3>Google Cloud (GCS)</h3>
                <p>Point to your service account JSON key:</p>
                <div class="env-vars">
                    <code
                        >export
                        GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"</code
                    >
                </div>
            </div>
        </div>
    </section>

    <section class="when-to-use">
        <h2>Key Differences</h2>
        <div class="when-grid">
            <div class="when-card">
                <h3>Pandas</h3>
                <p>
                    Good for smaller files that fit in memory. Downloads entire
                    file before parsing.
                </p>
            </div>
            <div class="when-card">
                <h3>Polars</h3>
                <p>
                    <strong>Best for Cloud.</strong> Can read only necessary columns/rows
                    (predicate pushdown) without downloading the whole file.
                </p>
            </div>
            <div class="when-card">
                <h3>DuckDB</h3>
                <p>
                    <strong>Best for Querying.</strong> virtual headers allow querying
                    TB-scale datasets remotely.
                </p>
            </div>
        </div>
    </section>
</div>

<style>
    .page-container {
        max-width: 1200px;
        margin: 0 auto;
    }

    h1 {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        margin-bottom: var(--space-4);
        color: var(--text-primary);
    }

    .intro {
        font-size: 1.2rem;
        color: var(--text-secondary);
        margin-bottom: var(--space-8);
        max-width: 800px;
    }

    section {
        margin-bottom: var(--space-12);
    }

    h2 {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        margin-bottom: var(--space-6);
        color: var(--accent-primary);
    }

    /* Cards */
    .card-grid,
    .when-grid,
    .cred-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: var(--space-4);
    }

    .card,
    .when-card,
    .cred-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-6);
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        margin-bottom: var(--space-3);
    }

    code {
        display: block;
        background: var(--bg-tertiary);
        padding: var(--space-3);
        border-radius: var(--radius-sm);
        font-size: 0.9rem;
        color: var(--text-primary);
        word-break: break-all;
    }

    /* Credentials */
    .cred-grid {
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    }

    .env-vars {
        display: flex;
        flex-direction: column;
        gap: var(--space-2);
        margin-top: var(--space-3);
    }

    .env-vars code {
        color: var(--accent-secondary);
    }
</style>
