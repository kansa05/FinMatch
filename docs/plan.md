# 📈 InvestMatch AI — Updated Checklist Roadmap + File Map

## 🎯 Project Goal
Build a personalized investment recommendation system using:
- User input
- Rule-based logic
- Financial analytics (returns, risk, drawdowns)
- Classical ML first (scikit-learn), then optional deep learning
- Feedback loops and retraining
- Optional GPT explanations

## Architecture layers (keep responsibilities split)

| Layer | Job |
|--------|-----|
| Streamlit / UI | Display inputs, results, charts |
| Rules | Decide pathway and baseline picks |
| API layer | Fetch prices, fundamentals, history |
| Analytics (`metrics.py`) | Compute returns, volatility, Sharpe, drawdowns, risk scores |
| Storage | Persist profiles, training rows, feedback |
| ML | Learn patterns from vectors + labels |

---

# 📁 PROJECT STRUCTURE

FINMATCH/
│
├── app.py
│   - Main Streamlit app
│   - Controls navigation: home → survey → results
│   - Calls cleaning, rules, recommendations, and saving functions
│
├── data/
│   ├── investments.csv
│   │   - Stock/ETF dataset
│   │   - Used for investment features later
│   │
│   ├── user_profiles.jsonl
│   │   - Raw survey answers
│   │   - Saved before cleaning
│   │
│   └── training_data.jsonl
│       - Cleaned profile + pathway + recommendations
│       - Used later for ML training
│
├── docs/
│   ├── plan.md
│   │   - Main roadmap/checklist
│   │
│   └── learningML.md
│       - Notes while learning ML concepts
│
├── models/
│   ├── investmatch_model.joblib (or .pkl)
│   │   - Saved scikit-learn model (Phase 5)
│   └── investmatch_nn.pt (optional, later)
│       - PyTorch checkpoint if you add deep learning (Phase 9)
│
└── src/
    └── main/
        ├── survey.py
        │   - Survey/helper UI functions
        │
        ├── model.py
        │   - Optional: sklearn wrapper or PyTorch module (later)
        │
        ├── train.py
        │   - Training script (sklearn first; PyTorch experiments optional)
        │
        ├── api/
        │   └── investment_api.py
        │       - Fetch market data (e.g. yfinance); Phase 3
        │
        └── logic/
            ├── schema.py
            │   - clean_profile()
            │   - Turns raw survey answers into clean labels
            │
            ├── rules.py
            │   - get_pathway()
            │   - Chooses ETF-only / ETF-heavy / balanced / growth
            │
            ├── recommendations.py
            │   - get_recommendations()
            │   - Maps pathway to actual investment suggestions
            │
            ├── metrics.py
            │   - Annual return, volatility, moving averages, max drawdown, Sharpe, risk score
            │   - Phase 3.5: analytics “brains” for features + UI later
            │
            └── save_data.py
                - save_training_example()
                - Saves cleaned training examples to JSONL

---

# 🟦 PHASE 0: Foundations ✅

## Goal
Understand system components.

## Files Used
- docs/learningML.md
- docs/plan.md

## Checklist
- [x] Understand ML pipeline: input → model → output
- [x] Understand user vector
- [x] Understand investment vector
- [x] Understand match score
- [x] Understand rules vs ML
- [x] Understand feedback loops
- [x] Add disclaimer to app.py

---

# 🟩 PHASE 1: User Onboarding Streamlit ✅

## Goal
Collect structured user data.

## Files Used
- app.py
- src/main/survey.py optional later
- data/user_profiles.jsonl

## Checklist
- [x] Build Streamlit survey UI
- [x] Ask investment amount
- [x] Ask monthly contribution
- [x] Ask goals
- [x] Ask time horizon
- [x] Ask risk preference
- [x] Ask experience level
- [x] Ask preferred sectors
- [x] Ask investment types
- [x] Ask values/preferences
- [x] Store responses in user_profile
- [x] Add navigation: home → survey → results
- [x] Save raw answers to data/user_profiles.jsonl

---

# 🟦 PHASE 1.5: Schema + Rule Engine ✅

## Goal
Turn user input into structured data and generate first recommendations.

---

## Step 1: Clean Schema

## File Used
- src/main/logic/schema.py

## Function
- clean_profile(user_profile)

## Checklist
- [X ] Create clean_profile from raw survey data
- [ X] Map risk answers → low / medium / high
- [X ] Map time horizon → short / medium / long
- [X ] Normalize experience levels
- [X ] Clean sector lists
- [X ] Clean values lists
- [ X] Return one clean dictionary

---

## Step 2: Rule-Based Pathways

## File Used
- src/main/logic/rules.py

## Function
- get_pathway(cleaned_profile)

## Checklist
- [ X] Create ETF-only rule: low amount + beginner
- [ X] Create ETF-heavy rule: low risk
- [X ] Create balanced portfolio rule: medium risk
- [ X] Create growth portfolio rule: high risk + long horizon
- [ X] Create values-based filtering rule
- [ X] Return pathway name

---

## Step 3: Generate Recommendations

## File Used
- src/main/logic/recommendations.py

## Function
- get_recommendations(pathway, cleaned_profile)

## Checklist
- [ X] Map pathways → actual tickers
- [X ] Return 2–5 investment recommendations
- [X ] Include ticker
- [ X] Include investment name
- [ X] Include asset type
- [ X] Include risk level
- [ X ] Include reasoning string

---

## Step 4: Save Training Data

## File Used
- src/main/logic/save_data.py
- data/training_data.jsonl

## Function
- save_training_example(cleaned_profile, pathway, recommendations)

## Checklist
- [x] Save cleaned_profile
- [x] Save pathway
- [x] Save recommended_investments
- [x] Save label_source as rule_based
- [x] Save feedback as null
- [x] Append to data/training_data.jsonl

---

## Step 5: Connect Phase 1.5 to Streamlit

## File Used
- app.py

## Checklist
- [x] Import clean_profile from schema.py
- [x] Import get_pathway from rules.py
- [x] Import get_recommendations from recommendations.py
- [x] Import save_training_example from save_data.py
- [x] On submit, create raw user_profile
- [x] Run cleaned_profile = clean_profile(user_profile)
- [x] Run pathway = get_pathway(cleaned_profile)
- [x] Run recommendations = get_recommendations(pathway, cleaned_profile)
- [x] Run save_training_example(cleaned_profile, pathway, recommendations)
- [x] Store results in st.session_state
- [x] Display recommendations on results page

---

# 🟨 PHASE 2: Data Storage

## Goal
Organize and persist data.

## Files Used
- data/user_profiles.jsonl
- data/training_data.jsonl
- src/main/logic/save_data.py

## Checklist
- [x] Save raw JSON data
- [ ] Structure JSON format consistently
- [ ] Save cleaned training data separately
- [ ] Handle multiple users
- [ ] Add timestamps
- [ ] Optional: move to SQLite later

---

# 🟧 PHASE 3: Investment Data Layer

## Goal
Fetch live investment data from APIs.

## Files Used
- data/investments.csv
- src/main/logic/recommendations.py
- src/main/api/investment_api.py

## Checklist
- [ ] Install yfinance
- [ ] Fetch stock data
- [ ] Fetch ETF data
- [ ] Pull dividend yield
- [ ] Pull market cap
- [ ] Pull historical prices
- [ ] Handle invalid tickers
- [ ] Return structured dictionaries

- [ ] Create CSV with 30–100 stocks/ETFs
- [ ] Add ticker
- [ ] Add company/fund name
- [ ] Add sector
- [ ] Add asset type
- [ ] Add risk level
- [ ] Add volatility
- [ ] Add returns
- [ ] Add dividend yield


---

# 🟦 PHASE 3.5: Financial Analytics Engine

## Goal
Calculate investment metrics from price history (and related inputs). This becomes the quantitative “brains” behind features, ranking, and UI charts later.

## Files Used
- src/main/logic/metrics.py
- (Inputs) price series from Phase 3 API or CSV-derived history

## Checklist
- [ ] Calculate annual return
- [ ] Calculate volatility
- [ ] Calculate moving averages
- [ ] Calculate max drawdown
- [ ] Calculate Sharpe ratio
- [ ] Create risk scoring formula (document assumptions, e.g. risk-free rate)

---

# 🟨 PHASE 4: Feature Engineering

## Goal
Convert data into numerical vectors.

## Files Used
- src/main/features.py
- data/investments.csv
- data/training_data.jsonl
- src/main/logic/metrics.py (reuse analytics outputs as investment features where applicable)

## User Features
- [ ] Encode risk level
- [ ] Encode goal
- [ ] Encode time horizon
- [ ] Normalize investment amount
- [ ] One-hot encode sectors
- [ ] Encode values preferences

## Investment Features
- [ ] Encode sector
- [ ] Encode asset type
- [ ] Add volatility score
- [ ] Add return metrics
- [ ] Add dividend yield

## Final Input
- [ ] Combine user_vector + investment_vector
- [ ] Create X training matrix
- [ ] Create y label vector

---

# 🟥 PHASE 5: Classical ML Recommender (scikit-learn first)

## Goal
Learn recommendation patterns with tabular models before deep learning. Start simple, interpretable, and fast to iterate.

## Why not PyTorch first
Neural nets are powerful but easy to overfit on small JSONL datasets. Logistic regression / random forest / gradient boosting match typical recommender-system bootstraps when features are structured.

## Files Used
- src/main/train.py
- src/main/model.py (optional: thin wrappers around sklearn pipelines)
- src/main/features.py
- data/training_data.jsonl
- models/investmatch_model.joblib (or .pkl)

## Checklist
- [ ] Add scikit-learn to project dependencies
- [ ] Define `X` from user + investment feature vectors (Phase 4)
- [ ] Define `y` (e.g. match / click / feedback label when available)
- [ ] Start with **logistic regression** baseline (calibrated probabilities if needed)
- [ ] Try **random forest** or **gradient boosting** (e.g. **XGBoost** / HistGradientBoosting later)
- [ ] Cross-validate; track metrics (AUC, log loss, or ranking metrics you choose)
- [ ] Train on collected data (rule-based labels first; improve with Phase 7 feedback)
- [ ] Save model with `joblib.dump` (or pickle) to `models/investmatch_model.joblib`

---

# 🟪 PHASE 6: Recommendation Engine

## Goal
Rank investments.

## Files Used
- src/main/recommender.py
- src/main/features.py
- src/main/train.py (load trained sklearn model)
- data/investments.csv
- models/investmatch_model.joblib

## Checklist
- [ ] Load user profile
- [ ] Load investment dataset
- [ ] Convert user profile to vector
- [ ] Convert each investment to vector
- [ ] Combine user_vector + investment_vector
- [ ] Run sklearn model `predict` / `predict_proba` (or decision_function)
- [ ] Score each investment
- [ ] Sort results
- [ ] Return top 5

---

# 🟫 PHASE 7: Feedback Loop

## Goal
Improve recommendations.

## Files Used
- app.py
- data/training_data.jsonl
- data/feedback.jsonl
- src/main/logic/save_data.py

## Checklist
- [ ] Add thumbs up/down buttons
- [ ] Add save/watchlist button
- [ ] Store feedback
- [ ] Convert feedback to labels: 1 or 0
- [ ] Add feedback examples to training data
- [ ] Retrain model

---

# ⚪ PHASE 8: UI + Output

## Goal
Make results usable.

## Files Used
- app.py
- src/main/survey.py optional
- src/main/recommender.py
- src/main/logic/metrics.py (charts: returns, drawdowns, moving averages)

## Checklist
- [ ] Show recommendations
- [ ] Show ticker + name
- [ ] Show risk level
- [ ] Show match score
- [ ] Show reasoning
- [ ] Add charts for price history
- [ ] Add warnings
- [ ] Add educational explanation

---

# 🟥 PHASE 9: Deep Learning Experiments (Optional, later)

## Goal
After classical ML and enough data, experiment with neural networks if they add value (e.g. embeddings, deeper interaction models).

## Files Used
- src/main/model.py (PyTorch `nn.Module` or similar)
- src/main/train_dl.py (optional separate script)
- models/investmatch_nn.pt

## Checklist
- [ ] Add PyTorch only when baseline sklearn models are stable
- [ ] Build a small network appropriate to data size (avoid huge MLPs on tiny JSONL)
- [ ] Reuse Phase 4 feature pipeline where possible
- [ ] Compare fairly against sklearn baseline (same train/val split)
- [ ] Save checkpoint to `models/investmatch_nn.pt`

---

# 🟣 PHASE 10: GPT Layer Optional

## Goal
Explain recommendations.

## Files Used
- src/main/gpt_explainer.py
- app.py

## Checklist
- [ ] Generate explanation text
- [ ] Explain why picks match user
- [ ] Summarize risks
- [ ] Keep educational tone
- [ ] Add strong disclaimer

---

# 🔄 FINAL SYSTEM FLOW

Survey  
→ Raw user_profile  
→ clean_profile()  
→ get_pathway()  
→ get_recommendations()  
→ save_training_example()  
→ APIs (prices, fundamentals)  
→ Analytics (metrics.py)  
→ Feature Engineering  
→ Classical ML (sklearn)  
→ Ranking  
→ UI  
→ Feedback  
→ Retrain  
→ (Optional) Deep learning experiments  

---

# 🚀 CURRENT STATUS

- Phase 0 ✅
- Phase 1 ✅
- Phase 1.5 ✅ (Streamlit wired; rules + JSONL pipeline live)
- Next focus: Phase 2–3 (storage hardening + investment data / API), then Phase 3.5 metrics

---

# 🎯 IMMEDIATE NEXT STEPS

## Suggested build order from here:
1. Phase 2: tighten JSONL schema, timestamps, optional user id
2. Phase 3: `investments.csv` + `src/main/api/investment_api.py` (yfinance)
3. Phase 3.5: `src/main/logic/metrics.py` (returns, vol, MA, drawdown, Sharpe, risk score)
4. Phase 4: `src/main/features.py` — vectors for user + investment (+ metrics)
5. Phase 5: sklearn `train.py` — logistic regression → forest / boosting → save `joblib`

---

# 🧠 Current Coding Task

## File (pick one track)
- `src/main/api/investment_api.py` (Phase 3) **or**
- `src/main/logic/metrics.py` (Phase 3.5)

## Purpose
Grow the data + analytics layer so Phase 4–5 have real numeric features, not only rule labels.