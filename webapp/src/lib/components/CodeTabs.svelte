<script>
    import Prism from "prismjs";
    import "prismjs/components/prism-python";
    import "prismjs/components/prism-sql";
    import Icon from "./Icon.svelte";

    export let examples = {};
    export let task = "";
    export let section = "load";

    const repoBase = "pythondatatools/python-data-tools";
    const branch = "main";

    const libraries = ["pandas", "polars", "duckdb", "bigquery"];
    const libraryConfig = {
        pandas: {
            label: "Pandas",
            icon: "pandas",
            color: "var(--pandas-color)",
        },
        polars: {
            label: "Polars",
            icon: "polars",
            color: "var(--polars-color)",
        },
        duckdb: {
            label: "DuckDB",
            icon: "duckdb",
            color: "var(--duckdb-color)",
        },
        bigquery: {
            label: "BigQuery",
            icon: "cloud",
            color: "var(--bigquery-color)",
        },
    };

    let activeTab = "pandas";
    let copiedCode = false;
    let copiedCmd = false;

    $: activeExample = examples[`${task}_${activeTab}`];
    $: code = activeExample?.code || "# Example coming soon";
    $: output = activeExample?.output || "";

    // Syntax highlight the code
    $: highlightedCode = Prism.highlight(
        code,
        Prism.languages.python,
        "python",
    );

    // Derived URLs for portability
    $: rawUrl = `https://raw.githubusercontent.com/${repoBase}/${branch}/chapters/${section}/${task}_${activeTab}.py`;
    $: uvRunCmd = `uv run ${rawUrl}`;
    $: colabUrl = `https://colab.research.google.com/github/${repoBase}/blob/${branch}/notebooks/${section}/${task}_${activeTab}.ipynb`;

    function copyCode() {
        navigator.clipboard.writeText(code);
        copiedCode = true;
        setTimeout(() => (copiedCode = false), 2000);
    }

    function copyCommand() {
        navigator.clipboard.writeText(uvRunCmd);
        copiedCmd = true;
        setTimeout(() => (copiedCmd = false), 2000);
    }
</script>

<div class="code-tabs">
    <div class="tab-bar">
        {#each libraries as lib}
            <button
                class="tab"
                class:active={activeTab === lib}
                onclick={() => (activeTab = lib)}
                style="--tab-color: {libraryConfig[lib].color}"
            >
                <Icon
                    name={libraryConfig[lib].icon}
                    size={16}
                    color={activeTab === lib
                        ? libraryConfig[lib].color
                        : "currentColor"}
                />
                <span class="tab-label">{libraryConfig[lib].label}</span>
            </button>
        {/each}
    </div>

    <div class="run-bar">
        <div class="run-left">
            <span class="run-label">Run it:</span>
            <button class="run-btn" onclick={copyCommand}>
                {#if copiedCmd}
                    <Icon name="check" size={14} />
                    <span>Copied!</span>
                {:else}
                    <Icon name="copy" size={14} />
                    <span>UV Run</span>
                {/if}
            </button>
            <a
                href={colabUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="run-btn colab"
            >
                <svg
                    viewBox="0 0 24 24"
                    width="14"
                    height="14"
                    fill="currentColor"
                >
                    <path
                        d="M16.9414 4.9757a7.033 7.033 0 0 0-9.8823 0 7.033 7.033 0 0 0 0 9.8823 7.033 7.033 0 0 0 9.8823 0 7.033 7.033 0 0 0 0-9.8823ZM12 16.0034a5.988 5.988 0 0 1-4.2426-1.7573 6.0045 6.0045 0 0 1 0-8.4853 6.0045 6.0045 0 0 1 8.4853 0 6.0045 6.0045 0 0 1 0 8.4853A5.988 5.988 0 0 1 12 16.0034Z"
                    />
                    <path d="M12 8.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7Z" />
                </svg>
                <span>Colab</span>
            </a>
        </div>
    </div>

    <div class="code-panel">
        <button class="copy-button" onclick={copyCode}>
            {#if copiedCode}
                <Icon name="check" size={12} />
                Copied!
            {:else}
                <Icon name="copy" size={12} />
                Copy
            {/if}
        </button>
        <pre><code class="language-python">{@html highlightedCode}</code></pre>
    </div>

    {#if output}
        <div class="output-panel">
            <div class="output-header">
                <Icon name="play" size={12} />
                <span>Output</span>
            </div>
            <pre class="output-content"><code>{output}</code></pre>
        </div>
    {/if}
</div>

<style>
    .code-tabs {
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        overflow: hidden;
        margin: var(--space-6) 0;
        background: var(--bg-secondary);
    }

    .tab-bar {
        display: flex;
        background: var(--bg-tertiary);
        border-bottom: 1px solid var(--border-color);
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }

    .tab-bar::-webkit-scrollbar {
        display: none;
    }

    .tab {
        flex: 1;
        min-width: 110px;
        padding: var(--space-3) var(--space-4);
        background: transparent;
        border: none;
        color: var(--text-secondary);
        font-size: 0.875rem;
        cursor: pointer;
        transition: all var(--transition-fast);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-2);
        border-bottom: 2px solid transparent;
    }

    .tab:hover {
        background: var(--surface-hover);
        color: var(--text-primary);
    }

    .tab.active {
        background: var(--bg-secondary);
        color: var(--tab-color);
        font-weight: 500;
        border-bottom-color: var(--tab-color);
    }

    .tab-label {
        white-space: nowrap;
    }

    .run-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--space-2) var(--space-4);
        background: var(--bg-tertiary);
        border-bottom: 1px solid var(--border-color);
    }

    .run-left {
        display: flex;
        align-items: center;
        gap: var(--space-3);
    }

    .run-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .run-btn {
        padding: var(--space-1) var(--space-3);
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        color: var(--text-secondary);
        font-size: 0.75rem;
        font-weight: 500;
        cursor: pointer;
        transition: all var(--transition-fast);
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: var(--space-1);
    }

    .run-btn:hover {
        background: var(--accent-primary);
        color: white;
        border-color: var(--accent-primary);
        text-decoration: none;
    }

    .run-btn.colab:hover {
        background: #f9ab00;
        border-color: #f9ab00;
    }

    .code-panel {
        background: var(--bg-primary);
        padding: var(--space-5);
        overflow-x: auto;
        position: relative;
    }

    .copy-button {
        position: absolute;
        top: var(--space-3);
        right: var(--space-3);
        padding: var(--space-1) var(--space-3);
        background: var(--bg-tertiary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        color: var(--text-muted);
        font-size: 0.7rem;
        font-weight: 500;
        cursor: pointer;
        transition: all var(--transition-fast);
        display: flex;
        align-items: center;
        gap: var(--space-1);
        opacity: 0.7;
    }

    .copy-button:hover {
        opacity: 1;
        background: var(--accent-primary);
        color: white;
        border-color: var(--accent-primary);
    }

    pre {
        margin: 0;
        font-family: var(--font-mono);
        font-size: 0.9rem;
        line-height: 1.7;
        background: transparent;
        border: none;
        padding: 0;
    }

    code {
        color: var(--text-primary);
        background: transparent;
        padding: 0;
    }

    /* Prism syntax highlighting overrides */
    :global(.token.comment) {
        color: #6b7785;
    }
    :global(.token.string) {
        color: #10b981;
    }
    :global(.token.number) {
        color: #f59e0b;
    }
    :global(.token.keyword) {
        color: #7c3aed;
    }
    :global(.token.function) {
        color: #06b6d4;
    }
    :global(.token.operator) {
        color: #ef4444;
    }
    :global(.token.punctuation) {
        color: #a0aab8;
    }
    :global(.token.builtin) {
        color: #7c3aed;
    }
    :global(.token.class-name) {
        color: #f59e0b;
    }

    .output-panel {
        background: #0a0e14;
        border-top: 1px solid var(--border-color);
    }

    .output-header {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        background: #151a20;
        color: var(--text-muted);
        font-size: 0.7rem;
        padding: var(--space-2) var(--space-4);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .output-content {
        margin: 0;
        padding: var(--space-4);
        color: #10b981;
        font-size: 0.8rem;
        line-height: 1.5;
        background: transparent;
        border: none;
    }

    .output-content code {
        color: #10b981;
    }
</style>
