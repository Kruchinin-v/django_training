# Generated by Django 2.2 on 2021-01-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0004_auto_20210118_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
