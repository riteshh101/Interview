from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(candidate)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in candidate._meta.fields]

@admin.register(test_score)
class TestScoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in test_score._meta.fields]