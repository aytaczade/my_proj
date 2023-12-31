# Generated by Django 4.2.3 on 2023-07-06 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ad')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ad')),
                ('description', models.TextField(verbose_name='tesviri')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='qiymet')),
                ('price_currency', models.CharField(choices=[('AZN', 'AZN'), ('USD', 'USD'), ('EUR', 'EUR')], default='AZN', max_length=50)),
                ('size', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('category', models.ManyToManyField(related_name='products', to='product.category')),
            ],
            options={
                'verbose_name': 'Mehsul',
                'verbose_name_plural': 'Mehsullar',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='sekil')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
            options={
                'verbose_name': 'Mehsul sekli',
                'verbose_name_plural': 'Mehsul sekilleri',
            },
        ),
    ]
