# Generated by Django 4.1.2 on 2023-08-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ребенок', to='main.category'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, upload_to='shop_pictures/', verbose_name='Фотография'),
        ),
    ]