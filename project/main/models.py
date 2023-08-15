from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey



class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    description = models.TextField(blank=True, verbose_name="Описание")
    def __str__(self):
        return str(self.id)
    
    class Meta():
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        permissions = [
            ("can_edit_shop", "Can edit shop"),
        ]
        
class Category(MPTTModel):
    
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()
    def __str__(self):
        return self.title
    class MPTTMeta:
        order_insertion_by = ['title']
    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        permissions = [
            ("can_edit_category", "Can edit category"),
        ]
                
class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name="Категория")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    amount = models.IntegerField(default=0, verbose_name="Количество")
    price = models.FloatField(default=0.0, verbose_name="Цена")
    active = models.BooleanField(default=False, verbose_name="Статус активности")
    orders = models.IntegerField(default=0, verbose_name="Заказы")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    
    def __str__(self):
        return str(self.id)
    
    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_edit_product", "Can edit product"),
        ]
class ShopGallery(models.Model):
    image = models.ImageField(upload_to='shop_pictures')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='images')    
     
class ProductGallery(models.Model):
    image = models.ImageField(upload_to='product_pictures')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    