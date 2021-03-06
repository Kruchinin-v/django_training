# Generated by Django 2.2 on 2021-01-18 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
