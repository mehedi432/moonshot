# Generated by Django 4.1.1 on 2022-09-18 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_content_de_post_content_en_post_create_at_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_en',
        ),
    ]
