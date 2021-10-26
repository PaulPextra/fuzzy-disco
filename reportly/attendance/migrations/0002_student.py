# Generated by Django 3.2.8 on 2021-10-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=300)),
                ('date_of_birth', models.DateField()),
                ('about', models.TextField()),
            ],
        ),
    ]
