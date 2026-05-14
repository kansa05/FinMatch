#Concepts


## Cleaning up the data

It is important to clean up the raw data so it is readable and understanable by your schema. I did this with schema.py

The function clean_profile, cleans up the user_profile(the answers given by the user)

It creates a dictonary cleaned_profile, and says fields like investment_amount, monthly_contribution, risk_preference, risk_level, time_horizon, experience_level, investment_goals, goals, investment, types, etc. 

##Base level rules

using the function GetPathways rules.py creates base level rules to instruct the ML with this

## recommendations

using the function get_recommendations, it creates an empty list recommendation which gets filled with dictonaries. 

