from django import forms
from .models import User


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())

