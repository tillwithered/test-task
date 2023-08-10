from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create")
    search_fields = ("title", "id", "time_create")
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "id")
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "price", "shop")
    search_fields = ("title", "id", "amount", "price")
    
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
