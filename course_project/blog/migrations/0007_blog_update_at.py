# Generated by Django 4.2.3 on 2023-07-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
