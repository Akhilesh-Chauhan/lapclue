# Generated by Django 3.2.6 on 2021-09-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lap', '0014_delete_companies'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
                ('modelno', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='laptopimages')),
                ('category', models.CharField(choices=[('Gaming', 'Gaming'), ('Business', 'Business'), ('Professional', 'Professional'), ('Student', 'Student')], max_length=20)),
                ('price', models.CharField(max_length=30)),
                ('screen', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('graphics', models.CharField(max_length=200)),
                ('memory', models.CharField(blank=True, max_length=50)),
                ('storage', models.CharField(blank=True, max_length=100)),
                ('ioports', models.CharField(blank=True, max_length=200)),
                ('dimensions', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]