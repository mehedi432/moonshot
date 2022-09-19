# Generated by Django 4.1.1 on 2022-09-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='create_at_de',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='create_at_en',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_de',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_en',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status_de',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status_en',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='time_de',
            field=models.CharField(max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='time_en',
            field=models.CharField(max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_de',
            field=models.CharField(max_length=233, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=233, null=True, unique=True),
        ),
    ]