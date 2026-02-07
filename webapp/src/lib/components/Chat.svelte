<script>
    import { onMount } from "svelte";
    import * as webllm from "@mlc-ai/web-llm";

    export let isOpen = false;

    // Chat State
    let messages = [
        {
            role: "system",
            content:
                "You are 'The Guardian', an AI assistant for Python Data Tools. You help users with Pandas, Polars, DuckDB, and BigQuery. Keep answers concise and code-heavy.",
        },
        {
            role: "assistant",
            content:
                "Hello! I'm The Guardian. How can I help you with your data wrangling today?",
        },
    ];
    let input = "";
    let isLoading = false;
    let progress = "";

    // Mode State
    let mode = "local"; // 'local' or 'byok'
    let apiKey = "";
    let apiBase = "https://api.openai.com/v1";
    let model = "gpt-4o-mini";
    let showSettings = false;

    // Local Mode State
    let engine = null;
    let isModelLoaded = false;
    const selectedModel = "Llama-3.1-8B-Instruct-q4f16_1-MLC";

    onMount(() => {
        const savedKey = localStorage.getItem("guardian_api_key");
        const savedBase = localStorage.getItem("guardian_api_base");
        const savedMode = localStorage.getItem("guardian_mode");
        if (savedKey) apiKey = savedKey;
        if (savedBase) apiBase = savedBase;
        if (savedMode) mode = savedMode;
    });

    async function saveSettings() {
        localStorage.setItem("guardian_api_key", apiKey);
        localStorage.setItem("guardian_api_base", apiBase);
        localStorage.setItem("guardian_mode", mode);
        showSettings = false;
    }

    async function initLocalEngine() {
        if (engine) return;
        isLoading = true;

        try {
            engine = await webllm.CreateMLCEngine(selectedModel, {
                initProgressCallback: (report) => {
                    progress = report.text;
                },
            });
            isModelLoaded = true;
        } catch (err) {
            console.error("Web-LLM Init Error:", err);
            progress =
                "Error: This feature requires a WebGPU-enabled browser. Switching to BYOK mode is recommended.";
            // Auto-switch to settings if local fails
            showSettings = true;
        } finally {
            isLoading = false;
        }
    }

    async function sendMessage() {
        if (!input.trim() || isLoading) return;

        const userMsg = { role: "user", content: input };
        messages = [...messages, userMsg];
        const currentInput = input;
        input = "";
        isLoading = true;

        if (mode === "local") {
            await handleLocalMessage(userMsg);
        } else {
            await handleBYOKMessage();
        }
    }

    async function handleLocalMessage(userMsg) {
        if (!isModelLoaded) {
            await initLocalEngine();
            if (!isModelLoaded) {
                isLoading = false;
                return;
            }
        }

        try {
            const reply = await engine.chat.completions.create({
                messages: messages.map((m) => ({
                    role: m.role,
                    content: m.content,
                })),
            });
            const assistantMsg = {
                role: "assistant",
                content: reply.choices[0].message.content,
            };
            messages = [...messages, assistantMsg];
        } catch (err) {
            messages = [
                ...messages,
                {
                    role: "assistant",
                    content:
                        "Local AI Error. Check WebGPU support or switch to BYOK mode.",
                },
            ];
        } finally {
            isLoading = false;
        }
    }

    async function handleBYOKMessage() {
        if (!apiKey) {
            messages = [
                ...messages,
                {
                    role: "assistant",
                    content:
                        "Please provide an API key in settings to use BYOK mode.",
                },
            ];
            showSettings = true;
            isLoading = false;
            return;
        }

        try {
            const response = await fetch(`${apiBase}/chat/completions`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${apiKey}`,
                },
                body: JSON.stringify({
                    model: model,
                    messages: messages.map((m) => ({
                        role: m.role,
                        content: m.content,
                    })),
                }),
            });

            const data = await response.json();
            if (data.error) throw new Error(data.error.message);

            const assistantMsg = {
                role: "assistant",
                content: data.choices[0].message.content,
            };
            messages = [...messages, assistantMsg];
        } catch (err) {
            messages = [
                ...messages,
                { role: "assistant", content: `API Error: ${err.message}` },
            ];
        } finally {
            isLoading = false;
        }
    }

    function handleKeydown(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    }
</script>

{#if isOpen}
    <div
        class="chat-overlay"
        role="presentation"
        on:click={() => (isOpen = false)}
        on:keydown={(e) => e.key === "Escape" && (isOpen = false)}
    ></div>
    <div class="chat-window">
        <div class="chat-header">
            <div class="header-info">
                <span class="bot-icon">🛡️</span>
                <div>
                    <h3>The Guardian</h3>
                    <p class="status">
                        {mode === "local"
                            ? isModelLoaded
                                ? "Local Mode (GPU)"
                                : "Local Mode (Ready)"
                            : "Cloud Mode (BYOK)"}
                    </p>
                </div>
            </div>
            <div class="header-actions">
                <button
                    class="settings-btn"
                    on:click={() => (showSettings = !showSettings)}>⚙️</button
                >
                <button class="close-btn" on:click={() => (isOpen = false)}
                    >&times;</button
                >
            </div>
        </div>

        <div class="chat-messages">
            {#if showSettings}
                <div class="settings-panel">
                    <h4>Settings</h4>
                    <div class="setting-item">
                        <label>Inference Mode</label>
                        <select bind:value={mode}>
                            <option value="local">Local (Web-LLM/WebGPU)</option
                            >
                            <option value="byok">Cloud (BYOK Key)</option>
                        </select>
                    </div>

                    {#if mode === "byok"}
                        <div class="setting-item">
                            <label>OpenAI-Compatible Key</label>
                            <input
                                type="password"
                                bind:value={apiKey}
                                placeholder="sk-..."
                            />
                        </div>
                        <div class="setting-item">
                            <label>API Base URL</label>
                            <input
                                type="text"
                                bind:value={apiBase}
                                placeholder="https://api.openai.com/v1"
                            />
                        </div>
                    {/if}

                    <button class="save-btn" on:click={saveSettings}
                        >Save & Core</button
                    >
                    <p class="settings-note">
                        Local mode needs WebGPU. BYOK mode uses your own API
                        credits.
                    </p>
                </div>
            {:else}
                {#each messages.filter((m) => m.role !== "system") as msg}
                    <div class="message {msg.role}">
                        <div class="message-content">
                            {msg.content}
                        </div>
                    </div>
                {/each}

                {#if isLoading}
                    <div class="message assistant loading">
                        <div class="message-content">
                            {#if mode === "local" && !isModelLoaded}
                                <div class="progress-bar">
                                    <p>Initializing Local LLM...</p>
                                    <p class="progress-detail">{progress}</p>
                                </div>
                            {:else}
                                <span class="typing-dot"></span>
                                <span class="typing-dot"></span>
                                <span class="typing-dot"></span>
                            {/if}
                        </div>
                    </div>
                {/if}
            {/if}
        </div>

        {#if !showSettings}
            <div class="chat-input">
                <textarea
                    placeholder="Ask about Pandas, Polars..."
                    bind:value={input}
                    on:keydown={handleKeydown}
                ></textarea>
                <button
                    on:click={sendMessage}
                    disabled={isLoading || !input.trim()}
                >
                    {mode === "local" && !isModelLoaded ? "Init" : "Send"}
                </button>
            </div>
        {/if}
    </div>
{/if}

<style>
    .chat-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(4px);
        z-index: 1000;
    }

    .chat-window {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 400px;
        height: 600px;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
        z-index: 1001;
        overflow: hidden;
        animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes slideIn {
        from {
            transform: translateY(20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    .chat-header {
        padding: 1rem 1.5rem;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .header-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .bot-icon {
        font-size: 1.5rem;
    }

    .header-info h3 {
        font-size: 1rem;
        margin: 0;
        font-weight: 600;
    }

    .status {
        font-size: 0.75rem;
        color: var(--accent-green);
        margin: 0;
    }

    .settings-btn {
        background: transparent;
        border: none;
        cursor: pointer;
        font-size: 1.1rem;
        opacity: 0.6;
        transition: opacity 0.2s;
    }

    .settings-btn:hover {
        opacity: 1;
    }

    .close-btn {
        background: transparent;
        border: none;
        color: var(--text-muted);
        font-size: 1.5rem;
        cursor: pointer;
    }

    .chat-messages {
        flex: 1;
        padding: 1.5rem;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        background: #0f172a;
    }

    .settings-panel {
        color: white;
    }

    .settings-panel h4 {
        margin-top: 0;
        margin-bottom: 1.5rem;
        font-size: 1rem;
    }

    .setting-item {
        margin-bottom: 1.25rem;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .setting-item label {
        font-size: 0.8rem;
        color: var(--text-muted);
    }

    .setting-item input,
    .setting-item select {
        padding: 0.6rem;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        color: white;
        outline: none;
    }

    .save-btn {
        width: 100%;
        background: var(--accent-blue);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        margin-top: 1rem;
    }

    .settings-note {
        font-size: 0.7rem;
        color: var(--text-muted);
        margin-top: 1rem;
        line-height: 1.4;
    }

    .message {
        display: flex;
        flex-direction: column;
    }

    .message.user {
        align-items: flex-end;
    }

    .message-content {
        padding: 0.75rem 1rem;
        border-radius: 12px;
        font-size: 0.9rem;
        line-height: 1.5;
        max-width: 85%;
        white-space: pre-wrap;
    }

    .user .message-content {
        background: var(--accent-blue);
        color: white;
        border-bottom-right-radius: 2px;
    }

    .assistant .message-content {
        background: var(--bg-tertiary);
        color: var(--text-primary);
        border-bottom-left-radius: 2px;
    }

    .chat-input {
        padding: 1rem;
        background: var(--bg-secondary);
        border-top: 1px solid var(--border-color);
        display: flex;
        gap: 0.75rem;
        align-items: flex-end;
    }

    textarea {
        flex: 1;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.75rem;
        color: var(--text-primary);
        font-family: inherit;
        font-size: 0.9rem;
        resize: none;
        height: 60px;
        outline: none;
    }

    textarea:focus {
        border-color: var(--accent-blue);
    }

    button.send-btn {
        background: var(--accent-blue);
        color: white;
        border: none;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: opacity 0.2s;
        height: 40px;
    }

    @media (max-width: 600px) {
        .chat-window {
            bottom: 0;
            right: 0;
            width: 100%;
            height: 100%;
            border-radius: 0;
        }
    }
</style>
