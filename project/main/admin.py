from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "time_update")
    search_fields = ("title", "id")
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "id")
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "id")
    
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
