from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
    fields = ("title", "time_create", "description", "image", "admin_photo")
    list_display = ("id", "title", "time_create", "admin_photo")
    search_fields = ("title", "id", "time_create")
    readonly_fields = ("time_create", "admin_photo")
    actions = ['delete_selected']
    
    def delete_selected(self, request, queryset):
        for shop in queryset:
            if shop.image:
                shop.image.delete()
            shop.delete()
        self.message_user(request, f"Deleted {queryset.count()} shops and associated pictures.")

    delete_selected.short_description = "Удаалить выбранные магазины"
     
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "id")
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "price", "shop")
    search_fields = ("title", "id", "amount", "price")
    
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
