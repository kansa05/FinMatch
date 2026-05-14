def get_pathway(cleaned_profile):
    """Return the rule-based pathway for a cleaned profile."""

    # Read safely to avoid KeyError if upstream data is incomplete.
    investment_amount = cleaned_profile.get("investment_amount", 0)
    monthly_contribution = cleaned_profile.get("monthly_contribution", 0)

    risk_level = cleaned_profile.get("risk_level")
    time_horizon = cleaned_profile.get("time_horizon")
    experience_level = cleaned_profile.get("experience_level")
    goals = cleaned_profile.get("goals", [])
    values = cleaned_profile.get("values", [])

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
    
    # Low risk = mostly ETFs.
    if risk_level == "low":
        return "ETF-Heavy"

    # Values-based preference leans toward ETF-heavy (easy ESG/thematic filtering).
    if values and risk_level != "high":
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


def GetPathways(cleaned_profile):
    """Backwards-compatible wrapper for older calls."""
    return get_pathway(cleaned_profile)