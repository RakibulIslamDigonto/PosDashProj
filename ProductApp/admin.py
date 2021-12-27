from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'cate_name',
        'cate_shot_des',
        'cate_des',
        'cate_image',
        'parent',
        'slug',
        'code',
        'is_active'
    ]
admin.site.register(Category, CategoryAdmin)