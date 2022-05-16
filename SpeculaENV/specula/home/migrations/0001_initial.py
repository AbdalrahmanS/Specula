# Generated by Django 4.0.4 on 2022-05-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posterName', models.CharField(max_length=200)),
                ('movieName', models.CharField(max_length=200)),
                ('opinion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TVPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posterName', models.CharField(max_length=200)),
                ('tvShowName', models.CharField(max_length=200)),
                ('opinion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoGamePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posterName', models.CharField(max_length=200)),
                ('videoGameName', models.CharField(max_length=200)),
                ('opinion', models.TextField()),
            ],
        ),
    ]
