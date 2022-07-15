from django.contrib import admin
from .models import Test
# Register your models here.
admin.site.register(Test)

# @admin.register(Test)
# class Test(admin.ModelAdmin):
#     list_display = ['__all__']
