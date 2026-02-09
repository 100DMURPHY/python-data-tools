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
            <span class="current">Databases</span>
        </div>
        <h1>Export to Databases</h1>
        <p class="intro">
            Push your transformed data into relational databases for long-term
            storage, multi-user access, or integration with BI tools.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.to_sql('table', con=engine)</code>
                    <span class="ref-note"
                        >SQLAlchemy-based database writes</span
                    >
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df.write_database('table', uri)</code>
                    <span class="ref-note">Fast bulk loading via ADBC</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>CREATE TABLE AS SELECT ...</code>
                    <span class="ref-note"
                        >Native persistence or external DB hooks</span
                    >
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Modern Database Workflow</h2>
        <div class="db-visual">
            <div class="db-step">
                <div class="step-num">1</div>
                <div class="step-title">Process</div>
                <div class="step-desc">Transform in-memory</div>
            </div>
            <div class="db-arrow">➔</div>
            <div class="db-step">
                <div class="step-num">2</div>
                <div class="step-title">Load</div>
                <div class="step-desc">Bulk write to DB</div>
            </div>
            <div class="db-arrow">➔</div>
            <div class="db-step">
                <div class="step-num">3</div>
                <div class="step-title">Serve</div>
                <div class="step-desc">BI Tools & Apps</div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Writing summary statistics to <strong>SQLite</strong> and
            <strong>BigQuery</strong>.
        </p>
        <CodeTabs {examples} task="output_database" section="output" />
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

    /* DB Visual */
    .db-visual {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-8);
        gap: var(--space-4);
    }

    .db-step {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: var(--space-2);
    }

    .step-num {
        width: 32px;
        height: 32px;
        background: var(--accent-primary);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: var(--space-1);
    }

    .step-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--text-primary);
    }

    .step-desc {
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    .db-arrow {
        font-size: 1.5rem;
        color: var(--border-color);
        margin-bottom: 24px;
    }

    @media (max-width: 600px) {
        .db-visual {
            flex-direction: column;
            gap: var(--space-6);
        }
        .db-arrow {
            transform: rotate(90deg);
            margin-bottom: 0;
        }
    }
</style>
