# Generated by Django 3.1.4 on 2021-01-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldata',
            name='disc',
            field=models.TextField(max_length=1000),
        ),
    ]