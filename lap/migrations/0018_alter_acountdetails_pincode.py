# Generated by Django 3.2.6 on 2021-09-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lap', '0017_acountdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acountdetails',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
