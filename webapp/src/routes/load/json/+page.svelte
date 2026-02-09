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
            <span class="current">JSON</span>
        </div>
        <h1>Load JSON Files</h1>
        <p class="intro">
            JSON is everywhere — APIs, configs, logs. Learn how each library
            handles both standard JSON and newline-delimited JSON
            (NDJSON/JSONL).
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>pd.read_json("file.json")</code>
                    <span class="ref-note">Use lines=True for NDJSON</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>pl.read_json("file.json")</code>
                    <span class="ref-note">read_ndjson() for NDJSON</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>duckdb.read_json("file.json")</code>
                    <span class="ref-note">Auto-detects format</span>
                </div>
            </div>
            <div class="ref-card bigquery">
                <Icon name="cloud" size={20} color="var(--bigquery-color)" />
                <div class="ref-content">
                    <code>NEWLINE_DELIMITED_JSON</code>
                    <span class="ref-note">Load from GCS</span>
                </div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Click each tab to see the complete, runnable code for each library.
        </p>
        <CodeTabs {examples} task="load_json" section="load" />
    </section>

    <section class="formats">
        <h2>JSON vs NDJSON</h2>
        <div class="format-grid">
            <div class="format-card">
                <h3>Standard JSON</h3>
                <pre><code
                        >[
  {`{"id": 1, "name": "Alice"}`},
  {`{"id": 2, "name": "Bob"}`}
]</code
                    ></pre>
                <p>Entire file is one JSON array. Must load all into memory.</p>
            </div>
            <div class="format-card">
                <h3>NDJSON / JSONL</h3>
                <pre><code
                        >{`{"id": 1, "name": "Alice"}`}
{`{"id": 2, "name": "Bob"}`}</code
                    ></pre>
                <p>
                    One JSON object per line. Can stream, more efficient for
                    large files.
                </p>
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
    .ref-card.duckdb {
        border-left: 3px solid var(--duckdb-color);
    }
    .ref-card.bigquery {
        border-left: 3px solid var(--bigquery-color);
    }

    .format-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: var(--space-4);
    }

    .format-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
    }

    .format-card h3 {
        font-size: 1rem;
        margin-bottom: var(--space-3);
    }

    .format-card pre {
        margin-bottom: var(--space-3);
        font-size: 0.8rem;
    }

    .format-card p {
        font-size: 0.85rem;
        margin: 0;
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
