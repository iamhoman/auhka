# Generated by Django 3.1.2 on 2021-11-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0007_auto_20211121_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='sharing',
            field=models.CharField(max_length=10000),
        ),
    ]
