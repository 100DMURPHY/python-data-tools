<script>
  import { base } from "$app/paths";
  import Icon from "$lib/components/Icon.svelte";
</script>

<div class="hero">
  <div class="hero-badge">
    <Icon name="python" size={20} />
    <span>Beginner Friendly</span>
  </div>

  <h1>Learn Python Data Tools</h1>
  <p class="tagline">
    Your journey from zero to data analysis starts here.<br />
    Compare syntax across <strong>Pandas</strong>, <strong>Polars</strong>,
    <strong>DuckDB</strong>, and <strong>BigQuery</strong>.
  </p>

  <div class="cta-row">
    <a href="{base}/setup" class="btn primary">
      <Icon name="rocket" size={18} />
      Get Started
    </a>
    <a href="{base}/load/csv" class="btn secondary">
      <Icon name="play" size={18} />
      See Examples
    </a>
  </div>
</div>

<section class="platforms-section">
  <h2>Libraries You'll Learn</h2>
  <div class="platforms-grid">
    <div class="platform-card">
      <div class="platform-icon" style="background: var(--pandas-bg);">
        <Icon name="pandas" size={32} color="var(--pandas-color)" />
      </div>
      <h3>Pandas</h3>
      <p>The most popular Python data library. Great for learning.</p>
      <span class="badge">v2.2</span>
    </div>
    <div class="platform-card">
      <div class="platform-icon" style="background: var(--polars-bg);">
        <Icon name="polars" size={32} color="var(--polars-color)" />
      </div>
      <h3>Polars</h3>
      <p>Lightning fast. Built in Rust for maximum performance.</p>
      <span class="badge">v1.x</span>
    </div>
    <div class="platform-card">
      <div class="platform-icon" style="background: var(--duckdb-bg);">
        <Icon name="duckdb" size={32} color="var(--duckdb-color)" />
      </div>
      <h3>DuckDB</h3>
      <p>SQL inside Python. Perfect if you know SQL.</p>
      <span class="badge">v1.1</span>
    </div>
    <div class="platform-card">
      <div class="platform-icon" style="background: var(--bigquery-bg);">
        <Icon name="cloud" size={32} color="var(--bigquery-color)" />
      </div>
      <h3>BigQuery</h3>
      <p>Google's cloud data warehouse. Scales infinitely.</p>
      <span class="badge">Cloud</span>
    </div>
  </div>
</section>

<section class="workflow-section">
  <h2>The Data Workflow</h2>
  <p class="section-desc">
    Every data project follows this pattern. Master each step and you'll be
    unstoppable.
  </p>

  <div class="workflow-grid">
    <a href="{base}/load/csv" class="workflow-card">
      <div class="workflow-icon">
        <Icon name="download" size={28} />
      </div>
      <div class="workflow-content">
        <h3>Load</h3>
        <p>Read data from files, databases, and cloud sources</p>
      </div>
      <span class="workflow-arrow">→</span>
    </a>

    <div class="workflow-card coming-soon">
      <div class="workflow-icon">
        <Icon name="transform" size={28} />
      </div>
      <div class="workflow-content">
        <h3>Transform</h3>
        <p>Filter, sort, join, and reshape your data</p>
      </div>
      <span class="workflow-badge">Coming Soon</span>
    </div>

    <div class="workflow-card coming-soon">
      <div class="workflow-icon">
        <Icon name="upload" size={28} />
      </div>
      <div class="workflow-content">
        <h3>Output</h3>
        <p>Save to files, databases, or cloud storage</p>
      </div>
      <span class="workflow-badge">Coming Soon</span>
    </div>

    <div class="workflow-card coming-soon">
      <div class="workflow-icon">
        <Icon name="sparkles" size={28} />
      </div>
      <div class="workflow-content">
        <h3>Special</h3>
        <p>Excel reports, charts, ML, and AI integration</p>
      </div>
      <span class="workflow-badge">Coming Soon</span>
    </div>
  </div>
</section>

<section class="try-section">
  <div class="try-card">
    <div class="try-left">
      <h2>Try It Right Now</h2>
      <p>
        No installation needed. Copy this command and paste it in your terminal:
      </p>
    </div>
    <div class="try-right">
      <code class="try-command"
        >curl -LsSf https://astral.sh/uv/install.sh | sh && uv run
        https://raw.githubusercontent.com/pythondatatools/python-data-tools/main/chapters/load/load_csv_pandas.py</code
      >
      <a href="{base}/setup" class="try-link">
        What is UV? <Icon name="rocket" size={14} />
      </a>
    </div>
  </div>
</section>

<section class="features-section">
  <h2>Why This Site?</h2>
  <div class="features-grid">
    <div class="feature">
      <div class="feature-icon">
        <Icon name="chart" size={24} />
      </div>
      <h3>Side-by-Side Comparison</h3>
      <p>
        See how the same operation looks in each library. Pick what feels right.
      </p>
    </div>
    <div class="feature">
      <div class="feature-icon">
        <Icon name="copy" size={24} />
      </div>
      <h3>Copy & Run</h3>
      <p>
        Every example is ready to run. Just copy and paste into your terminal.
      </p>
    </div>
    <div class="feature">
      <div class="feature-icon">
        <Icon name="brain" size={24} />
      </div>
      <h3>AI-Ready</h3>
      <p>Learn the basics, then leverage AI coding assistants to go further.</p>
    </div>
  </div>
</section>

<style>
  /* Hero Section */
  .hero {
    text-align: center;
    padding: var(--space-12) 0 var(--space-10);
    max-width: 700px;
    margin: 0 auto;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: var(--space-2);
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    padding: var(--space-2) var(--space-4);
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-bottom: var(--space-6);
  }

  .hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: var(--space-4);
    background: linear-gradient(
      135deg,
      var(--text-primary) 0%,
      var(--accent-primary) 50%,
      var(--accent-secondary) 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
  }

  .tagline {
    font-size: 1.2rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: var(--space-8);
  }

  .tagline strong {
    color: var(--text-primary);
  }

  .cta-row {
    display: flex;
    gap: var(--space-4);
    justify-content: center;
    flex-wrap: wrap;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-3) var(--space-6);
    border-radius: var(--radius-lg);
    font-weight: 600;
    font-size: 1rem;
    text-decoration: none;
    transition: all var(--transition-base);
  }

  .btn.primary {
    background: linear-gradient(135deg, var(--accent-primary), #9333ea);
    color: white;
    box-shadow:
      var(--shadow-md),
      0 0 20px rgba(124, 58, 237, 0.3);
  }

  .btn.primary:hover {
    transform: translateY(-2px);
    box-shadow:
      var(--shadow-lg),
      0 0 30px rgba(124, 58, 237, 0.4);
  }

  .btn.secondary {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
  }

  .btn.secondary:hover {
    background: var(--bg-elevated);
    border-color: var(--accent-primary);
  }

  /* Platforms Section */
  .platforms-section {
    margin: var(--space-12) 0;
  }

  .platforms-section h2 {
    text-align: center;
    margin-bottom: var(--space-8);
  }

  .platforms-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--space-5);
  }

  .platform-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-6);
    text-align: center;
    transition: all var(--transition-base);
  }

  .platform-card:hover {
    border-color: var(--accent-primary);
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
  }

  .platform-icon {
    width: 64px;
    height: 64px;
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto var(--space-4);
  }

  .platform-card h3 {
    font-size: 1.1rem;
    margin-bottom: var(--space-2);
  }

  .platform-card p {
    font-size: 0.875rem;
    margin-bottom: var(--space-3);
  }

  .badge {
    display: inline-block;
    background: var(--bg-tertiary);
    color: var(--text-muted);
    font-size: 0.7rem;
    padding: var(--space-1) var(--space-2);
    border-radius: var(--radius-sm);
    font-weight: 500;
  }

  /* Workflow Section */
  .workflow-section {
    margin: var(--space-12) 0;
  }

  .section-desc {
    text-align: center;
    max-width: 600px;
    margin: 0 auto var(--space-8);
  }

  .workflow-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: var(--space-4);
  }

  .workflow-card {
    display: flex;
    align-items: center;
    gap: var(--space-4);
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-5);
    text-decoration: none;
    transition: all var(--transition-base);
    position: relative;
  }

  a.workflow-card:hover {
    border-color: var(--accent-primary);
    background: var(--bg-tertiary);
  }

  .workflow-card.coming-soon {
    opacity: 0.6;
  }

  .workflow-icon {
    width: 48px;
    height: 48px;
    background: var(--bg-tertiary);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent-primary);
    flex-shrink: 0;
  }

  .workflow-content h3 {
    font-size: 1rem;
    color: var(--text-primary);
    margin-bottom: var(--space-1);
  }

  .workflow-content p {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin: 0;
  }

  .workflow-arrow {
    color: var(--accent-primary);
    font-size: 1.2rem;
    margin-left: auto;
  }

  .workflow-badge {
    position: absolute;
    top: var(--space-2);
    right: var(--space-2);
    background: var(--bg-tertiary);
    color: var(--text-muted);
    font-size: 0.65rem;
    padding: var(--space-1) var(--space-2);
    border-radius: var(--radius-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  /* Try Section */
  .try-section {
    margin: var(--space-12) 0;
  }

  .try-card {
    background: linear-gradient(
      135deg,
      var(--bg-secondary),
      var(--bg-tertiary)
    );
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    padding: var(--space-8);
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: var(--space-8);
    align-items: center;
  }

  .try-left h2 {
    margin-bottom: var(--space-2);
    margin-top: 0;
  }

  .try-left p {
    margin: 0;
  }

  .try-command {
    display: block;
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: var(--space-4);
    font-size: 0.8rem;
    color: var(--accent-secondary);
    word-break: break-all;
    margin-bottom: var(--space-3);
  }

  .try-link {
    display: inline-flex;
    align-items: center;
    gap: var(--space-1);
    font-size: 0.85rem;
  }

  @media (max-width: 768px) {
    .try-card {
      grid-template-columns: 1fr;
      gap: var(--space-4);
    }
  }

  /* Features Section */
  .features-section {
    margin: var(--space-12) 0;
  }

  .features-section h2 {
    text-align: center;
    margin-bottom: var(--space-8);
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-6);
  }

  .feature {
    text-align: center;
    padding: var(--space-6);
  }

  .feature-icon {
    width: 56px;
    height: 56px;
    background: linear-gradient(
      135deg,
      var(--accent-primary),
      var(--accent-secondary)
    );
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto var(--space-4);
    color: white;
  }

  .feature h3 {
    font-size: 1.1rem;
    margin-bottom: var(--space-2);
  }

  .feature p {
    font-size: 0.9rem;
  }

  /* Responsive */
  @media (max-width: 600px) {
    .hero h1 {
      font-size: 2rem;
    }

    .tagline {
      font-size: 1rem;
    }

    .cta-row {
      flex-direction: column;
      align-items: center;
    }

    .btn {
      width: 100%;
      justify-content: center;
    }
  }
</style>
