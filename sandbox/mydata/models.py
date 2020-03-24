from django.db import models
from django.utils import timezone
import datetime
import myfitnesspal

# Create your models here.
class User(models.Model):
    firstname = models.CharField('First Name', max_length=50)
    lastname = models.CharField('Last Name', max_length=50)
    height = models.SmallIntegerField('Height (in.)', default=64)
    weight = models.SmallIntegerField('Weight (lbs.)', default=150)
    GENDERS = [
        ('ML', 'Male'),
        ('FM', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDERS)
    myfitpal_user = models.CharField(max_length=50)
    myfitpal_pw = models.CharField(max_length=50)

    def name(self):
        return self.firstname + ' ' + self.lastname

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Nutrient(models.Model):
    date = models.DateField(primary_key=True)
    calories = models.SmallIntegerField(default=0)
    sodium = models.SmallIntegerField(default=0)
    carbs = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)
    sugar = models.SmallIntegerField(default=0)
    protein = models.SmallIntegerField(default=0)
    userid = models.CharField(max_length=50)
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

    def update(self):
        """
        updates the item from myfitpal api
        """
        client = myfitnesspal.Client(self.user_rec.myfitpal_user)
        api_day = client.get_date(self.date)
        self.calories = api_day.totals['calories']
        self.sodium = api_day.totals['sodium']
        self.carbs = api_day.totals['carbohydrates']
        self.fat = api_day.totals['fat']
        self.sugar = api_day.totals['sugar']
        self.protein = api_day.totals['protein']
        self.save()
        return str(self.date) + 'nutrition updated'


"""


# class Exercise(models.Model):
#     date = models.DateField()
#     start = models.TimeField()
#     end = models.TimeField()

#     class Meta:
#         abstract = True

# class Run(Exercise):
#     RUN_TYPES = (
#         ('LDR', 'Long distance run/walk'),
#         ('VO2', 'Cooper VO2max Test'),
#         ('INT')
#     )
#     distance = 

"""