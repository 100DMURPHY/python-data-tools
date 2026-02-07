<script>
    import { createEventDispatcher } from "svelte";
    import { base } from "$app/paths";

    const dispatch = createEventDispatcher();

    function toggleSidebar() {
        dispatch("toggleSidebar");
    }
</script>

<nav class="navbar">
    <div class="logo">
        <a href="{base}/">
            <span>🐍 Python Data Tools</span>
        </a>
    </div>

    <button
        class="hamburger"
        on:click={toggleSidebar}
        aria-label="Toggle Navigation"
    >
        <svg viewBox="0 0 24 24" width="24" height="24">
            <path
                fill="currentColor"
                d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z"
            />
        </svg>
    </button>
</nav>

<style>
    .navbar {
        display: none;
        height: 60px;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
        padding: 0 1rem;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 100;
    }

    .logo span {
        font-weight: 700;
        font-size: 1.1rem;
        background: linear-gradient(
            135deg,
            var(--accent-blue),
            var(--accent-purple)
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hamburger {
        background: transparent;
        border: none;
        color: var(--text-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0.5rem;
        border-radius: 6px;
        transition: background 0.2s;
    }

    .hamburger:hover {
        background: var(--bg-tertiary);
    }

    @media (max-width: 900px) {
        .navbar {
            display: flex;
        }
    }
</style>
