from django import forms
from .models import User


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())

class DataForm(forms.Form):
    CALORIES = 'CAL'  
    SODIUM = 'SAL'
    CARBOHYDRATES = 'CRB'
    FAT = 'FAT'
    SUGAR = 'SUG'
    PROTEIN = 'PRO'
    BALANCE = 'BAL'
    CALORIES_BURNED = 'BUR'
    DATATYPES = [
        (PROTEIN,'Protein (grams)'),
        (SODIUM, 'Sodium (grams)'),
        (CARBOHYDRATES, 'Carbohydrates (grams)'),
        (FAT, 'Fat (grams)'),
        (SUGAR, 'Sugar (grams)'),
        (PROTEIN, 'Protein (grams'),
        (CALORIES, 'Calories Consumed (Cal)'),
        (BALANCE, ' Caloric Balance (+/- Cal)'),
        (CALORIES_BURNED, 'Calories Burned')
    ]
    choices = forms.ChoiceField(choices=DATATYPES)

