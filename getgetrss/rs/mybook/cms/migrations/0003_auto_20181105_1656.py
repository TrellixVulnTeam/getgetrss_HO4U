# Generated by Django 2.1.3 on 2018-11-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20181105_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='prirss',
            name='siteDetail',
            field=models.CharField(blank=True, max_length=255, verbose_name='詳細'),
        ),
        migrations.AddField(
            model_name='prirss',
            name='siteName',
            field=models.CharField(blank=True, max_length=255, verbose_name='サイト名'),
        ),
    ]
