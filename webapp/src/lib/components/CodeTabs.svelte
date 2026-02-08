<script>
    export let examples = {};
    export let task = "";
    export let section = "load"; // Default to load

    const repoBase = "pythondatatools/python-data-tools";
    const branch = "main";

    const libraries = ["pandas", "polars", "duckdb", "bigquery"];
    const libraryLabels = {
        pandas: "🐼 Pandas",
        polars: "🐻‍❄️ Polars",
        duckdb: "🦆 DuckDB",
        bigquery: "☁️ BigQuery",
    };

    let activeTab = "pandas";

    $: activeExample = examples[`${task}_${activeTab}`];
    $: code = activeExample?.code || "// Example coming soon";
    $: output = activeExample?.output || "";

    // Derived URLs for portability
    $: rawUrl = `https://raw.githubusercontent.com/${repoBase}/${branch}/chapters/${section}/${task}_${activeTab}.py`;
    $: uvRunCmd = `uv run ${rawUrl}`;
    $: colabUrl = `https://colab.research.google.com/github/${repoBase}/blob/${branch}/notebooks/${section}/${task}_${activeTab}.ipynb`;
    $: jupyterCmd = `uvx --from jupytext jupytext --to notebook --execute ${rawUrl}`;

    let copied = false;
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text);
        copied = true;
        setTimeout(() => (copied = false), 2000);
    }
</script>

<div class="code-tabs">
    <div class="tab-bar">
        {#each libraries as lib}
            <button
                class="tab"
                class:active={activeTab === lib}
                on:click={() => (activeTab = lib)}
            >
                {libraryLabels[lib]}
            </button>
        {/each}
    </div>

    <div class="run-bar">
        <div class="run-label">Run this script:</div>
        <div class="run-actions">
            <button
                class="run-btn"
                on:click={() => copyToClipboard(uvRunCmd)}
                title="Copy uv run command"
            >
                🚀 {copied ? "COPIED UV!" : "UV RUN"}
            </button>
            <a
                href={colabUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="run-btn colab"
            >
                📒 COLAB
            </a>
            <button
                class="run-btn"
                on:click={() => copyToClipboard(jupyterCmd)}
                title="Copy Jupyter launcher command"
            >
                🪐 JUPYTER
            </button>
        </div>
    </div>

    <div class="code-panel">
        <button class="copy-button" on:click={() => copyToClipboard(code)}>
            {copied ? "COPIED CODE!" : "COPY CODE"}
        </button>
        <pre><code>{code}</code></pre>
    </div>

    {#if output}
        <div class="output-panel">
            <div class="output-header">
                <span>Output</span>
            </div>
            <pre class="output-content"><code>{output}</code></pre>
        </div>
    {/if}
</div>

<style>
    .code-tabs {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        overflow: hidden;
        margin: 1.5rem 0;
    }

    .tab-bar {
        display: flex;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none; /* Hide scrollbar for Chrome/Safari */
    }

    .tab-bar::-webkit-scrollbar {
        display: none;
    }

    .tab {
        flex: 1;
        min-width: 100px; /* Prevent tabs from being too small on mobile */
        padding: 0.75rem 1rem;
        background: transparent;
        border: none;
        color: var(--text-secondary);
        font-size: 0.875rem;
        cursor: pointer;
        transition: all 0.15s;
    }

    .tab:hover {
        background: var(--bg-tertiary);
        color: var(--text-primary);
    }

    .tab.active {
        background: var(--bg-primary);
        color: var(--accent-blue);
        font-weight: 500;
        border-bottom: 2px solid var(--accent-blue);
    }

    .run-bar {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem 1rem;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
    }

    .run-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .run-actions {
        display: flex;
        gap: 0.5rem;
    }

    .run-btn {
        padding: 0.35rem 0.75rem;
        background: var(--bg-tertiary);
        border: 1px solid var(--border-color);
        border-radius: 4px;
        color: var(--text-secondary);
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }

    .run-btn:hover {
        background: var(--bg-primary);
        color: var(--accent-blue);
        border-color: var(--accent-blue);
    }

    .run-btn.colab:hover {
        color: #f9ab00; /* Google Orange/Yellow */
        border-color: #f9ab00;
    }

    .code-panel {
        background: var(--bg-tertiary);
        padding: 1.5rem 1rem 1rem 1rem;
        overflow-x: auto;
        position: relative;
    }

    .copy-button {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        padding: 0.25rem 0.5rem;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 4px;
        color: var(--text-secondary);
        font-size: 0.65rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s;
        opacity: 0.6;
    }

    .copy-button:hover {
        opacity: 1;
        background: var(--bg-tertiary);
        color: var(--accent-blue);
        border-color: var(--accent-blue);
    }

    pre {
        margin: 0;
        font-family: "JetBrains Mono", "Fira Code", monospace;
        font-size: 0.875rem;
        line-height: 1.6;
    }

    code {
        color: var(--text-primary);
    }

    .output-panel {
        background: #1e1e1e; /* Dark terminal background */
        border-top: 1px solid var(--border-color);
        padding: 0;
    }

    .output-header {
        background: #2d2d2d;
        color: #a9a9a9;
        font-size: 0.75rem;
        padding: 0.25rem 1rem;
        font-family: inherit;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .output-content {
        margin: 0;
        padding: 1rem;
        color: #d4d4d4;
        font-size: 0.8125rem;
        line-height: 1.4;
    }
</style>
