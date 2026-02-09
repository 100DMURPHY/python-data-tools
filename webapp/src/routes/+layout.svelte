<script>
    import "../app.css";
    import { page } from "$app/stores";
    import { base } from "$app/paths";
    import navSections from "$lib/nav.json";
    import Navbar from "$lib/components/Navbar.svelte";
    import Search from "$lib/components/Search.svelte";
    import Chat from "$lib/components/Chat.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import { afterNavigate } from "$app/navigation";

    let isSidebarOpen = false;
    let isChatOpen = false;

    function toggleSidebar() {
        isSidebarOpen = !isSidebarOpen;
    }

    function toggleChat() {
        isChatOpen = !isChatOpen;
    }

    // Close sidebar after navigation on mobile
    afterNavigate(() => {
        isSidebarOpen = false;
    });

    // Section icons mapping
    const sectionIcons = {
        "Getting Started": "rocket",
        "Learn Python": "book",
        Load: "download",
        Transform: "transform",
        Output: "upload",
        Special: "sparkles",
    };

    // Dynamic SEO
    $: currentPath = $page.url.pathname;
    $: currentItem = navSections
        .flatMap((s) => s.items)
        .find((i) => `${base}${i.path}` === currentPath);

    $: title = currentItem
        ? `${currentItem.title} | Python Data Tools`
        : "Python Data Tools | Learn Data Wrangling with Python";
    $: description = currentItem
        ? `Learn how to ${currentItem.title.toLowerCase()} using Pandas, Polars, DuckDB, and BigQuery.`
        : "The beginner-friendly guide to Python data wrangling. Compare syntax across platforms.";
</script>

<svelte:head>
    <title>{title}</title>
    <meta name="description" content={description} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content="website" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
        rel="stylesheet"
    />
</svelte:head>

<div class="layout">
    <Navbar on:toggleSidebar={toggleSidebar} on:toggleChat={toggleChat} />
    <Chat bind:isOpen={isChatOpen} />

    {#if isSidebarOpen}
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <div class="sidebar-overlay" onclick={toggleSidebar}></div>
    {/if}

    <nav class="sidebar" class:open={isSidebarOpen}>
        <div class="logo">
            <a href="{base}/">
                <Icon name="python" size={28} color="var(--accent-primary)" />
                <span class="logo-text">Python Data Tools</span>
            </a>
        </div>

        <div class="sidebar-search">
            <Search />
        </div>

        {#each navSections as section}
            <div class="nav-section">
                <h4>
                    <Icon
                        name={sectionIcons[section.section] || "book"}
                        size={14}
                    />
                    {section.section}
                </h4>
                <ul>
                    {#each section.items as item}
                        <li>
                            <a
                                href="{base}{item.path}"
                                class:active={$page.url.pathname.startsWith(
                                    `${base}${item.path}`,
                                )}
                            >
                                {item.title.replace(/^[🚀📥🔄📤🎯]\s*/, "")}
                            </a>
                        </li>
                    {/each}
                </ul>
            </div>
        {/each}

        <div class="nav-section platforms">
            <h4>
                <Icon name="layers" size={14} />
                Libraries
            </h4>
            <ul class="platforms-list">
                <li>
                    <Icon name="pandas" size={18} color="var(--pandas-color)" />
                    <span>Pandas 2.2</span>
                </li>
                <li>
                    <Icon name="polars" size={18} color="var(--polars-color)" />
                    <span>Polars 1.x</span>
                </li>
                <li>
                    <Icon name="duckdb" size={18} color="var(--duckdb-color)" />
                    <span>DuckDB 1.1</span>
                </li>
                <li>
                    <Icon
                        name="cloud"
                        size={18}
                        color="var(--bigquery-color)"
                    />
                    <span>BigQuery</span>
                </li>
            </ul>
        </div>
    </nav>

    <main class="content">
        <slot />
    </main>
</div>

<style>
    .layout {
        display: flex;
        min-height: 100vh;
    }

    .sidebar {
        width: 280px;
        background: var(--bg-secondary);
        border-right: 1px solid var(--border-color);
        padding: var(--space-6);
        position: fixed;
        height: 100vh;
        overflow-y: auto;
        z-index: 200;
        transition: transform var(--transition-slow);
    }

    .sidebar-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(4px);
        z-index: 150;
    }

    .logo a {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        text-decoration: none;
        margin-bottom: var(--space-6);
    }

    .logo-text {
        font-size: 1.1rem;
        font-weight: 700;
        background: linear-gradient(
            135deg,
            var(--accent-primary),
            var(--accent-secondary)
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .sidebar-search {
        margin-bottom: var(--space-6);
        display: none;
    }

    @media (max-width: 900px) {
        .sidebar-search {
            display: block;
        }
    }

    .nav-section {
        margin-bottom: var(--space-6);
    }

    .nav-section h4 {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        color: var(--text-muted);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        margin-bottom: var(--space-3);
    }

    .nav-section ul {
        list-style: none;
    }

    .nav-section li {
        margin-bottom: var(--space-1);
    }

    .nav-section a {
        display: block;
        padding: var(--space-2) var(--space-3);
        border-radius: var(--radius-md);
        color: var(--text-secondary);
        font-size: 0.9rem;
        transition: all var(--transition-fast);
        text-decoration: none;
    }

    .nav-section a:hover {
        background: var(--surface-hover);
        color: var(--text-primary);
        text-decoration: none;
    }

    .nav-section a.active {
        background: rgba(124, 58, 237, 0.15);
        color: var(--accent-primary);
        font-weight: 500;
    }

    .platforms-list li {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        padding: var(--space-2) 0;
        color: var(--text-secondary);
        font-size: 0.875rem;
    }

    .content {
        flex: 1;
        margin-left: 280px;
        padding: var(--space-8) var(--space-10);
        max-width: 1400px;
        margin-top: 64px;
    }

    @media (max-width: 900px) {
        .sidebar {
            transform: translateX(-100%);
        }

        .sidebar.open {
            transform: translateX(0);
        }

        .sidebar-overlay {
            display: block;
        }

        .content {
            margin-left: 0;
            padding: var(--space-4);
            margin-top: 60px;
        }
    }
</style>
