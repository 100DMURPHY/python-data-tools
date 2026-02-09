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
            <span class="current">Pivot & Reshape</span>
        </div>
        <h1>Pivot & Reshape</h1>
        <p class="intro">
            Transform your data between wide and long formats. Essential for
            analysis, visualization, and preparing data for different tools.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.pivot_table(...)</code>
                    <span class="ref-note">Long → Wide with aggregation</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df.pivot(...) / df.unpivot(...)</code>
                    <span class="ref-note">Pivot and Unpivot methods</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>PIVOT / UNPIVOT</code>
                    <span class="ref-note">Native SQL reshape syntax</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Understanding Reshaping</h2>
        <div class="reshape-visual">
            <div class="shape-box long">
                <div class="shape-title">Long Format</div>
                <table>
                    <thead>
                        <tr><th>Species</th><th>Island</th><th>Mass</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Adelie</td><td>Biscoe</td><td>3700</td></tr>
                        <tr><td>Adelie</td><td>Dream</td><td>3688</td></tr>
                        <tr><td>Gentoo</td><td>Biscoe</td><td>5076</td></tr>
                    </tbody>
                </table>
                <span class="desc">More rows, fewer columns</span>
            </div>
            <div class="arrows">
                <div class="arrow-row">
                    <span class="label">PIVOT →</span>
                </div>
                <div class="arrow-row">
                    <span class="label">← UNPIVOT</span>
                </div>
            </div>
            <div class="shape-box wide">
                <div class="shape-title">Wide Format</div>
                <table>
                    <thead>
                        <tr><th>Species</th><th>Biscoe</th><th>Dream</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Adelie</td><td>3700</td><td>3688</td></tr>
                        <tr><td>Gentoo</td><td>5076</td><td>—</td></tr>
                    </tbody>
                </table>
                <span class="desc">Fewer rows, more columns</span>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Reshaping the <strong>Palmer Penguins</strong> dataset between formats.
        </p>
        <CodeTabs {examples} task="transform_pivot" section="transform" />
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

    /* Reshape Visual */
    .reshape-visual {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-6);
        gap: var(--space-4);
        overflow-x: auto;
    }

    .shape-box {
        flex: 1;
        min-width: 180px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-2);
    }

    .shape-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .shape-box table {
        font-size: 0.7rem;
        border-collapse: collapse;
        background: var(--bg-primary);
        border-radius: var(--radius-md);
        overflow: hidden;
    }

    .shape-box th,
    .shape-box td {
        padding: var(--space-1) var(--space-2);
        border: 1px solid var(--border-color);
        text-align: center;
    }

    .shape-box th {
        background: var(--bg-tertiary);
        color: var(--text-muted);
        font-weight: 600;
    }

    .shape-box td {
        color: var(--text-secondary);
    }

    .shape-box .desc {
        font-size: 0.65rem;
        color: var(--text-muted);
        text-align: center;
    }

    .arrows {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-2);
    }

    .arrow-row {
        display: flex;
        align-items: center;
    }

    .arrow-row .label {
        font-size: 0.7rem;
        font-weight: 700;
        color: var(--accent-primary);
        white-space: nowrap;
    }
</style>
