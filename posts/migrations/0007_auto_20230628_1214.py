# Generated by Django 3.2.19 on 2023-06-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='makeup',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='makeup_links',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_nhqkkf', upload_to='images/'),
        ),
    ]