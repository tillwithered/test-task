# Generated by Django 4.1.2 on 2023-08-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_imageurl_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(upload_to='pinned_pics', verbose_name='Фотографии'),
        ),
    ]
