<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <div class="page-header">
        <div class="breadcrumb">
            <span>Transform</span>
            <span class="sep">/</span>
            <span class="current">Aggregation & Grouping</span>
        </div>
        <h1>Aggregation & Grouping</h1>
        <p class="intro">
            Turn raw data into meaningful summaries. Group by categories and
            calculate statistics like mean, count, and sum.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.groupby('col').mean()</code>
                    <span class="ref-note">Group then Aggregate</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df.group_by('col').agg(...)</code>
                    <span class="ref-note">Expression-based Aggregation</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>SELECT col, AVG(x) GROUP BY col</code>
                    <span class="ref-note">Standard SQL aggregates</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>How Grouping Works</h2>
        <div class="agg-visual">
            <div class="step">
                <span class="step-num">1</span>
                <span class="step-label">Split</span>
                <div class="visual split">
                    <div class="box blue"></div>
                    <div class="box orange"></div>
                    <div class="box blue"></div>
                </div>
                <p>Divide data into groups based on keys.</p>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <span class="step-num">2</span>
                <span class="step-label">Apply</span>
                <div class="visual apply">
                    <div class="op">SUM()</div>
                    <div class="op">SUM()</div>
                </div>
                <p>Calculate stats for each group independenty.</p>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <span class="step-num">3</span>
                <span class="step-label">Combine</span>
                <div class="visual combine">
                    <div class="row">Blue: 10</div>
                    <div class="row">Orange: 5</div>
                </div>
                <p>Merge results into a new summary table.</p>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Summarizing the <strong>Palmer Penguins</strong> dataset by species and
            island.
        </p>
        <CodeTabs {examples} task="transform_aggregate" section="transform" />
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

    /* Agg Visual */
    .agg-visual {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-8);
        gap: var(--space-4);
    }

    .step {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: var(--space-3);
    }

    .step-num {
        width: 24px;
        height: 24px;
        background: var(--accent-primary);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
    }

    .step-label {
        font-size: 0.875rem;
        font-weight: 600;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .step p {
        font-size: 0.75rem;
        color: var(--text-muted);
        margin: 0;
        line-height: 1.4;
    }

    .visual {
        height: 60px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: var(--space-1);
        background: var(--bg-primary);
        border-radius: var(--radius-md);
        padding: var(--space-2);
    }

    .arrow {
        font-size: 1.5rem;
        color: var(--border-color);
    }

    .box {
        width: 80%;
        height: 8px;
        border-radius: 2px;
    }
    .box.blue {
        background: #3b82f6;
    }
    .box.orange {
        background: #f59e0b;
    }

    .op {
        font-size: 0.7rem;
        font-weight: 700;
        color: var(--accent-primary);
        background: rgba(124, 58, 237, 0.1);
        padding: 2px 8px;
        border-radius: 10px;
    }

    .combine .row {
        font-size: 0.7rem;
        font-family: var(--font-mono);
        color: var(--text-secondary);
    }
</style>
