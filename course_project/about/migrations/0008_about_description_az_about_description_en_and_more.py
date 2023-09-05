# Generated by Django 4.2.3 on 2023-08-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description_az',
            field=models.TextField(null=True, verbose_name='Metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='footer_description_az',
            field=models.TextField(null=True, verbose_name='footer-deki metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='footer_description_en',
            field=models.TextField(null=True, verbose_name='footer-deki metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='footer_description_ru',
            field=models.TextField(null=True, verbose_name='footer-deki metn'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='basliq'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='basliq'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='basliq'),
        ),
        migrations.AddField(
            model_name='store',
            name='address_az',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='address_en',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='address_ru',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='name_az',
            field=models.CharField(default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='name_en',
            field=models.CharField(default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='name_ru',
            field=models.CharField(default=0, max_length=255, null=True),
        ),
    ]