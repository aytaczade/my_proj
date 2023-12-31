# Generated by Django 4.2.3 on 2023-07-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Green', 'Green'), ('Gray', 'Gray'), ('Red', 'Red'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Orange', 'Orange')], max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=255),
        ),
    ]
