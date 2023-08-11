from django.db import models
from django.utils.safestring import mark_safe
class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(blank=True, upload_to="shop_pictures/", verbose_name="Фотография")
    
    def admin_photo(self):
        if self.image:
            return mark_safe("<img src='{}' width='150' />".format(self.image.url))
    admin_photo.short_description = "Фотография"
    admin_photo.allow_tags = True
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        
class Category(models.Model):
    
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='children')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
                
class Product(models.Model):
    category = models.ManyToManyField(Category)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    amount = models.IntegerField(default=0, verbose_name="Количество")
    price = models.FloatField(default=0.0, verbose_name="Цена")
    ative = models.BooleanField(default=False, verbose_name="Статус активности")
    images = models.ImageField(blank=True, verbose_name="Фотографии")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    
    
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

