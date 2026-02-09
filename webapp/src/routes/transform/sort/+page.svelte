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
            <span class="current">Sorting & Ordering</span>
        </div>
        <h1>Sorting & Ordering</h1>
        <p class="intro">
            Organizing data is essential for analysis. Whether you need the top
            10 customers or just want to order by date, every library has
            powerful sorting capabilities.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.sort_values(by=['A', 'B'])</code>
                    <span class="ref-note">Lists for multi-column</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df.sort(['A', 'B'], descending=...)</code>
                    <span class="ref-note">Highly optimized</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>ORDER BY A ASC, B DESC</code>
                    <span class="ref-note">Standard SQL</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>How it Works</h2>
        <div class="visual-container">
            <div class="step input">
                <span class="step-label">Input</span>
                <div class="mini-list">
                    <div class="item">3. Charlie</div>
                    <div class="item">1. Alice</div>
                    <div class="item">2. Bob</div>
                </div>
            </div>
            <div class="step process">
                <div class="process-box">
                    <div class="process-icon">⬇️</div>
                    <code>Sort by ID</code>
                </div>
            </div>
            <div class="step output">
                <span class="step-label">Sorted</span>
                <div class="mini-list">
                    <div class="item highlight">1. Alice</div>
                    <div class="item highlight">2. Bob</div>
                    <div class="item highlight">3. Charlie</div>
                </div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Examples using the <strong>Palmer Penguins</strong> dataset.
        </p>
        <CodeTabs {examples} task="transform_sort" section="transform" />
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

    /* Visual Explainer */
    .visual-container {
        display: flex;
        align-items: center;
        gap: var(--space-6);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-6);
        overflow-x: auto;
    }

    .step {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-2);
    }

    .step-label {
        font-size: 0.75rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .mini-list {
        display: flex;
        flex-direction: column;
        gap: 2px;
        background: var(--bg-tertiary);
        padding: 8px;
        border-radius: 4px;
        width: 120px;
    }

    .item {
        font-size: 0.75rem;
        padding: 6px 10px;
        background: var(--bg-primary);
        border-radius: 2px;
        text-align: center;
        color: var(--text-secondary);
    }

    .item.highlight {
        color: var(--text-primary);
        border-left: 2px solid var(--accent-primary);
    }

    .process-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: var(--bg-tertiary);
        border-radius: 50%;
        border-radius: var(--radius-lg);
        width: 100px;
        height: 80px;
        border: 1px dashed var(--border-color);
    }

    .process-icon {
        font-size: 1.5rem;
    }

    .process-box code {
        font-size: 0.65rem;
        color: var(--accent-secondary);
    }
</style>
