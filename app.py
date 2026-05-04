import streamlit as st
import json

if "page" not in st.session_state:
    st.session_state.page = "home"



# -------------------------
# APP TITLE
# -------------------------

#displays the title and subtitle of the app, doe snot have a return value
if st.session_state.page == "home":

    st.title("FinMatch")
    st.subheader("Welcome to the beginning of your investment journey")
# -------------------------
# DISCLAIMER
# -------------------------
    st.warning("For educational purposes only, used to estimate and provide recommendations.")
    st.write("Answer a few questions and get personalized educational investing ideas.")


# -------------------------
# PHASE 1: USER ONBOARDING
# -------------------------

    if st.button("Start My Journey"):
        st.write("Let's get started!")
        st.session_state.page = "survey"



# --- Section: Investment Basics ---
# initial investment
# monthly contribution
elif st.session_state.page == "survey":

    st.header("Starting with your numbers")
    investment_basics = st.number_input("How much money are you willing to invest?",
    min_value=0, step=50, value=1000, help="Enter the amount you are willing to invest")

    monthly_contribution = st.number_input("How much money are you willing to contribute monthly?",
    min_value=0, step=100, value=100, help="Enter the amount you are willing to contribute monthly")

    # --- Section: Goals ---
    # main goal (growth, retirement, etc.)
    # when user needs money (time horizon)
    st.header("What are your main goals")

    investment_goals = st.selectbox("What is your main investment goal?",
    ["Growth", "Retirement", "Education" ], help="Select your main investment goal")

    time_horizon = st.selectbox("How long do you plan to invest?",
    ["Short-term (1-3 years)", "Medium-term (3-10 years)", "Long-term (10+ years)"], help="Select your time horizon")


    # --- Section: Risk / Behavior ---
    # stability vs growth preference
    # investing consistency
    st.header("Your investment style")

    risk_preference = st.radio(
        "Which sounds more like you?",
        [
            "I prefer stable, predictable growth",
            "I want a balance of stability and growth",
            "I am okay with ups and downs for higher growth"
        ]
    )

    investing_consistency = st.radio(
        "How consistent do you want to be in your investing?",
        [
            "I can invest regularly and want to stick to a plan",
            "I can invest sometimes and follow market trends",
            "I’m not sure yet, I’m just exploring"
        ]
    )
    # --- Section: Experience ---
    # experience level
    st.header("Your experience level")
    experience_level = st.radio(
        "How experienced are you with investing?",
        [ "I'm just starting out, learning as I go",
        "I have some experience, but want to learn more",
        "I'm an expert, I know exactly what I'm doing"
        ]
    )

    # --- Section: Interests ---
    # preferred sectors
    #eventually will make a screen that explains all of these options
    st.header("Your interests")
    preferred_sectors = st.multiselect(
        "What sectors are you interested in?",
        ["Technology", "Healthcare", "Financial Services", "Consumer Discretionary", "Energy", "Industrials", "Utilities", "Telecommunications", "Real Estate", "Consumer Staples"],
        help="Select the sectors you are interested in"
    )

#eventually will make a screen that explains all of these options
    preferred_investment_types = st.multiselect(
        "What types of investments are you interested in?",
        ["Stocks", "Bonds", "Mutual Funds", "ETFs", "Cryptocurrency", "Real Estate", "Other"],
        help="Select the types of investments you are interested in"
    )
    # --- Section: Preferences ---
    st.header("Your Preferences")

    values_preferences = st.multiselect(
        "Are there any values you care about when investing?",
        [
            "Climate-friendly companies",
            "Strong labor practices",
            "Diverse leadership",
            "Ethical business practices",
            "Avoid fossil fuels",
            "Avoid controversial industries",
            "No strong preference"
        ]
    )

    # --- Submit Button ---
    if st.button("Submit"):
        user_profile = {
            "investment_basics": investment_basics,
            "monthly_contribution": monthly_contribution,
            "investment_goals": investment_goals,
            "time_horizon": time_horizon,
            "risk_preference": risk_preference,
            "investing_consistency": investing_consistency,
            "experience_level": experience_level,
            "preferred_sectors": preferred_sectors,
            "preferred_investment_types": preferred_investment_types,
            "values_preferences": values_preferences
        }

        # store in session (temporary)
        st.session_state.user_profile = user_profile

        # save to JSON file (permanent)
        with open("user_profiles.jsonl", "a") as f:
            json.dump(user_profile, f)
            f.write("\n")

        st.session_state.page = "results"
        st.rerun()