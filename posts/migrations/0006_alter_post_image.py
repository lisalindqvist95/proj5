# Generated by Django 3.2.19 on 2023-06-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_delete_postimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='../default_post_nhqkkf', upload_to='images/'),
        ),
    ]
