# Generated by Django 4.2.3 on 2023-07-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_store_options_store_address_store_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='optional_phone_number',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
