"""
Some helpful functions to work on getting api data into my database
"""
import datetime
from mydata.models import Nutrient
import myfitnesspal
from django.db import models

def log_myfitpal(user, reqdate):
    """
    Takes a datetime date and user and updates the database with api entry
    """
    client = myfitnesspal.Client(user)
    api_day = client.get_date(reqdate)
    if not Nutrient.objects.get(date=reqdate):
        print('No object there')
        Nutrient.objects.create(
            date=reqdate, 
            calories=api_day.totals['calories'],
            sodium = api_day.totals['sodium'],
            carbs = api_day.totals['carbohydrates'],
            fat = api_day.totals['fat'],
            sugar = api_day.totals['sugar'],
            protein = api_day.totals['protein'],
            )
    else:
        print('There is an entry for that date')
        edits = Nutrient.objects.get(date=reqdate)
        edits.calories = api_day.totals['calories']
        edits.sodium = api_day.totals['sodium']
        edits.carbs = api_day.totals['carbohydrates']
        edits.fat = api_day.totals['fat']
        edits.sugar = api_day.totals['sugar']
        edits.protein = api_day.totals['protein']
        print(edits.protein)
        edits.save()
    return

def import_block_myfitpal(user, origin, end):
    """
    From two dates a beginning and end imports nutritional values to database
    """
    reqdate = origin
    daycounter = datetime.timedelta(days=1)
    while reqdate <= end:
        log_myfitpal(user, reqdate)
        reqdate += daycounter

ORIGIN = datetime.date(2020, 2, 15)
END = datetime.date(2020, 3, 18)
