# Generated by Django 4.2.3 on 2023-08-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_campaign_name_az_campaign_name_en_campaign_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_trand',
            field=models.BooleanField(default=False),
        ),
    ]