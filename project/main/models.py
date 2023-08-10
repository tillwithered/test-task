from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    description = models.TextField(blank=True, verbose_name="Описание")
    imageUrl = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    amount = models.IntegerField(default=0, verbose_name="Количество")
    price = models.FloatField(default=0.0, verbose_name="Цена")
    ative = models.BooleanField(default=False, verbose_name="Статус активности")
    images = models.ImageField(verbose_name="Фотографии")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    
    
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"