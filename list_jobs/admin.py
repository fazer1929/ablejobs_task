from django.contrib import admin
from .models import CustomUser,Job
# Register your models here.
admin.site.register(Job)
admin.site.register(CustomUser)