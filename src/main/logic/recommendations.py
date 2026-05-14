def get_recommendations(pathway, cleaned_profile):
    """
    Input:
        pathway: one core strategy from get_pathway()
        cleaned_profile: standardized user profile from clean_profile()

    Output:
        recommendations: a list of dictionaries

    Big idea:
        This function conditionally builds a recommendation list.

        IF the pathway matches,
        THEN we store certain investment dictionaries in the list.

        Each dictionary represents ONE investment.
        The list stores MANY investment dictionaries.

        This is still rule-based logic, not ML yet.
    """

    values = cleaned_profile.get("values", [])
    sectors = cleaned_profile.get("sectors", [])
    investment_types = cleaned_profile.get("investment_types", [])

    # Start with an empty dynamic list.
    # Python lists can grow as we add recommendation dictionaries.
    recommendations = []

    # If the user is ETF-Only, store beginner-friendly ETF dictionaries.
    #list of dictonaries.  
    if pathway == "ETF-Only":
        recommendations = [
            #dictonary 0
            {
                "ticker": "VOO",
                "name": "Vanguard S&P 500 ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Broad S&P 500 exposure; simple beginner-friendly diversification."
            },
            #dictonary 1
            {
                "ticker": "VTI",
                "name": "Vanguard Total Stock Market ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Gives exposure to the overall U.S. stock market."
            }
        ]

    # If the user is ETF-Heavy, store mostly ETF-based recommendations.
    elif pathway == "ETF-Heavy":
        recommendations = [
            {
                "ticker": "VTI",
                "name": "Vanguard Total Stock Market ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Strong core ETF for diversified long-term investing."
            },
            {
                "ticker": "VXUS",
                "name": "Vanguard Total International Stock ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Adds international diversification."
            },
            {
                "ticker": "BND",
                "name": "Vanguard Total Bond Market ETF",
                "asset_type": "ETF",
                "risk_level": "low",
                "reasoning": "Adds stability through bond exposure."
            }
        ]

    # If the user is Balanced, store a mix of stable and growth-oriented investments.
    elif pathway == "Balanced":
        recommendations = [
            {
                "ticker": "VOO",
                "name": "Vanguard S&P 500 ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Stable core market exposure."
            },
            {
                "ticker": "QQQ",
                "name": "Invesco QQQ Trust",
                "asset_type": "ETF",
                "risk_level": "high",
                "reasoning": "Adds growth exposure through large technology-heavy companies."
            },
            {
                "ticker": "SCHD",
                "name": "Schwab U.S. Dividend Equity ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Adds dividend-focused stability."
            }
        ]

    # If the user is Growth, store more aggressive long-term growth recommendations.
    elif pathway == "Growth":
        recommendations = [
            {
                "ticker": "QQQ",
                "name": "Invesco QQQ Trust",
                "asset_type": "ETF",
                "risk_level": "high",
                "reasoning": "Growth-focused ETF with heavy technology exposure."
            },
            {
                "ticker": "VUG",
                "name": "Vanguard Growth ETF",
                "asset_type": "ETF",
                "risk_level": "high",
                "reasoning": "Broad exposure to U.S. growth companies."
            },
            {
                "ticker": "NVDA",
                "name": "NVIDIA Corporation",
                "asset_type": "Stock",
                "risk_level": "high",
                "reasoning": "High-growth individual stock with AI and semiconductor exposure."
            }
        ]

    # Fallback if pathway does not match anything above.
    else:
        recommendations = [
            {
                "ticker": "VTI",
                "name": "Vanguard Total Stock Market ETF",
                "asset_type": "ETF",
                "risk_level": "medium",
                "reasoning": "Default diversified recommendation."
            },
            {
                "ticker": "BND",
                "name": "Vanguard Total Bond Market ETF",
                "asset_type": "ETF",
                "risk_level": "low",
                "reasoning": "Adds stability when no specific pathway is matched."
            }
        ]

    # Preference modifier:
    # If the user selected sustainability as a value,
    # append one more ESG-focused investment dictionary.
    #
    # This does NOT replace the pathway.
    # It customizes the existing recommendation list.
    if "sustainability" in values:
        recommendations.append({
            "ticker": "ESGU",
            "name": "iShares ESG Aware MSCI USA ETF",
            "asset_type": "ETF",
            "risk_level": "medium",
            "reasoning": "Added because the user selected sustainability/values-based preferences."
        })

    # Sector modifier:
    # If the user prefers technology,
    # append a technology-focused ETF dictionary.
    if "technology" in sectors:
        recommendations.append({
            "ticker": "XLK",
            "name": "Technology Select Sector SPDR Fund",
            "asset_type": "ETF",
            "risk_level": "high",
            "reasoning": "Added because the user prefers technology exposure."
        })

    # Investment type modifier:
    # If the user only wants ETFs, remove any recommendation where asset_type is Stock.
    if "etfs" in investment_types and "stocks" not in investment_types:
        recommendations = [
            investment for investment in recommendations
            if investment["asset_type"] == "ETF"
        ]

    return recommendations