# Generated by Django 4.0.5 on 2022-06-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
