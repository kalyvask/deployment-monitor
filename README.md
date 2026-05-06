# AI Deployment Research Monitor

A Python-based research monitoring tool that automatically scans multiple sources (news sites, Reddit, Hacker News, blogs, RSS feeds) for content relevant to AI deployment strategies, implementation models, and the latest AI trends.

## Personalize this for your own use

This repo ships with the maintainer's curated keywords, sources, and target companies. If you forked or cloned it, do these steps in order before running anything — otherwise you will be researching someone else's interests.

1. **Copy the env file:** `cp .env.example .env`. The `.env` file is gitignored — your secrets stay local.
2. **Set your Anthropic API key in `.env`:** `ANTHROPIC_API_KEY=sk-ant-...` Get one at [console.anthropic.com](https://console.anthropic.com). Required for AI analysis.
3. **Set email delivery in `.env`** so the newsletter can reach you. Edit these vars:
   - `SMTP_HOST` (default `smtp.gmail.com`)
   - `SMTP_PORT` (default `587`)
   - `SMTP_USER=your_email@gmail.com`
   - `SMTP_PASSWORD=your_app_password` — for Gmail, generate an App Password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - `REPORT_EMAIL_TO=where_the_newsletter_goes@example.com`
   - `REPORT_EMAIL_FROM=` (optional; defaults to `SMTP_USER`)
4. **(Optional) Set Reddit credentials in `.env`** if you want Reddit scraping: `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`. Create an app at [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps). Without these, Reddit is skipped — HN and RSS still work.
5. **Edit `src/config.py` to swap in your own focus areas.** The defaults are tuned for AI deployment / observability research. Replace these lists with what you actually care about:
   - `PRIMARY_KEYWORDS` and `SECONDARY_KEYWORDS` — the terms the relevance scorer matches on (primary = higher weight)
   - `EXCLUSION_KEYWORDS` — terms that filter articles out (e.g. crypto, web3)
   - `REDDIT_SUBREDDITS` — list of subreddit names (no `r/` prefix)
   - `RSS_FEEDS` — dict of `{name: url}` for blogs and news
   - `TARGET_COMPANIES`, `COMPANY_TIER_A`, `COMPANY_TIER_B`, `COMPANY_TIER_C` — companies to flag and weight in scoring
   - `INDUSTRY_VERTICALS` — sector-classification keyword groups
   - `TREND_CATEGORIES` — the trend buckets shown in the UI
6. **Set up the scheduled newsletter (Windows):** `cp run_newsletter.bat.example run_newsletter.bat`, then edit two lines inside it:
   - `cd /d "C:\path\to\your\clone\ai-deployment-monitor"` — point to your local clone
   - `python main.py newsletter --type executive --to your_email@example.com` — set your recipient

   Then point Windows Task Scheduler at `run_newsletter.bat`. The `.bat` file (and `newsletter_log.txt`) are gitignored.

   **Cross-platform alternative:** skip the `.bat` and run `python main.py daemon --interval 4h`, or wire `python main.py newsletter ...` into cron / launchd.
7. **Initialize and verify:** `python main.py init` then `python main.py run` to confirm the pipeline works end-to-end.

**What stays local (gitignored, never pushed):** `.env`, `data/research.db` (your scraped articles), `output/reports/*.md` (generated reports), `drafts/`, `run_newsletter.bat`, `newsletter_log.txt`, and any `*.log` files.

## Features

- **Web UI Dashboard**: Interactive Streamlit interface for browsing and analyzing content
- **Multi-source scraping**: Reddit, Hacker News, RSS/Atom feeds
- **Intelligent relevance scoring**: Keyword-based filtering with weighted scoring
- **AI-powered analysis**: Claude API integration for content summarization and insight extraction
- **Trend tracking**: Monitor emerging AI trends like agents, RAG, fine-tuning, and more
- **Automated reports**: Weekly and daily digest generation in Markdown format
- **SQLite storage**: Lightweight, portable database
- **CLI interface**: Command-line tool for automation and scripting

## Quick Start

### 1. Installation

```bash
# Navigate to the project
cd ai-deployment-monitor

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Required for AI analysis
ANTHROPIC_API_KEY=your_anthropic_api_key

# Optional: For Reddit scraping
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=AIDeploymentMonitor/1.0
```

**Getting API Keys:**

- **Anthropic API**: Sign up at [console.anthropic.com](https://console.anthropic.com)
- **Reddit API**: Create an app at [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

### 3. Launch the Web UI

```bash
streamlit run app.py
```

This opens the dashboard at `http://localhost:8501`

![Dashboard Preview](docs/dashboard.png)

### 4. Or Use the CLI

```bash
# Initialize database
python main.py init

# Run full pipeline
python main.py run

# Or step by step:
python main.py scrape
python main.py analyze
python main.py report --type weekly
```

## Web UI Features

### Dashboard
- Overview of collected articles and metrics
- Top relevant articles at a glance
- Company mention distribution
- Source breakdown charts

### Article Browser
- Filter by relevance score
- Sort by date or relevance
- View summaries and matched keywords

### Search
- Full-text search across all articles
- Suggested search terms for quick exploration

### Trend Analysis
- Track 8 major AI trend categories:
  - AI Agents & Autonomy
  - LLM Infrastructure
  - RAG & Knowledge
  - Fine-tuning & Customization
  - AI Coding Tools
  - Enterprise AI
  - AI Safety
  - Open Source AI
- Timeline charts showing article volume

### Reports
- Generate weekly or daily reports
- Preview reports in the browser
- Save as Markdown files

### Settings
- API configuration status
- Database management
- Manual scraper controls

## CLI Commands

| Command | Description |
|---------|-------------|
| `streamlit run app.py` | Launch web UI |
| `python main.py init` | Initialize database and seed sources |
| `python main.py scrape` | Scrape content from sources |
| `python main.py analyze` | Analyze articles with AI |
| `python main.py report` | Generate research reports |
| `python main.py view` | View recent articles |
| `python main.py search <query>` | Search articles |
| `python main.py stats` | Show database statistics |
| `python main.py export` | Export data to CSV/JSON |
| `python main.py run` | Run full pipeline |
| `python main.py daemon` | Run in scheduled mode |

### Command Options

```bash
# Scrape specific source
python main.py scrape --source hackernews

# View articles sorted by relevance
python main.py view --limit 30 --sort relevance

# Export to CSV
python main.py export --format csv --output data.csv

# Run daemon with custom interval
python main.py daemon --interval 4h
```

## Project Structure

```
ai-deployment-monitor/
├── app.py                  # Streamlit web UI
├── main.py                 # CLI entry point
├── src/
│   ├── config.py           # Configuration and keywords
│   ├── database.py         # SQLite operations
│   ├── scrapers/
│   │   ├── reddit.py       # Reddit scraper
│   │   ├── hackernews.py   # HN API scraper
│   │   └── rss.py          # RSS feed scraper
│   ├── processors/
│   │   ├── relevance.py    # Relevance scoring
│   │   └── analyzer.py     # Claude API analysis
│   ├── reports/
│   │   └── generator.py    # Report generation
│   └── utils/
│       └── helpers.py
├── data/
│   └── research.db         # SQLite database
├── output/
│   └── reports/            # Generated reports
├── requirements.txt
├── .env.example
└── README.md
```

## Monitored Sources

### Reddit Subreddits
- r/MachineLearning, r/artificial, r/LocalLLaMA
- r/ChatGPT, r/ClaudeAI, r/OpenAI
- r/singularity, r/mlops
- r/startups, r/SaaS, r/ProductManagement

### RSS Feeds
**News**: TechCrunch, VentureBeat, MIT Tech Review, The Verge, Wired, Ars Technica

**Company Blogs**: OpenAI, Anthropic, DeepMind, Meta AI, Databricks, HuggingFace, LangChain

**VC Blogs**: a16z, Sequoia, First Round Review

**Research**: arXiv CS.AI, arXiv CS.CL

### Hacker News
- Top, New, and Best stories
- Show HN posts

## Latest AI Trends Tracked

The tool focuses on cutting-edge 2025 AI trends:

**AI Agents & Autonomy**
- Agentic AI, autonomous agents, multi-agent systems
- Computer use, browser automation

**LLM Infrastructure**
- Inference at scale, model serving, LLMOps
- GPU clusters, optimization

**RAG & Knowledge**
- Retrieval augmented generation
- Vector databases, embeddings, knowledge graphs

**AI Coding Tools**
- Cursor, Copilot, Replit, Codeium
- AI pair programming

**Enterprise AI**
- Deployment, ROI, adoption patterns
- Governance, compliance, private AI

**Target Companies (60+)**
- AI Labs: OpenAI, Anthropic, DeepMind, Mistral, xAI, DeepSeek
- Infrastructure: Databricks, Scale AI, Modal, Replicate, Groq
- Startups: Harvey, Glean, Cursor, Perplexity, Cognition
- And many more...

## Cost Management

The tool uses Claude API for content analysis. To manage costs:

- Use `--skip-api` flag for keyword-only analysis
- Limit articles analyzed: `python main.py analyze --limit 20`
- In the UI, analysis only runs when you click "Analyze Articles"
- Token usage is tracked and displayed

## Troubleshooting

**Web UI won't start:**
- Ensure Streamlit is installed: `pip install streamlit`
- Check port 8501 is available

**Reddit API not working:**
- Reddit credentials are optional
- Tool works without Reddit using HN and RSS feeds

**No articles found:**
- Click "Fetch New Content" in the sidebar
- Check network connectivity
- Some RSS feeds may be temporarily unavailable

**Claude API errors:**
- Verify ANTHROPIC_API_KEY in .env
- Analysis works without API (uses keyword scoring only)

## License

MIT License
