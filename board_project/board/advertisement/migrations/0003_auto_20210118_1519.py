# Generated by Django 2.2 on 2021-01-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20210118_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
