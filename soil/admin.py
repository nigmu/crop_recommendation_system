from django.contrib import admin

from .models import upload_soil_data_class


# Register your models here.

class upload_soil_data_admin(admin.ModelAdmin):
    list_display = ['id', 'N', 'P', 'K', 'Temperature', 'Humidity', 'Ph', 'Rainfall', 'predicted_crop']


admin.site.register(upload_soil_data_class, upload_soil_data_admin)