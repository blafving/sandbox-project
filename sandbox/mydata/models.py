from django.db import models

# Create your models here.
Class Nutrient(models.Model):
    date = models.DateField()
    calories = models.SmallIntegerField()
    sodium = models.SmallIntegerField()
    carbs = models.SmallIntegerField()
    fat = models.SmallIntegerField()
    sugar = models.SmallIntegerField()
    protein = models.SmallIntegerField()
    BREAKFAST = 'BRK'
    LUNCH = 'LUN'
    DINNER = 'DIN'
    MEAL_CHOICES = [
        (BREAKFAST = 'Breakfast'),
        (LUNCH = 'Lunch'),
        (DINNER = 'Dinner'),
    ]
    meal = models.Charfield(max_length = 3, choices = MEAL_CHOICES)
