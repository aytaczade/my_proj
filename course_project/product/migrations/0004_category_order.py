# Generated by Django 4.2.3 on 2023-07-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]