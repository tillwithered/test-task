from typing import Any, List, Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django_admin_filters import DateRange
from django_mptt_admin.admin import DjangoMpttAdmin
import os 
from django.contrib.sessions.models import Session

class ProductGalleryInline(admin.TabularInline):
    extra = 1
    fk_name = 'product'
    verbose_name = "Добавить Фото"
    verbose_name_plural = "Добавить Фотографии"
    model = ProductGallery
    readonly_fields = ('product_preview', )
    def product_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" width="20%" height="10%" />'.format(obj.image.url))
        else:
            return '(No image)'
        
class ShopGalleryInline(admin.TabularInline):
    extra = 1
    fk_name = 'shop'
    verbose_name = "Добавить Фото"
    verbose_name_plural = "Добавить Фотографии"
    model = ShopGallery
    readonly_fields = ('product_preview',)
    def product_preview(self, obj):
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
    list_display = ("id", "title", "time_create", 'preview')
    search_fields = ("title",)
    readonly_fields = ("time_create",)
    inlines = [ShopGalleryInline, ]
    def preview(self, obj):
        data_set = ShopGallery.objects.filter(shop_id=obj)
        try:
            data = data_set[0]
            return  mark_safe("<img src='{}' width='150' />".format(data.image.url))
        except Exception:
            return "---"
        
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "parent")
    search_fields = ("title", "id")
    actions = ['show_all_paths']

    def show_all_paths(self, request, queryset):
        answer = []
        for data in queryset:
            instance = Category.objects.get(title=data)
            sub_answer = [instance.title]
            while instance.parent_id != None:
                sub_answer.append(name := (Category.objects.filter(id=instance.parent_id)[0].title))
                instance = Category.objects.get(title=name)
            answer.append(sub_answer)
        request.session['category_path'] = answer
        url = reverse('scheme')
        return HttpResponseRedirect(url)
    show_all_paths.short_description = "Показать отношения категорий"

    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "price", "shop", "orders","active", "time_create", 'preview') #"display_gallery_info"
    search_fields = ("title", "id")
    list_filter = ('shop', 'active', ('price', PriceProductFilter))
    inlines = [ProductGalleryInline,] 
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

