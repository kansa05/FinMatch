def clean_profile(user_profile):
    """
    Input: raw user_profile dict from Streamlit
    Output: cleaned_profile dict with standardized values
    """

    # 1. initialize
    cleaned_profile = {}

    # 2. numeric fields
    cleaned_profile["investment_amount"] = user_profile["investment_basics"]
    cleaned_profile["monthly_contribution"] = user_profile["monthly_contribution"]

    # 3. risk mapping
    raw_risk = user_profile["risk_preference"]
    # map raw_risk → "low" / "medium" / "high"
    if raw_risk == "I prefer stable, predictable growth":
        cleaned_profile["risk_level"]= "low"
    elif raw_risk == "I want a balance of stability and growth": 
        cleaned_profile["risk_level"] = "medium"
    
    elif raw_risk == "I am okay with ups and downs for higher growth":
        cleaned_profile["risk_level"] = "high"
    else: 
        cleaned_profile["risk_level"] = None

    # 4. time horizon mapping
    raw_time = user_profile["time_horizon"]
    #map raw_time → "short" / "medium" / "long"

    if raw_time == "Short-term (1-3 years)":
        cleaned_profile["time_horizon"] = "short"
    elif raw_time == "Medium-term (3-10 years)":
        cleaned_profile["time_horizon"] = "medium"
    elif raw_time == "Long-term (10+ years)":
        cleaned_profile["time_horizon"] = "long"
    else:
        cleaned_profile["time_horizon"] = []

    # 5. experience mapping
    raw_exp = user_profile["experience_level"]
    # map raw_exp → "beginner" / "intermediate" / "advanced"

    if raw_exp == "I'm just starting out, learning as I go":
        cleaned_profile["experience_level"] = "beginner"
    elif raw_exp == "I have some experience, but want to learn more": 
        cleaned_profile["experience_level"] = "intermediate"
    elif raw_exp == "I'm an expert, I know exactly what I'm doing": 
        cleaned_profile["experience_level"] = "advanced"
    else: 
        cleaned_profile["experience_level"] = None

    # 6. goals
    raw_goal = user_profile["investment_goals"]
    #  convert to standardized list format

    if raw_goal == "Growth":
        cleaned_profile["goals"] = ["growth"]
    elif raw_goal == "Retirement":
        cleaned_profile["goals"]= ["retirement"]
    elif raw_goal == "Education":
        cleaned_profile["goals"] = ["education"]
    else: 
        cleaned_profile["goals"] = []

    # 7. sectors
    raw_sectors = user_profile["preferred_sectors"]
    # clean + lowercase + standardize names


    cleaned_sectors = []

    for sector in raw_sectors:
        cleaned_sectors.append(sector.lower())

    cleaned_profile["sectors"] = cleaned_sectors
        

    # 8. investment types
    raw_types = user_profile["preferred_investment_types"]
    cleaned_investment_types= []

    for types in raw_types: 
        cleaned_investment_types.append(types.lower())

    cleaned_profile["investment_types"] = cleaned_investment_types

    # 9. values/preferences
    raw_values = user_profile["values_preferences"]
    # map phrases → standardized tags

    cleaned_values= []

    for values in raw_values:
        cleaned_values.append(values.lower())
    
    cleaned_profile["values"] = cleaned_values

    # 10. return final cleaned profile
    return cleaned_profile