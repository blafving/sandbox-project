from django.contrib import admin
from .models import User, Nutrient, Day
# Register your models here.
admin.site.register(User)
admin.site.register(Nutrient)
admin.site.register(Day)