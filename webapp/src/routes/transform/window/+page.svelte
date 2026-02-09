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
            <span class="current">Window Functions</span>
        </div>
        <h1>Window Functions</h1>
        <p class="intro">
            Perform calculations across related rows without collapsing them.
            Perfect for rankings, running totals, and row comparisons.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.groupby().rank()</code>
                    <span class="ref-note">Group-aware ranking</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>pl.col().rank().over('col')</code>
                    <span class="ref-note">Expression with .over() window</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>RANK() OVER (PARTITION BY ...)</code>
                    <span class="ref-note">Standard SQL window syntax</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Common Window Operations</h2>
        <div class="window-grid">
            <div class="window-card">
                <div class="window-icon">🏆</div>
                <div class="window-name">RANK / DENSE_RANK</div>
                <div class="window-desc">
                    Position within a group (1st, 2nd, 3rd...)
                </div>
            </div>
            <div class="window-card">
                <div class="window-icon">#️⃣</div>
                <div class="window-name">ROW_NUMBER</div>
                <div class="window-desc">Sequential counter (1, 2, 3...)</div>
            </div>
            <div class="window-card">
                <div class="window-icon">⬅️</div>
                <div class="window-name">LAG / LEAD</div>
                <div class="window-desc">Access previous/next row value</div>
            </div>
            <div class="window-card">
                <div class="window-icon">📈</div>
                <div class="window-name">SUM / AVG OVER</div>
                <div class="window-desc">
                    Running totals and moving averages
                </div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Analyzing the <strong>Palmer Penguins</strong> dataset with window functions.
        </p>
        <CodeTabs {examples} task="transform_window" section="transform" />
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

    /* Window Grid */
    .window-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: var(--space-4);
    }

    .window-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: var(--space-2);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
        transition: transform var(--transition-fast);
    }

    .window-card:hover {
        transform: translateY(-2px);
        border-color: var(--accent-primary);
    }

    .window-icon {
        font-size: 1.5rem;
    }

    .window-name {
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--text-primary);
    }

    .window-desc {
        font-size: 0.7rem;
        color: var(--text-muted);
        line-height: 1.3;
    }
</style>
