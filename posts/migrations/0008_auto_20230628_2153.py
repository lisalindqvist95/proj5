# Generated by Django 3.2.19 on 2023-06-28 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20230628_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='makeup',
        ),
        migrations.RemoveField(
            model_name='post',
            name='makeup_links',
        ),
    ]