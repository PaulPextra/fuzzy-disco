# Generated by Django 3.2.9 on 2021-11-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(default=10),
        ),
    ]
