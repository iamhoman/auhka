# Generated by Django 3.1.2 on 2021-11-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211122_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic04',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
