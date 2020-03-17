"""
Some helpful functions to work on getting api data into my database
"""
import datetime
from .models import Nutrient
import myfitnesspal

def log_myfitpal(user, date):
    """
    Takes a datetime date and user and updates the database
    """
    client = myfitnesspal.Client(user)
    if date not in Nutrient.objects.all():
        api_day = client.get_date(date)
        db_meal = Nutrient(date=date, calories=api_day.totals['calories'])
        db_meal.save()