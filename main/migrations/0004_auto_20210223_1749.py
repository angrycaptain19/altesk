# Generated by Django 3.1.6 on 2021-02-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210223_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentfile',
            name='category',
            field=models.ManyToManyField(to='main.Content'),
        ),
    ]
