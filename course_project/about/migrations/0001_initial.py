# Generated by Django 4.2.3 on 2023-07-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='basliq')),
                ('description', models.TextField(verbose_name='Metn')),
                ('image', models.ImageField(upload_to='about', verbose_name='sekil')),
            ],
            options={
                'verbose_name': 'Haqqimizda',
                'verbose_name_plural': 'Haqqimizda',
            },
        ),
    ]
