# Generated by Django 4.2.3 on 2023-08-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_name_az_category_name_en_category_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_az',
            field=models.TextField(null=True, verbose_name='təsviri'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='təsviri'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='təsviri'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=200, null=True, verbose_name='ad'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='ad'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='ad'),
        ),
    ]
