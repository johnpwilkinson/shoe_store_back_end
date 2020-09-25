from django.contrib import admin

# Register your models here.
from .models import Manufacturer, ShoeType, ShoeColor, Shoe

admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)