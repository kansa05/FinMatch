# 📈 InvestMatch AI — Updated Checklist Roadmap + File Map

## 🎯 Project Goal
Build a personalized investment recommendation system using:
- User input
- Rule-based logic
- Machine learning
- Feedback loops
- Optional GPT explanations

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
│   └── investmatch_model.pt
│       - Saved PyTorch model later
│
└── src/
    └── main/
        ├── survey.py
        │   - Survey/helper UI functions
        │
        ├── model.py
        │   - PyTorch model class later
        │
        ├── train.py
        │   - Training script later
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
- [ ] Add disclaimer to app.py

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

# 🟦 PHASE 1.5: Schema + Rule Engine 🔄 CURRENT

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
- [ ] Create ETF-only rule: low amount + beginner
- [ ] Create ETF-heavy rule: low risk
- [ ] Create balanced portfolio rule: medium risk
- [ ] Create growth portfolio rule: high risk + long horizon
- [ ] Create values-based filtering rule
- [ ] Return pathway name

---

## Step 3: Generate Recommendations

## File Used
- src/main/logic/recommendations.py

## Function
- get_recommendations(pathway, cleaned_profile)

## Checklist
- [ ] Map pathways → actual tickers
- [ ] Return 2–5 investment recommendations
- [ ] Include ticker
- [ ] Include investment name
- [ ] Include asset type
- [ ] Include risk level
- [ ] Include reasoning string

---

## Step 4: Save Training Data

## File Used
- src/main/logic/save_data.py
- data/training_data.jsonl

## Function
- save_training_example(cleaned_profile, pathway, recommendations)

## Checklist
- [ ] Save cleaned_profile
- [ ] Save pathway
- [ ] Save recommended_investments
- [ ] Save label_source as rule_based
- [ ] Save feedback as null
- [ ] Append to data/training_data.jsonl

---

## Step 5: Connect Phase 1.5 to Streamlit

## File Used
- app.py

## Checklist
- [ ] Import clean_profile from schema.py
- [ ] Import get_pathway from rules.py
- [ ] Import get_recommendations from recommendations.py
- [ ] Import save_training_example from save_data.py
- [ ] On submit, create raw user_profile
- [ ] Run cleaned_profile = clean_profile(user_profile)
- [ ] Run pathway = get_pathway(cleaned_profile)
- [ ] Run recommendations = get_recommendations(pathway, cleaned_profile)
- [ ] Run save_training_example(cleaned_profile, pathway, recommendations)
- [ ] Store results in st.session_state
- [ ] Display recommendations on results page

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
Create investment dataset.

## Files Used
- data/investments.csv
- src/main/logic/recommendations.py

## Checklist
- [ ] Create CSV with 30–100 stocks/ETFs
- [ ] Add ticker
- [ ] Add company/fund name
- [ ] Add sector
- [ ] Add asset type
- [ ] Add risk level
- [ ] Add volatility
- [ ] Add returns
- [ ] Add dividend yield
- [ ] Optional: add ESG data
- [ ] Optional: connect yfinance API later

---

# 🟨 PHASE 4: Feature Engineering

## Goal
Convert data into numerical vectors.

## Files Used
- src/main/features.py
- data/investments.csv
- data/training_data.jsonl

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

# 🟥 PHASE 5: ML Model PyTorch

## Goal
Learn recommendation patterns.

## Files Used
- src/main/model.py
- src/main/train.py
- models/investmatch_model.pt

## Checklist
- [ ] Build simple neural network
- [ ] Create input layer
- [ ] Create hidden layer with ReLU
- [ ] Create output layer with Sigmoid
- [ ] Output match score between 0 and 1
- [ ] Choose loss function
- [ ] Set learning rate
- [ ] Train on collected data
- [ ] Save model to models/investmatch_model.pt

---

# 🟪 PHASE 6: Recommendation Engine

## Goal
Rank investments.

## Files Used
- src/main/recommender.py
- src/main/features.py
- src/main/model.py
- data/investments.csv
- models/investmatch_model.pt

## Checklist
- [ ] Load user profile
- [ ] Load investment dataset
- [ ] Convert user profile to vector
- [ ] Convert each investment to vector
- [ ] Combine user_vector + investment_vector
- [ ] Run model inference
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

# 🟣 PHASE 9: GPT Layer Optional

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
→ Feature Engineering  
→ ML Model  
→ Ranking  
→ UI  
→ Feedback  
→ Improvement  

---

# 🚀 CURRENT STATUS

- Phase 0 ✅
- Phase 1 ✅
- Phase 1.5 🔄 YOU ARE HERE

---

# 🎯 IMMEDIATE NEXT STEPS

## Create these files first:
- [ ] src/main/logic/schema.py
- [ ] src/main/logic/rules.py
- [ ] src/main/logic/recommendations.py
- [ ] src/main/logic/save_data.py

## Build in this order:
1. schema.py → clean_profile()
2. rules.py → get_pathway()
3. recommendations.py → get_recommendations()
4. save_data.py → save_training_example()
5. app.py → connect everything

---

# 🧠 Current Coding Task

## File
src/main/logic/schema.py

## Function
clean_profile(user_profile)

## Purpose
Translate raw Streamlit answers into consistent machine-readable labels.