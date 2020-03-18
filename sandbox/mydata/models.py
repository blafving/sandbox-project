from django.db import models
from django.utils import timezone
import datetime
import myfitnesspal

# Create your models here.
class Nutrient(models.Model):
    date = models.DateField(primary_key=True)
    calories = models.SmallIntegerField(default=0)
    sodium = models.SmallIntegerField(default=0)
    carbs = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)
    sugar = models.SmallIntegerField(default=0)
    protein = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return str(self.date)

    @property
    def __is_updated__(self):
        client = myfitnesspal.Client('blafving@gmail.com')
        api_day = client.get_date(self.date)
        return self.calories == api_day.totals['calories']