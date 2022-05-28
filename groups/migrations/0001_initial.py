# Generated by Django 4.0.4 on 2022-05-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('students_number', models.PositiveIntegerField()),
                ('teacher_last_name', models.CharField(max_length=100)),
            ],
        ),
    ]