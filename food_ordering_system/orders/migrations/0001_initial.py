# Generated by Django 5.0.3 on 2024-06-17 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
                ('category_gif', models.ImageField(upload_to='media')),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'List of Diner Platters',
                'verbose_name_plural': 'List of Diner Platters',
            },
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'List of Pasta',
                'verbose_name_plural': 'List of Pasta',
            },
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name': 'List of Regular Pizza',
                'verbose_name_plural': 'List of Regular Pizza',
            },
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'List of Salad',
                'verbose_name_plural': 'List of Salad',
            },
        ),
        migrations.CreateModel(
            name='SavedCarts',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cart', models.TextField()),
            ],
            options={
                'verbose_name': 'Saved Users Cart',
                'verbose_name_plural': 'Saved Users Cart',
            },
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name': 'List of Sicilian Pizza',
                'verbose_name_plural': 'List of Sicilian Pizza',
            },
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_filling', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'List of Subway Food',
                'verbose_name_plural': 'List of Subway Food',
            },
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'List of Pizza Toppings',
                'verbose_name_plural': 'List of Pizza Toppings',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('order', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time_of_order', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delivered', models.BooleanField()),
            ],
            options={
                'verbose_name': 'User Order List',
                'verbose_name_plural': 'User Order List',
            },
        ),
    ]
