# 📈 InvestMatch AI — Full Roadmap

## 🎯 Project Goal

Build an **ML-powered investment recommender** that:

- Learns user preferences
- Matches users to stocks/ETFs
- Uses real performance data
- Shows charts + explanations
- Improves using feedback over time

> ⚠️ This is NOT a stock prediction app.  
> It is a **personalized recommendation system**.

---

# 🟦 PHASE 0: Foundations

## Goal
Understand the system before coding

## Tasks
- [ X] Understand recommender systems vs prediction models
- [ X] Understand ML pipeline: input → model → output
- [X ] Understand user vector
- [ X] Understand investment vector
- [ X] Understand match score
- [X ] Understand feedback loops
- [ ] Add disclaimer: "Educational only, not financial advice"

---

# 🟩 PHASE 1: User Onboarding

## Goal
Collect structured user preference data

## Tasks
- [ ] Ask initial investment amount
- [ ] Ask monthly contribution
- [ ] Ask risk tolerance (low, medium, high)
- [ ] Ask time horizon (short, medium, long)
- [ ] Ask goal (retirement, growth, income, learning, stock picking)
- [ ] Ask experience level
- [ ] Ask preferred sectors (tech, AI, healthcare, finance, etc.)
- [ ] Ask growth vs dividend preference
- [ ] Ask values preferences (ESG, climate, etc.)

## Learn
- [ ] Form design
- [ ] User profiling
- [ ] Mapping inputs → ML features

---

# 🟨 PHASE 2: Database + UI

## Goal
Store all system data

## Tasks
- [ ] Create project structure
- [ ] Set up SQLite database

### Tables
- [ ] user_profiles
- [ ] user_preferences
- [ ] investments
- [ ] stock_data
- [ ] feedback
- [ ] user_watchlist
- [ ] user_portfolio

## UI
- [ ] Build Streamlit interface

## Learn
- [ ] CRUD operations
- [ ] DB schema design
- [ ] UI → DB flow

---

# 🟧 PHASE 3: Investment Data Layer

## Goal
Use real stock/ETF data

## Tasks
- [ ] Create CSV with 30–50 stocks/ETFs
- [ ] Add ticker, name, sector, asset_type
- [ ] Add risk level
- [ ] Add dividend yield
- [ ] Add ETF expense ratio

## API Integration
- [ ] Integrate yfinance
- [ ] Fetch 1-year price history
- [ ] Fetch 5-year price history
- [ ] Calculate 1Y return
- [ ] Calculate volatility
- [ ] Store processed data in DB

## Learn
- [ ] Financial metrics
- [ ] API usage
- [ ] Data cleaning

---

# 🟨 PHASE 4: Rule-Based Logic (Fallback)

## Goal
Provide safe baseline recommendations

## Tasks
- [ ] Low risk → ETF-heavy strategy
- [ ] Long-term → diversified growth strategy
- [ ] High risk → stock-heavy strategy
- [ ] Dividend → income-focused strategy
- [ ] Values-based → ESG filtering
- [ ] Use rules when ML confidence is low

---

# 🟧 PHASE 5: Feature Engineering

## Goal
Convert data into ML-ready format

## User Features
- [ ] Encode risk tolerance
- [ ] Encode goal
- [ ] Encode time horizon
- [ ] Normalize investment amount
- [ ] One-hot encode sectors
- [ ] Encode values preferences
- [ ] Encode growth vs dividend

## Investment Features
- [ ] Encode sector
- [ ] Encode asset_type
- [ ] Include volatility
- [ ] Include 1Y return
- [ ] Include 5Y return
- [ ] Include dividend yield
- [ ] Include expense ratio

## Final Input
[user_vector + investment_vector] → model → match_score

---

# 🟥 PHASE 6: PyTorch Basics

## Goal
Learn ML fundamentals

## Tasks
- [ ] Create tensors
- [ ] Build simple model (nn.Linear)
- [ ] Forward pass
- [ ] Compute loss
- [ ] Backward pass
- [ ] Use Adam optimizer
- [ ] Save/load model

---

# 🟪 PHASE 7: ML Match Model

## Goal
Build recommender model

## Tasks
- [ ] Create InvestmentRecommender class
- [ ] Input layer
- [ ] Hidden layer (ReLU)
- [ ] Output layer (Sigmoid)
- [ ] Output match score (0–1)
- [ ] Rank investments by score

---

# 🟫 PHASE 8: Feedback Training

## Goal
Personalize recommendations

## Tasks
- [ ] Add 👍 (like)
- [ ] Add 👎 (dislike)
- [ ] Add "save to watchlist"
- [ ] Add "add to portfolio"
- [ ] Store feedback
- [ ] Convert feedback → labels (1/0)
- [ ] Retrain model with feedback

---

# ⚫ PHASE 9: Recommendation Engine

## Goal
Generate ranked results

## Tasks
- [ ] Load user profile
- [ ] Load stock dataset
- [ ] Generate feature vectors
- [ ] Run ML model
- [ ] Score each investment
- [ ] Sort results
- [ ] Return top recommendations
- [ ] Attach performance + risk data

---

# ⚪ PHASE 10: Recommendation Cards + Charts

## Goal
Make recommendations understandable

## Each Card Includes
- [ ] Ticker
- [ ] Name
- [ ] Match score
- [ ] Sector
- [ ] Risk level
- [ ] 1-year return
- [ ] Volatility
- [ ] 1-year price chart
- [ ] Explanation: why it matches
- [ ] Risk warning
- [ ] Suggested role (core/growth/dividend)

---

# 🟤 PHASE 11: Dashboard

## Goal
Track investments

## Tasks
- [ ] Watchlist view
- [ ] Portfolio view
- [ ] Saved recommendations
- [ ] Portfolio growth chart
- [ ] Sector allocation chart
- [ ] Risk breakdown chart
- [ ] Notes for each investment

---

# 🟣 PHASE 12: GPT Explanation Layer

## Goal
Generate human-readable insights

## Tasks
- [ ] Generate explanation: "why this matches you"
- [ ] Explain company
- [ ] Highlight risks
- [ ] Summarize performance
- [ ] Add citations
- [ ] Include disclaimer

---

# 🔄 FINAL FLOW


---

# 🚀 MVP CHECKLIST

Before adding advanced features:

- [ ] 30+ stocks loaded
- [ ] Working user survey
- [ ] Feature vectors working
- [ ] Basic ML model running
- [ ] Top 5 recommendations displayed
- [ ] At least 1 chart working

---

# 🔥 FUTURE UPGRADES

- [ ] Real-time stock data
- [ ] Portfolio optimization
- [ ] Multi-user accounts
- [ ] News + sentiment analysis
- [ ] React frontend + FastAPI backend
- [ ] Advanced ML models