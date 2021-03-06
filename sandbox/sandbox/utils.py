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
    if Nutrient.objects.get(date=reqdate).DoesNotExist == True or \
    Nutrient.objects.get(date=reqdate) != api_day.totals['calories']:
        db_meal = Nutrient(date=date, calories=api_day.totals['calories'])
        db_meal.save()

def import_block_myfitpal(user, origin, end):
    """
    From two dates a beginning and end imports nutritional values to database
    """
    reqdate = origin
    daycounter = datetime.timedelta(days=1)
    while reqdate <= end:
        log_myfitpal(user, reqdate)
        reqdate += daycounter