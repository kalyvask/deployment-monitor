"""Configuration and constants for the AI Deployment Research Monitor."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables (override=True ensures .env takes precedence)
load_dotenv(override=True)

# Base paths — use /tmp on Vercel (read-only filesystem)
VERCEL = os.getenv("VERCEL", "")
BASE_DIR = Path(__file__).parent.parent

if VERCEL:
    DATA_DIR = Path("/tmp/data")
    OUTPUT_DIR = Path("/tmp/output")
    REPORTS_DIR = OUTPUT_DIR / "reports"
else:
    DATA_DIR = BASE_DIR / "data"
    OUTPUT_DIR = BASE_DIR / "output"
    REPORTS_DIR = OUTPUT_DIR / "reports"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

# Database
DATABASE_PATH = DATA_DIR / "research.db"

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "AIDeploymentMonitor/1.0")

# Email / SMTP settings
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", "587")
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
REPORT_EMAIL_TO = os.getenv("REPORT_EMAIL_TO", "")
REPORT_EMAIL_FROM = os.getenv("REPORT_EMAIL_FROM", "")

# Claude model
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

# Scraping settings
DEFAULT_SCRAPE_INTERVAL_HOURS = 6
REQUEST_TIMEOUT = 10 if VERCEL else 30
REQUEST_DELAY = 0.1 if VERCEL else 1.0  # Faster on Vercel, polite locally

# Relevance threshold
RELEVANCE_THRESHOLD = 0.6

# Recency controls
# Reject articles whose published_date is older than this at ingestion time.
MAX_ARTICLE_AGE_DAYS = 14
# Half-life used when applying freshness decay to relevance scores at report time.
# An article 7 days old is worth half a fresh one; 14 days old is worth a quarter.
FRESHNESS_HALF_LIFE_DAYS = 7

# =============================================================================
# LATEST AI TRENDS & KEYWORDS (2025)
# =============================================================================

# Primary keywords (higher weight) - Focus on cutting-edge trends
PRIMARY_KEYWORDS = [
    # AI Deployment & Implementation
    "ai deployment",
    "ai implementation",
    "forward deployment",
    "forward deployed engineer",
    "forward-deployed",
    "ai pilot",
    "proof of concept",
    "ai rollout",
    "enterprise ai adoption",
    "ai success metrics",
    "ai roi",
    "design partners",
    "land and expand",
    "ai go-to-market",
    "time to value",

    # 2025 AI Trends - Agents & Autonomy
    "ai agents",
    "agentic ai",
    "autonomous agents",
    "multi-agent",
    "agent framework",
    "agent orchestration",
    "computer use",
    "browser automation",
    "ai assistant",
    "copilot",

    # AI Infrastructure & Scaling
    "inference at scale",
    "model serving",
    "llm ops",
    "llmops",
    "gpu cluster",
    "inference optimization",
    "model deployment",
    "ai infrastructure",

    # RAG & Knowledge Systems
    "rag",
    "retrieval augmented",
    "vector database",
    "knowledge graph",
    "semantic search",
    "embeddings",

    # Fine-tuning & Customization
    "fine-tuning",
    "fine tuning",
    "lora",
    "qlora",
    "custom model",
    "domain adaptation",

    # Multimodal & New Capabilities
    "multimodal ai",
    "vision language model",
    "vlm",
    "text to image",
    "image understanding",
    "video ai",
    "audio ai",

    # AI Safety & Alignment
    "ai safety",
    "alignment",
    "red teaming",
    "jailbreak",
    "guardrails",
    "responsible ai",

    # Coding & Development AI
    "ai coding",
    "code generation",
    "ai pair programming",
    "vibe coding",
    "ai ide",

    # AI Observability & Monitoring (core research focus)
    "ai observability",
    "llm observability",
    "llm monitoring",
    "ai monitoring",
    "model monitoring",
    "ai evaluation",
    "llm evaluation",
    "eval pipeline",
    "ai tracing",
    "reasoning traces",
    "ai sre",
    "ai site reliability",
    "ai ops",
    "aiops",
    "ml monitoring",
    "model drift",
    "data drift",
    "prompt injection detection",
    "ai governance",
    "ai reliability",

    # AI Security & Trust
    "ai security",
    "agent security",
    "agent permissions",
    "rbac agents",
    "ai trust",
    "ai compliance",
    "agent sandboxing",
    "prompt injection",
    "ai auditing",

    # Continual Learning & Self-Healing AI
    "continual learning",
    "self-healing ai",
    "corrective ai",
    "online learning",
    "catastrophic forgetting",
    "feedback loop",
    "human in the loop",
    "hitl",
]

# Secondary keywords (lower weight)
SECONDARY_KEYWORDS = [
    # Operations & Infrastructure
    "mlops",
    "ml infrastructure",
    "ai consulting",
    "solutions engineering",
    "technical account management",
    "ai case study",
    "production ml",
    "ai scaling",
    "customer onboarding",
    "inference infrastructure",
    "ai operations",

    # Models & Architectures
    "transformer",
    "attention mechanism",
    "context window",
    "token limit",
    "reasoning model",
    "chain of thought",
    "cot",
    "o1",
    "o3",

    # Efficiency & Optimization
    "quantization",
    "distillation",
    "pruning",
    "speculative decoding",
    "kv cache",
    "flash attention",

    # Data & Training
    "synthetic data",
    "data flywheel",
    "rlhf",
    "dpo",
    "preference learning",

    # Enterprise & Business
    "enterprise llm",
    "private ai",
    "on-premise ai",
    "data privacy",
    "ai governance",
    "ai compliance",

    # Open Source
    "open source llm",
    "open weights",
    "llama",
    "mistral",
    "qwen",
    "deepseek",

    # AI Observability & Evaluation (research focus)
    "llm-as-judge",
    "llm as judge",
    "evals",
    "benchmark",
    "regression testing",
    "a/b testing models",
    "trace",
    "span",
    "observability stack",
    "anomaly detection",
    "failure detection",
    "cost monitoring",
    "token usage",
    "latency monitoring",
    "error analysis",
    "model versioning",
    "model registry",
    "experiment tracking",
    "opentelemetry",
    "otel",
]

# =============================================================================
# COMPANY TIERS — weighted by signal value
# Tier A: rare mentions, high signal (vertical AI startups, FDE-heavy companies)
# Tier B: common mentions, medium signal (model labs, big platforms)
# Tier C: ubiquitous mentions, low signal (hyperscalers, chip makers)
# =============================================================================
COMPANY_TIER_A = [
    # Vertical / applied AI — a mention is informative
    "harvey", "sierra", "glean", "decagon", "cresta", "hebbia", "writer",
    "cognition", "devin", "factory.ai", "magic.dev", "lovable", "bolt.new",
    "world labs", "physical intelligence", "/dev/agents",
    # Coding agents at scale
    "cursor", "codeium", "windsurf", "replit", "tabnine", "sourcegraph",
    # AI observability / eval (research focus)
    "langsmith", "langfuse", "braintrust", "humanloop", "patronus ai",
    "log10", "helicone", "portkey", "openllmetry", "traceloop",
    "phoenix arize", "opik", "confident ai", "deepchecks", "arthur ai",
    "fiddler ai", "aporia", "superwise",
    # Defense / niche
    "anduril", "shield ai", "rebellion defense", "palantir",
    # AI security
    "lasso security", "robust intelligence", "protect ai",
    "hidden layer", "calypso ai",
]

COMPANY_TIER_B = [
    # Model labs
    "anthropic", "openai", "google deepmind", "deepmind", "mistral",
    "cohere", "ai21", "inflection", "xai", "deepseek",
    # Data + AI platforms
    "databricks", "snowflake", "motherduck", "duckdb", "clickhouse",
    "starburst", "trino", "confluent",
    # GPU / inference platforms
    "scale ai", "anyscale", "modal", "replicate", "together ai",
    "fireworks ai", "groq", "cerebras",
    # Vector DBs
    "pinecone", "weaviate", "qdrant", "chroma", "milvus",
    # Enterprise AI
    "c3 ai", "datarobot", "h2o.ai", "weights & biases", "wandb",
    "neptune", "mlflow", "perplexity", "jasper", "copy.ai", "notion ai",
    # Agent frameworks
    "adept", "langchain", "llamaindex", "autogpt", "crewai",
    # Observability infra (broader)
    "arize", "whylabs", "galileo ai",
]

COMPANY_TIER_C = [
    # Hyperscalers + chip makers — almost everyone mentions these
    "nvidia", "amd", "intel", "google tpu", "aws trainium", "inferentia",
    "aws bedrock", "azure openai", "google vertex", "vertex ai",
    "meta ai", "evidently ai", "opentelemetry",
]

# Flat companion list — preserved for backward compat (relevance scorer + report code).
# Companies to always flag - Updated for 2025
TARGET_COMPANIES = [
    # AI Labs & Model Providers
    "openai",
    "anthropic",
    "google deepmind",
    "deepmind",
    "meta ai",
    "mistral",
    "cohere",
    "ai21",
    "inflection",
    "xai",
    "deepseek",

    # AI Infrastructure & Platforms
    "databricks",
    "snowflake",
    "motherduck",
    "duckdb",
    "clickhouse",
    "starburst",
    "trino",
    "confluent",
    "scale ai",
    "anyscale",
    "modal",
    "replicate",
    "together ai",
    "fireworks ai",
    "groq",
    "cerebras",

    # Enterprise AI / Vertical AI
    "palantir",
    "c3 ai",
    "datarobot",
    "h2o.ai",
    "weights & biases",
    "wandb",
    "neptune",
    "mlflow",

    # AI-Native Startups
    "harvey",
    "glean",
    "cursor",
    "replit",
    "perplexity",
    "jasper",
    "copy.ai",
    "notion ai",
    "codeium",
    "tabnine",
    "sourcegraph",

    # AI Agents & Automation
    "adept",
    "cognition",
    "devin",
    "langchain",
    "llamaindex",
    "autogpt",
    "crewai",

    # Hardware & Chips
    "nvidia",
    "amd",
    "intel",
    "google tpu",
    "aws trainium",
    "inferentia",

    # Cloud AI Services
    "aws bedrock",
    "azure openai",
    "google vertex",
    "vertex ai",

    # Vector DBs & Search
    "pinecone",
    "weaviate",
    "qdrant",
    "chroma",
    "milvus",

    # Defense & Government AI
    "anduril",
    "shield ai",
    "rebellion defense",

    # AI Observability & Evaluation (research focus)
    "langsmith",
    "langfuse",
    "arize",
    "whylabs",
    "galileo ai",
    "braintrust",
    "humanloop",
    "patronus ai",
    "log10",
    "helicone",
    "portkey",
    "openllmetry",
    "traceloop",
    "phoenix arize",
    "opik",
    "confident ai",
    "deepchecks",
    "arthur ai",
    "fiddler ai",
    "aporia",
    "superwise",
    "evidently ai",
    "opentelemetry",

    # AI Security
    "lasso security",
    "robust intelligence",
    "protect ai",
    "hidden layer",
    "calypso ai",
]

# =============================================================================
# OPPORTUNITY SIGNAL KEYWORDS (flag business opportunity indicators)
# =============================================================================
# =============================================================================
# REGEX-BASED OPPORTUNITY SIGNALS
# These require a numeric amount or quantifier — much lower false-positive rate
# than substring matches like "raised $" (which matches "raised $5 to fix it").
# Each pattern carries a label used for downstream classification.
# =============================================================================
OPPORTUNITY_REGEX_PATTERNS = [
    # Funding rounds with amounts: "raised $50M", "$1.2 billion Series C"
    (r"\braised\s+\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\b", "funding_amount"),
    (r"\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\s+(?:series\s+[a-e]|seed|pre-seed)\b", "funding_amount"),
    (r"\bseries\s+[a-e]\b.{0,40}?\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\b", "funding_amount"),

    # Valuations with amounts
    (r"\bvalu(?:ed|ation)\s+(?:at\s+)?\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\b", "valuation"),
    (r"\$\s?\d+(?:\.\d+)?\s*(?:b|bn|billion)\s+valuation\b", "valuation"),

    # Customer counts: "200+ customers", "deployed at 50 enterprises"
    (r"\b\d{2,}\+?\s+(?:customers|enterprises|companies|fortune\s+\d+\s+companies)\b", "customer_count"),
    (r"\b(?:deployed|adopted|used|implemented)\s+(?:by|at)\s+\d{2,}\+?\s+(?:companies|customers|enterprises)\b", "customer_count"),

    # Revenue / ARR
    (r"\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\s+(?:in\s+)?(?:arr|annual\s+recurring|revenue)\b", "revenue"),
    (r"\b(?:arr|annual\s+recurring\s+revenue)\s+of\s+\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\b", "revenue"),

    # Quantified business impact
    (r"\b(?:reduced|cut|saved)\s+(?:costs?|expenses?)\s+by\s+\d+\s*%", "cost_savings"),
    (r"\bsaved\s+\d+\+?\s+(?:hours|days|weeks|engineers)\b", "time_savings"),
    (r"\b\d+x\s+(?:faster|productivity|throughput|efficiency)\b", "productivity_gain"),

    # Acquisitions with amounts
    (r"\bacquir(?:ed|es|ing)\b.{0,40}?\$\s?\d+(?:\.\d+)?\s*(?:m|mm|b|bn|million|billion)\b", "acquisition"),

    # Deployment-stage transitions (non-numeric but specific)
    (r"\b(?:general\s+availability|generally\s+available|now\s+ga)\b", "deployment_milestone"),
    (r"\bmoving\s+(?:from\s+)?pilot\s+to\s+production\b", "deployment_milestone"),
    (r"\brolled\s+out\s+to\s+\d+\+?\s+(?:teams|users|employees|customers)\b", "deployment_milestone"),
]

OPPORTUNITY_KEYWORDS = [
    # Deployment maturity signals
    "pilot program", "general availability", "rolled out to", "production deployment",
    "now available", "launched", "went live", "ga release", "public preview",
    "expanding to", "scaling to",
    # Business impact signals
    "reduced costs by", "saved hours", "roi of", "increased revenue",
    "cost savings", "productivity gains", "time savings", "efficiency gains",
    "million in revenue", "billion valuation",
    # Funding & growth signals
    "raised $", "series a", "series b", "series c", "series d",
    "seed round", "funding round", "ipo", "acquisition", "acquires",
    "strategic investment", "joint venture", "strategic partnership",
    # Competitive choice signals
    "chose over", "switched from", "replaced", "migrated to", "compared to",
    "alternative to", "better than", "instead of",
    # Hiring & team signals
    "hiring for", "growing the team", "looking for engineers", "new roles",
    "head of ai", "vp of engineering", "founding engineer",
    # Customer success signals
    "case study", "customer story", "success story", "testimonial",
    "deployed by", "used by", "adopted by", "implemented at",
    # Observability & monitoring signals
    "observability platform", "monitoring solution", "evaluation framework",
    "tracing tool", "llm evaluation", "model monitoring", "drift detection",
    "opentelemetry for ai", "ai sre", "ai reliability",
]

# =============================================================================
# INDUSTRY VERTICALS (classify articles by sector)
# =============================================================================
INDUSTRY_VERTICALS = {
    "Financial Services": ["fintech", "banking", "insurance", "trading", "payments", "finance", "hedge fund", "wealth management"],
    "Healthcare": ["healthcare", "medical", "pharma", "biotech", "clinical", "patient", "drug discovery", "diagnostics"],
    "Legal": ["legal", "law firm", "contract", "compliance", "litigation", "regulatory", "attorney"],
    "Manufacturing": ["manufacturing", "supply chain", "logistics", "warehouse", "industrial", "factory", "procurement"],
    "Retail & E-commerce": ["retail", "ecommerce", "e-commerce", "shopping", "marketplace", "consumer"],
    "Education": ["education", "edtech", "university", "school", "learning", "tutoring"],
    "Government & Defense": ["government", "defense", "military", "federal", "public sector", "intelligence"],
    "Media & Entertainment": ["media", "entertainment", "content creation", "publishing", "streaming", "advertising"],
    "Professional Services": ["consulting", "advisory", "professional services", "accounting", "audit"],
    "Technology & SaaS": ["saas", "software", "platform", "developer tools", "devtools", "cloud services"],
}

# Exclusion keywords (reduce noise)
EXCLUSION_KEYWORDS = [
    "crypto",
    "blockchain",
    "web3",
    "nft",
    "defi",
    "stock prediction",
    "trading bot",
    "meme coin",
    "token launch",
    "forex",
    "betting",
    "casino",
]

# Reddit subreddits to monitor - FOCUSED on AI Deployment, FDE, Implementation
REDDIT_SUBREDDITS = [
    # ========== HIGHEST PRIORITY: AI Deployment & Operations ==========
    "mlops",                    # MLOps - deployment, serving, monitoring
    "dataengineering",          # Data pipelines and infrastructure
    "devops",                   # DevOps practices for AI systems
    "kubernetes",               # K8s for ML workloads
    "aws",                      # Cloud AI deployment
    "googlecloud",              # GCP AI services
    "azure",                    # Azure AI deployment

    # ========== HIGH PRIORITY: Enterprise & Implementation ==========
    "ExperiencedDevs",          # Senior engineers - real deployment stories
    "cscareerquestions",        # Career discussions incl. FDE roles
    "consulting",               # Implementation consulting
    "startups",                 # Startup AI deployment challenges
    "SaaS",                     # SaaS AI product deployment
    "ProductManagement",        # PM perspective on AI rollouts
    "enterpriseIT",             # Enterprise IT adoption

    # ========== HIGH PRIORITY: LLM Production & Deployment ==========
    "LocalLLaMA",               # Self-hosted LLM deployment
    "LangChain",                # LLM app development & deployment
    "ClaudeAI",                 # Claude enterprise use cases
    "OpenAI",                   # OpenAI API production usage

    # ========== HIGH PRIORITY: AI Engineering ==========
    "MachineLearning",          # ML engineering practices
    "datascience",              # Data science in production
    "deeplearning",             # DL deployment considerations
    "LanguageTechnology",       # NLP deployment

    # ========== AI Coding & Developer Productivity ==========
    "cursor",                   # Cursor AI deployment in teams
    "CursorAI",                 # Cursor workflows
    "copilot",                  # Copilot enterprise rollout
    "programming",              # Dev AI adoption

    # ========== AI Agents & Automation ==========
    "AutoGPT",                  # Autonomous agents deployment
    "LangChain",                # Agent frameworks

    # ========== AI Observability & SRE (research focus) ==========
    "sre",                      # Site Reliability Engineering
    "observability",            # Observability practices
    "monitoring",               # Monitoring tools and practices

    # ========== LOWER PRIORITY: General AI (for context) ==========
    "artificial",               # General AI context
    "ArtificialIntelligence",   # AI industry news
]

# RSS feeds to monitor.
# All URLs verified working as of 2026-04-25. Dropped feeds without public RSS:
# Anthropic news, a16z, First Round Review, Shopify Eng, Notion, Uber Eng,
# Google SRE, WhyLabs (shutting down), Evidently AI, Starburst.
RSS_FEEDS = {
    # News & Tech Publications
    "techcrunch_ai": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "venturebeat_ai": "https://venturebeat.com/category/ai/feed/",
    "mit_tech_review": "https://www.technologyreview.com/feed/",
    "the_verge_ai": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
    "ars_technica": "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "wired_ai": "https://www.wired.com/feed/tag/ai/latest/rss",

    # VC & Startup Blogs
    "sequoia": "https://www.sequoiacap.com/feed/",

    # AI Lab Blogs
    "deepmind_blog": "https://deepmind.google/blog/rss.xml",
    "openai_news": "https://openai.com/news/rss.xml",

    # Company Engineering Blogs
    "huggingface_blog": "https://huggingface.co/blog/feed.xml",
    "langchain_blog": "https://www.langchain.com/blog/rss.xml",

    # AI Research
    "arxiv_cs_ai": "https://rss.arxiv.org/rss/cs.AI",
    "arxiv_cs_cl": "https://rss.arxiv.org/rss/cs.CL",

    # Additional AI News Sources
    "import_ai": "https://jack-clark.net/feed/",

    # Engineering Blogs (deployment case studies)
    "stripe_blog": "https://stripe.com/blog/feed.rss",
    "netflix_tech": "https://medium.com/feed/netflix-techblog",
    "airbnb_eng": "https://medium.com/feed/airbnb-engineering",

    # AI Industry Analysis
    # (The Information dropped — feed is 403 even with browser UA)
    "semianalysis": "https://semianalysis.com/feed",
    "stratechery": "https://stratechery.com/feed/",

    # AI Observability & Monitoring (research focus)
    # (Arize dropped — Cloudflare 403s any non-browser request)
    "langchain_changelog": "https://changelog.langchain.com/feed",
    "helicone_blog": "https://blog.helicone.ai/feed",

    # Coding/agent product cadence
    "cursor_changelog": "https://www.cursor.com/changelog/rss.xml",
    "vercel_atom": "https://vercel.com/atom",

    # Hyperscaler AI announcements (GA / customer wins)
    "aws_whatsnew": "https://aws.amazon.com/about-aws/whats-new/recent/feed/",
    "gcp_ai_blog": "https://cloudblog.withgoogle.com/products/ai-machine-learning/rss/",

    # Curated AI deal-flow / practitioner aggregators
    "latent_space": "https://www.latent.space/feed",
    "tldr_ai": "https://tldr.tech/api/rss/ai",
    "bens_bites": "https://bensbites.com/feed.xml",
    "crunchbase_ai": "https://news.crunchbase.com/sections/ai/feed/",

    # Data + AI platforms (Snowflake, Databricks, and lakehouse/warehouse competitors)
    # (MotherDuck and ClickHouse dropped — neither publishes a working RSS feed)
    "snowflake_blog": "https://www.snowflake.com/feed/",
    "databricks_blog": "https://www.databricks.com/blog/feed.xml",
    "confluent_blog": "https://www.confluent.io/feed/",
}

# Hacker News settings
HN_API_BASE = "https://hacker-news.firebaseio.com/v0"
HN_ITEMS_PER_FETCH = 100  # Number of stories to check per run

# Claude API settings
MAX_TOKENS_SUMMARY = 500
MAX_TOKENS_ANALYSIS = 2000

# Report settings
WEEKLY_REPORT_DAY = "monday"  # Day to generate weekly reports
DAILY_REPORT_TIME = "09:00"  # Time to generate daily reports

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# =============================================================================
# TREND CATEGORIES FOR UI
# =============================================================================
TREND_CATEGORIES = {
    "AI Agents & Autonomy": [
        "ai agents", "agentic ai", "autonomous agents", "multi-agent",
        "agent framework", "computer use", "browser automation"
    ],
    "LLM Infrastructure": [
        "inference", "model serving", "llmops", "gpu", "optimization",
        "scaling", "infrastructure"
    ],
    "RAG & Knowledge": [
        "rag", "retrieval", "vector database", "embeddings",
        "knowledge graph", "semantic search"
    ],
    "Fine-tuning & Customization": [
        "fine-tuning", "lora", "qlora", "custom model", "domain adaptation"
    ],
    "AI Coding Tools": [
        "cursor", "copilot", "code generation", "ai coding", "replit",
        "codeium", "tabnine"
    ],
    "Enterprise AI": [
        "enterprise", "deployment", "roi", "adoption", "compliance",
        "governance", "private ai"
    ],
    "AI Safety": [
        "safety", "alignment", "guardrails", "red teaming", "responsible ai"
    ],
    "Open Source AI": [
        "llama", "mistral", "open source", "open weights", "deepseek", "qwen"
    ],
    "AI Observability & Monitoring": [
        "observability", "monitoring", "tracing", "evaluation", "evals",
        "llm-as-judge", "drift", "anomaly detection", "langfuse", "langsmith",
        "arize", "helicone", "braintrust", "model monitoring"
    ],
    "AI Security & Trust": [
        "ai security", "prompt injection", "guardrails", "rbac", "sandboxing",
        "ai trust", "ai compliance", "ai governance", "agent permissions"
    ],
    "AI SRE & Reliability": [
        "ai sre", "reliability", "self-healing", "corrective", "failure detection",
        "error analysis", "incident", "on-call", "runbook", "production issues"
    ],
}
