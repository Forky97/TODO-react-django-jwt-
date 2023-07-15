from django.contrib import admin
from .models import Note,User

@admin.register(Note)
class RegisterModels(admin.ModelAdmin):
    pass

