# Generated by Django 4.2.3 on 2023-07-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_options_blog_author_blog_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
