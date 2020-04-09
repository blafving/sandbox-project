# sandbox-project
# Catchall folder for my unwholesome experiments with django. 

## Experiment 1: Fitness App
Currently you can use this app to import your nutrition and exercise info from myfitnesspal. 
Key difference here is that you can actually look at all your data in one place, see it
graphically and see some snapshots that let you know how you are doing in the context of a week 
or month. 

Very nice for: 
- trend analysis
- seeing how big those cheat days really set you back
- showing the direct connection between Calories and pounds of fat 

## What I'm building right now

1. Energy/Nutrient view 
    - isolate/combine attributes in graph view such as energy consumed, expended, balance, or protein, fat carbs etc.
    - select a custom date range to look at
2. User view
    - More granular control over imports and records management direct from the interface
3. Strength View
    - Model
    - JEFIT integration by using requests and possibly other automation packages
    - URLS
    - Views

## Mid-term vision
1. Agility/Power Section
    - Built-in tools for time trials and reaction drills
    - VO2max calculator
    - .FIT file integration
2. Flexibility Section

## Long-term
1. Comparative analysis between energy, strength, agility and flexibility
2. Machine Learning ... for everything.

    1. Statistics built on cal balance (weekly, monthly, etc.)
    2. Compare these estimates with monthly weight readings
    3. (Far future - suggest changes to Base Metabolic Rate)

Will add exercises
    1. Manually input calories (admin) to calculate in daily calorie balance (Models)
    2. User side form input
    3. Integrate with phone app api (ideally google fit but could be other)

Will add analytics/graphing functionality

BIG Feature! .FIT file upload and analysis coming in summer 