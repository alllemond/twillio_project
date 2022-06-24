from atexit import register
from .models import Category
from django.contrib import admin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields= {'slug':('title',)}