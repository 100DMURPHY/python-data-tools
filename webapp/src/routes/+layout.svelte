<script>
    import "../app.css";
    import { page } from "$app/stores";
    import { base } from "$app/paths";
    import navSections from "$lib/nav.json";
    import Navbar from "$lib/components/Navbar.svelte";
    import Search from "$lib/components/Search.svelte";
    import Chat from "$lib/components/Chat.svelte";
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

    // Dynamic SEO
    $: currentPath = $page.url.pathname;
    $: currentItem = navSections
        .flatMap((s) => s.items)
        .find((i) => `${base}${i.path}` === currentPath);

    $: title = currentItem
        ? `${currentItem.title} | Python Data Tools`
        : "Python Data Tools | Compare Pandas, Polars, DuckDB";
    $: description = currentItem
        ? `Learn how to handle ${currentItem.title} using Pandas, Polars, DuckDB, and BigQuery.`
        : "The definitive guide to comparing Python data wrangling syntax across platforms.";
</script>

<svelte:head>
    <title>{title}</title>
    <meta name="description" content={description} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:type" content="website" />
    <meta name="twitter:card" content="summary_large_image" />
</svelte:head>

<div class="layout">
    <Navbar on:toggleSidebar={toggleSidebar} on:toggleChat={toggleChat} />
    <Chat bind:isOpen={isChatOpen} />

    {#if isSidebarOpen}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div class="sidebar-overlay" on:click={toggleSidebar}></div>
    {/if}

    <nav class="sidebar" class:open={isSidebarOpen}>
        <div class="logo">
            <a href="{base}/">
                <h1>🐍 Python Data Tools</h1>
            </a>
        </div>

        <div class="sidebar-search">
            <Search />
        </div>

        {#each navSections as section}
            <div class="nav-section">
                <h4>{section.section}</h4>
                <ul>
                    {#each section.items as item}
                        <li>
                            <a
                                href="{base}{item.path}"
                                class:active={$page.url.pathname.startsWith(
                                    `${base}${item.path}`,
                                )}
                            >
                                {item.title}
                            </a>
                        </li>
                    {/each}
                </ul>
            </div>
        {/each}

        <div class="nav-section platforms">
            <h4>Libraries</h4>
            <ul class="platforms-list">
                <li><span class="icon">🐼</span> Pandas 2.2</li>
                <li><span class="icon">🐻‍❄️</span> Polars 1.x</li>
                <li><span class="icon">🦆</span> DuckDB 1.1</li>
                <li><span class="icon">☁️</span> BigQuery</li>
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
        width: 260px;
        background: var(--bg-secondary);
        border-right: 1px solid var(--border-color);
        padding: 1.5rem;
        position: fixed;
        height: 100vh;
        overflow-y: auto;
        z-index: 200;
        transition: transform 0.3s ease;
    }

    .sidebar-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(4px);
        z-index: 150;
    }

    .logo h1 {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        background: linear-gradient(
            135deg,
            var(--accent-blue),
            var(--accent-purple)
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }

    .sidebar-search {
        margin-bottom: 1.5rem;
        display: none;
    }

    @media (max-width: 900px) {
        .sidebar-search {
            display: block;
        }
    }

    .nav-section {
        margin-bottom: 2rem;
    }

    .nav-section h4 {
        color: var(--text-muted);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.75rem;
    }

    .nav-section ul {
        list-style: none;
    }

    .nav-section li {
        margin-bottom: 0.25rem;
    }

    .nav-section a {
        display: block;
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        color: var(--text-secondary);
        font-size: 0.875rem;
        transition: all 0.15s;
    }

    .nav-section a:hover {
        background: var(--bg-tertiary);
        color: var(--text-primary);
        text-decoration: none;
    }

    .nav-section a.active {
        background: color-mix(in srgb, var(--accent-blue) 20%, transparent);
        color: var(--accent-blue);
    }

    .platforms-list li {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 0;
        color: var(--text-secondary);
        font-size: 0.875rem;
    }

    .icon {
        font-size: 1rem;
    }

    .content {
        flex: 1;
        margin-left: 260px;
        padding: 2rem 3rem;
        max-width: 1600px;
        margin-top: 64px; /* Space for fixed navbar */
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
            padding: 1rem;
            margin-top: 60px; /* Space for fixed navbar */
        }
    }
</style>
