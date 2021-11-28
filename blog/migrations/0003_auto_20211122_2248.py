# Generated by Django 3.1.2 on 2021-11-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pic',
            new_name='pic01',
        ),
        migrations.AddField(
            model_name='post',
            name='pic02',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='pic03',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]