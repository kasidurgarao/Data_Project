from django.contrib import admin
from .models import Dataset,ComputedData,PlottedData
# Register your models here.
admin.site.register(Dataset)
admin.site.register(ComputedData)
admin.site.register(PlottedData)