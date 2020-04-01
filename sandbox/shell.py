"""
Some helpful functions to work on getting api data into my database
"""
from django.db import models
from django.utils import timezone
import datetime
import myfitnesspal
from mydata.models import Day, Nutrient, User

Brandon = User.objects.get(id=1)
Brandon.weight_init

day_obj = Day.objects.get(user=Brandon, date=datetime.date(2020, 2, 19))
day_obj.weight

Day.objects.create(date=datetime.date(2020, 2, 17), user=Brandon, new_weight=194)
Day.objects.create(date=datetime.date(2020, 2, 18), user=Brandon, new_weight=193.9)
Day.objects.create(date=datetime.date(2020, 2, 19), user=Brandon, new_weight=193.8)

day_obj.age
day_obj.base_metabolic_rate()


nut_obj = Nutrient.objects.get(id=1)
nut_obj.update()
