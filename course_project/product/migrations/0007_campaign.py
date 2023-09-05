# Generated by Django 4.2.3 on 2023-07-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_productimage_created_at_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('percent', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Kompaniya',
                'verbose_name_plural': 'Kompaniyalar',
            },
        ),
    ]