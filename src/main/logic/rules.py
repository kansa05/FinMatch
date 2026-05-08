def GetPathways(cleaned_profile): 

    #get the inputs from cleaned_profi;le
    investment_amount = cleaned_profile["investment_amount"]
    monthly_contribution= cleaned_profile["monthly_contribution"]

    risk_level= cleaned_profile["risk_level"]
    time_horizon= cleaned_profile["time_horizon"]
    experience_level= cleaned_profile["experience_level"]
    goals= cleaned_profile["goals"]
    sectors= cleaned_profile["sectors"]
    values=cleaned_profile["values"]

    if time_horizon == "short":
        if risk_level == "high":
            return "ETF-Heavy"
        return "ETF-Only"

    if investment_amount <= 2000 and experience_level == "beginner": 
        return "ETF-Only"

    if investment_amount <=2000 and monthly_contribution <= 200: 
        return "ETF-Only"
    
    if risk_level == "low" and experience_level == "beginner":
        return "ETF-Only"
    if monthly_contribution <= 200 and experience_level == "beginner":
        return "ETF-Only"
    
    #Low risk = mostly ETFs
    if risk_level == "low":
        return "ETF-Heavy"

    #  High risk only becomes growth if horizon is long TO allow for stabilization
    if risk_level == "high" and time_horizon == "long":
        return "Growth"

    # 5. High risk + medium horizon = balanced/growth-ish, not full growth
    if risk_level == "high" and time_horizon == "medium":
        return "Balanced"

    # 6. Medium risk = balanced
    if risk_level == "medium":
        return "Balanced"

    # 7. Goal fallback
    if "growth" in goals and time_horizon == "long":
        return "Growth"

    return "Balanced"