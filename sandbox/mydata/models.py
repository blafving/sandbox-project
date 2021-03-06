from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
import datetime
import myfitnesspal
from django.core import exceptions


# Create your models here.
class User(AbstractUser):
    height = models.SmallIntegerField('Height (in.)', default=64)
    birthday = models.DateField('Birthday', default=datetime.date(1981, 9, 20))
    GENDERS = [
        ('ML', 'Male'),
        ('FM', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDERS)
    start_date = models.DateField('My Fitness Pal Start Date', default=datetime.date(2020, 3, 10))
    myfitpal_user = models.CharField(max_length=50)
    myfitpal_pw = models.CharField(max_length=50)
    weight_init = models.FloatField('Weight', default=190)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name
        
    def block_import(self, start):
        """
        Ensures that there are no more than one Day and one Nutrient for each day of the calendar
        since the start date.
        """
        scanner = start
        while scanner < (datetime.date.today()):
            while Day.objects.filter(user=self, date=scanner).count() > 1:
                print('I found more than one Day on %s' % str(scanner))
                day_list = Day.objects.filter(user=self, date=scanner)
                day_list[0].delete()
            day, created = Day.objects.get_or_create(user=self, date=scanner)
            while Nutrient.objects.filter(date_owner=day.id, user_owner=self).count() > 1:
                nut_list = Nutrient.objects.filter(date_owner=day.id, user_owner=self)
                nut_list[0].delete()
            nut, created = Nutrient.objects.get_or_create(date_owner=day, user_owner=self)
            day.nutrient.update()
            scanner += datetime.timedelta(days=1)

    def recent_import(self):
        """
        Imports all fitness data from last import to yesterday
        """
        last_import = Day.objects.filter(user=self).order_by('date').reverse()
        last_date = last_import[0].date + datetime.timedelta(days=1) 
        self.block_import(last_date)

    def snapshot(self):
        """
        Gives high level analytics including weekly and monthly figure in a nice dictionary
        keys: cal_balance, cal_mean, cal_burned, burn_mean
        """
        stats = {}
        # Weekly statistics
        week = Day.objects.filter(user=self).order_by('date').reverse()[:6]
        month = Day.objects.filter(user=self).order_by('date').reverse()[:30]
        stats['Running Weekly Energy Balance'] = int(sum([entry.nutrient.balance for entry in week]))
        mean_fat = str(sum([entry.nutrient.balance for entry in month]) / month.count() / 3500)
        stats['Mean lbs. of fat per day'] = mean_fat[:6]
        stats['Exercise in last 7 days'] = int(sum([entry.nutrient.cal_burned for entry in week]))
        stats['Mean exercise per day'] = int(sum([entry.nutrient.cal_burned for entry in month]) / month.count())
        return stats
        

class Day(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField('Date')
    new_weight = models.FloatField(
        'Weight Reading (lbs.)', 
        null=True, 
        blank=True,
    )
    
    def __str__(self):
        return str(self.date)

    @property
    def base_metabolic_rate(self):
        user_ref = self.user
        height = float(user_ref.height)
        age = self.age
        weight = self.weight[1]
        if user_ref.gender == 'ML':
            return (
                88.362 + (13.397 * weight / 2.205) \
                + (4.799 * height * 2.54) - (5.677 * age)
            )
    @property
    def weight(self):
        """
        returns a tuple of (
            [0]date measurement, 
            [1]weight ) from the most recent weight reading
        """
        user_ref = self.user
        if Day.objects.filter(user=user_ref, date__lte=self.date, new_weight__isnull=False):  # Pull the most recent new_weight
            last_rec = Day.objects.filter(user=user_ref, date__lte=self.date, new_weight__gt=0).order_by('-date')[0]
            weight = last_rec.new_weight
            measured_on = last_rec.date
        else:
            weight = self.user.weight_init
            measured_on = self.user.date_joined
        return (measured_on, weight)

    @property
    def age(self):
        user_ref = self.user
        delta = datetime.date.today() - user_ref.birthday
        return delta.days / 365.242199

    @property
    def cal_balance(self):
        """
        The number of calories added or subtracted from User this day.
        """
        return int(self.nutrient.calories - self.base_metabolic_rate - self.nutrient.cal_burned)
    
    # @property
    # def cal_burned(self):
    #     return Nutrient.objects.get(date_owner=self, user=self.user).cal_burned

class Nutrient(models.Model):
    date_owner = models.OneToOneField(Day, 
        on_delete=models.CASCADE,
    )
    user_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    calories = models.SmallIntegerField(default=0)
    sodium = models.SmallIntegerField(default=0)
    carbs = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)
    sugar = models.SmallIntegerField(default=0)
    protein = models.SmallIntegerField(default=0)
    balance = models.SmallIntegerField(default=0)
    cal_burned = models.SmallIntegerField(default=0)

    def __str__(self):
        username = self.get_username()
        day = str(self.get_date())
        return '%s: %s' % (username, day)

    def get_date(self):
        """
        Returns date of Day owner as datetime object
        """
        day = self.date_owner
        return day.date

    def get_username(self):
        """
        Retrieves name of user object as single string 'Firstname Lastname'
        """
        user = self.user_owner
        return user.name()

    def update(self):
        """
        updates the item from myfitpal api
        """
        user = self.user_owner
        day = self.date_owner
        client = myfitnesspal.Client(user.myfitpal_user)
        api_day = client.get_date(self.get_date())
        self.calories = api_day.totals['calories']
        self.sodium = api_day.totals['sodium']
        self.carbs = api_day.totals['carbohydrates']
        self.fat = api_day.totals['fat']
        self.sugar = api_day.totals['sugar']
        self.protein = api_day.totals['protein']
        try:
            self.cal_burned = sum([x['nutrition_information']['calories burned'] for x in api_day.exercises[0].get_as_list()])
        finally:
            self.balance = self.calories - (day.base_metabolic_rate + self.cal_burned)
            self.save()
            return str(self.date_owner) + ': nutrition updated'
    
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