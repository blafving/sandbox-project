'''
A nice set of functions to help manage lists and dictionaries
To use when running data to/from modules in django
'''
CALORIES = 'CAL'  
SODIUM = 'SAL'
CARBOHYDRATES = 'CRB'
FAT = 'FAT'
SUGAR = 'SUG'
PROTEIN = 'PRO'
BALANCE = 'BAL'
CALORIES_BURNED = 'BUR'

DATATYPES = [
    (SODIUM, 'Sodium (grams)'),
    (CARBOHYDRATES, 'Carbohydrates (grams)'),
    (FAT, 'Fat (grams)'),
    (SUGAR, 'Sugar (grams)'),
    (PROTEIN,'Protein (grams)'),
    (CALORIES, 'Calories Consumed (Cal)'),
    (BALANCE, ' Caloric Balance (+/- Cal)'),
    (CALORIES_BURNED, 'Calories Burned')
]

model_fields = '''sodium = models.SmallIntegerField(default=0)
carbs = models.SmallIntegerField(default=0)
fat = models.SmallIntegerField(default=0)
sugar = models.SmallIntegerField(default=0)
protein = models.SmallIntegerField(default=0)
calories = models.SmallIntegerField(default=0)
balance = models.SmallIntegerField(default=0)
cal_burned'''

model_fields2 = model_fields.split(' = models.SmallIntegerField(default=0)\n')
print(model_fields2)
datatypes = [data[0] for data in DATATYPES]
print(datatypes)
model_dict = dict(zip(datatypes, model_fields2))
print(model_dict)
for value in model_dict.values():
    value = 'self.'