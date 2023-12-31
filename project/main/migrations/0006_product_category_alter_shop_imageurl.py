# Generated by Django 4.1.2 on 2023-08-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='main.category'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='imageUrl',
            field=models.ImageField(blank=True, upload_to='pinned_pics', verbose_name='Фотографии'),
        ),
    ]
