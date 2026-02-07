<script>
  import { base } from "$app/paths";
</script>

<div class="hero">
  <h1>🐍 Python Data Tools</h1>
  <p class="tagline">Compare data wrangling syntax across platforms</p>

  <div class="platforms">
    <div class="platform-card">
      <span class="icon">🐼</span>
      <span class="name">Pandas</span>
      <span class="desc">The baseline</span>
    </div>
    <div class="platform-card">
      <span class="icon">🦆</span>
      <span class="name">DuckDB</span>
      <span class="desc">SQL analytics</span>
    </div>
    <div class="platform-card">
      <span class="icon">☁️</span>
      <span class="name">BigQuery</span>
      <span class="desc">Cloud SQL</span>
    </div>
    <div class="platform-card">
      <span class="icon">🐻‍❄️</span>
      <span class="name">Polars</span>
      <span class="desc">High-perf</span>
    <div class="cta-row">
      <a href="{base}/setup" class="btn primary">🚀 Get Started with UV</a>
    </div>
  </div>
</div>

<section class="intro">
  <h2>About This Project</h2>
  <p>
    Based on <strong>"Python for Data Analysis, 3rd Edition"</strong> by Wes McKinney,
    this project converts every data wrangling example to multiple platforms so you
    can compare syntax and performance.
  </p>

  <div class="features">
    <div class="feature">
      <h3>📊 Side-by-Side</h3>
      <p>Toggle platforms to compare only what you need</p>
    </div>
    <div class="feature">
      <h3>⏱️ Benchmarks</h3>
      <p>Educational timing comparisons (not marketing)</p>
    </div>
    <div class="feature">
      <h3>🔌 Extensible</h3>
      <p>Designed for future platforms: ibis, chdb, more</p>
    </div>
  </div>
</section>

<section class="workflow">
  <h2>Wrangling Workflow</h2>
  <div class="workflow-grid">
    <a href="{base}/load/csv" class="workflow-card">
      <span class="icon">📥</span>
      <span class="title">Load</span>
      <span class="desc">CSV, Parquet, JSON, Cloud</span>
    </a>
    <div class="workflow-card disabled">
      <span class="icon">🔄</span>
      <span class="title">Transform</span>
      <span class="desc">Filter, Join, Aggr, Pivot</span>
    </div>
    <div class="workflow-card disabled">
      <span class="icon">📤</span>
      <span class="title">Output</span>
      <span class="desc">Files, DBs, BigQuery</span>
    </div>
    <div class="workflow-card disabled">
      <span class="icon">🎯</span>
      <span class="title">Special</span>
      <span class="desc">Excel, Charts, ML, LLM</span>
    </div>
  </div>
</section>

<style>
  .hero {
    text-align: center;
    padding: 3rem 0;
    border-bottom: 1px solid var(--border-color);
    margin-bottom: 3rem;
  }

  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(
      135deg,
      var(--accent-blue),
      var(--accent-purple)
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .tagline {
    color: var(--text-secondary);
    font-size: 1.1rem;
    margin-bottom: 2rem;
  }

  .platforms {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }

  .platform-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem 1.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    min-width: 100px;
  }

  .platform-card .icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }

  .platform-card .name {
    font-weight: 600;
    color: var(--text-primary);
  }

  .platform-card .desc {
    font-size: 0.75rem;
    color: var(--text-muted);
  }

  .intro {
    margin-bottom: 3rem;
  }

  .intro h2 {
    margin-bottom: 1rem;
  }

  .intro p {
    color: var(--text-secondary);
    max-width: 600px;
  }

  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .feature {
    padding: 1.5rem;
    background: var(--bg-secondary);
    border-radius: 8px;
  }

  .feature h3 {
    margin-bottom: 0.5rem;
  }

  .feature p {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  /* Workflow styles */
  .workflow {
    margin-bottom: 3rem;
  }

  .workflow h2 {
    margin-bottom: 1.5rem;
  }

  .workflow-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.5rem;
  }

  .workflow-card {
    display: flex;
    flex-direction: column;
    padding: 1.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    transition: all 0.2s;
    text-decoration: none;
  }

  a.workflow-card:hover {
    border-color: var(--accent-blue);
    transform: translateY(-2px);
  }

  .workflow-card.disabled {
    opacity: 0.5;
    cursor: default;
  }

  .workflow-card .icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .workflow-card .title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
  }

  .workflow-card .desc {
    font-size: 0.875rem;
    color: var(--text-muted);
  }
</style>
