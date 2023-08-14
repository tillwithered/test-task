from typing import Any, List, Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django_admin_filters import DateRange
from django_mptt_admin.admin import DjangoMpttAdmin
from django.forms.models import BaseInlineFormSet
import os 


class GalleryInline(admin.TabularInline):
    extra = 1
    fk_name = 'product'
    model = ProductGallery
    readonly_fields = ('image_preview', )
    
    def delete_model(self, request, obj):
        obj.image.delete()
        print("removing")
        # os.remove(f'media/product_pictures/{url}')
        super().delete_model(request, obj)
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" width="20%" height="10%" />'.format(obj.image.url))
        else:
            return '(No image)'   
    
    
class PriceProductFilter(DateRange):
    FILTER_LABEL = "Интервал цены"
    BUTTON_LABEL = "Задать интервал"
    FROM_LABEL = "От"
    TO_LABEL = "До"
    ALL_LABEL = ''
    CUSTOM_LABEL = ""
    NULL_LABEL = ""
    DATE_FORMAT = "Введите промежуток"
    options = (
      ('1da', "", 0),
      ('1dp', "", 0),
    )
    @staticmethod
    def to_dtime(text):
        try:
            return int(text)
        except ValueError:
            return None
    
         
class ShopAdmin(admin.ModelAdmin):
    fields = ("title", "time_create", "description", "image", "admin_photo")
    list_display = ("id", "title", "time_create", "admin_photo")
    search_fields = ("title")
    readonly_fields = ("time_create", "admin_photo")
    actions = ['delete_selected']
    
    def delete_selected(self, request, queryset):
        for shop in queryset:
            if shop.image:
                shop.image.delete()
            shop.delete()
        self.message_user(request, f"Deleted {queryset.count()} shops and associated pictures.")

    delete_selected.short_description = "Удаалить выбранные магазины"
     
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "parent")
    search_fields = ("title", "id", "parent")
    actions = ['show_all_paths']

    def show_all_paths(self, request, queryset):
        url = reverse('scheme')
        return HttpResponseRedirect(url)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "price", "shop", "orders","active", "time_create", 'preview') #"display_gallery_info"
    search_fields = ("title", "id")
    list_filter = ('shop', 'active', ('price', PriceProductFilter))
    inlines = [GalleryInline,] 
    def preview(self, obj):
        data_set = ProductGallery.objects.filter(product_id=obj)
        try:
            data = data_set[0]
            return  mark_safe("<img src='{}' width='150' />".format(data.image.url))
        except Exception:
            return "---"
        
        

          
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)

