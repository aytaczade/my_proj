# Generated by Django 4.2.3 on 2023-07-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
    ]
