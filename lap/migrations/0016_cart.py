# Generated by Django 3.2.6 on 2021-09-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lap', '0015_allproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('modelno', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=800)),
                ('category', models.CharField(max_length=150)),
                ('image', models.ImageField(default='', upload_to='cart/pictures')),
                ('status', models.CharField(default='unordered', max_length=100)),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]