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
            <span class="current">CSV / Parquet / JSON</span>
        </div>
        <h1>Export to Files</h1>
        <p class="intro">
            Save your processed data to persistent storage. Performance,
            portability, and schema preservation are key considerations when
            choosing a format.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>df.to_csv() / df.to_parquet()</code>
                    <span class="ref-note">Comprehensive export methods</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df.write_csv() / df.write_parquet()</code>
                    <span class="ref-note">High-perf IO methods</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>COPY table TO 'file' (FORMAT ...)</code>
                    <span class="ref-note">Efficient SQL bulk export</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Choosing a Format</h2>
        <div class="format-grid">
            <div class="format-card">
                <div class="format-icon">📄</div>
                <div class="format-name">CSV</div>
                <div class="format-pros">✅ Human-readable, universal</div>
                <div class="format-cons">❌ Large, no schema, slow</div>
            </div>
            <div class="format-card">
                <div class="format-icon">📦</div>
                <div class="format-name">Parquet</div>
                <div class="format-pros">✅ Tiny, keeps schema, fast</div>
                <div class="format-cons">❌ Binary (needs tools)</div>
            </div>
            <div class="format-card">
                <div class="format-icon">🕸️</div>
                <div class="format-name">JSON</div>
                <div class="format-pros">✅ Web-friendly, nested data</div>
                <div class="format-cons">❌ Large, lacks schema</div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Exporting a summary dataset across different libraries.
        </p>
        <CodeTabs {examples} task="output_files" section="output" />
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

    /* Format Grid */
    .format-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: var(--space-4);
    }

    .format-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: var(--space-6);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        gap: var(--space-2);
        transition: transform var(--transition-fast);
    }

    .format-card:hover {
        transform: translateY(-2px);
        border-color: var(--accent-primary);
    }

    .format-icon {
        font-size: 1.5rem;
        margin-bottom: var(--space-2);
    }

    .format-name {
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--text-primary);
    }

    .format-pros,
    .format-cons {
        font-size: 0.7rem;
        color: var(--text-secondary);
    }

    .format-cons {
        color: var(--text-muted);
    }
</style>
