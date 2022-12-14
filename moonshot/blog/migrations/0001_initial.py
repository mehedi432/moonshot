# Generated by Django 4.1.1 on 2022-09-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('time', models.CharField(max_length=233)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
