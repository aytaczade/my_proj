# Generated by Django 4.2.3 on 2023-08-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_campaign'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Məhsul', 'verbose_name_plural': 'Məhsullar'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Məhsul şəkli', 'verbose_name_plural': 'Məhsullar şəkilləri'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Green', 'Green'), ('Gray', 'Gray'), ('Red', 'Red'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Orange', 'Orange')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='təsviri'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='qiymət'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='şəkil'),
        ),
    ]
