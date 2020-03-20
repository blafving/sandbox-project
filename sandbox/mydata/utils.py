"""
Utilities for data handling
"""
import myfitnesspal
from .models import Nutrient

def log_myfitpal(user, reqdate):
    """
    Takes a datetime date and user and updates the database with api entry
    """
    client = myfitnesspal.Client(user)
    api_day = client.get_date(reqdate)
    try: 
        edits = Nutrient.objects.get(date=reqdate)
        edits.calories = api_day.totals['calories']
        edits.sodium = api_day.totals['sodium']
        edits.carbs = api_day.totals['carbohydrates']
        edits.fat = api_day.totals['fat']
        edits.sugar = api_day.totals['sugar']
        edits.protein = api_day.totals['protein']
        edits.save()
    except:
        Nutrient.objects.create(
            date=reqdate, 
            calories=api_day.totals['calories'],
            sodium = api_day.totals['sodium'],
            carbs = api_day.totals['carbohydrates'],
            fat = api_day.totals['fat'],
            sugar = api_day.totals['sugar'],
            protein = api_day.totals['protein'],
        )

    return