"""
Some helpful functions to work on getting api data into my database
"""
from django.db import models
from django.utils import timezone
import datetime
import myfitnesspal
from mydata.models import Day, Nutrient, User
from django.core import exceptions

Brandon = User.objects.get(id=1)
days = Day.objects.filter(user=Brandon).order_by('date')   
yesterday = datetime.date(2020, 3, 29)
day = Day.objects.get(user=Brandon, date=yesterday)
range_balance = Day.objects.filter(user=Brandon, date__gte=datetime.date(2020, 2, 15))
net = 0
for day in range_balance:
    net += day.cal_balance
print(net)

day_obj = Day.objects.get(user=Brandon, date=datetime.date(2020, 2, 19))
day_obj.weight

week = Day.objects.filter(user=Brandon, date__lte=datetime.date()

day_obj.age
day_obj.base_metabolic_rate()


nut_obj = Nutrient.objects.get(id=1)
nut_obj.update()
