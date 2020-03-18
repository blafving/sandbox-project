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
    Nutrient.objects.create(date=reqdate, calories=api_day.totals['calories'])

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
END = datetime.date(2020, 3, 17)
