# Generated by Django 4.2.3 on 2023-07-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
