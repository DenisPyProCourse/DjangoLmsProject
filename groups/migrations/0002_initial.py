# Generated by Django 4.0.4 on 2022-06-11 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('teachers', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headman_group', to='students.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='headteacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headteacher_group', to='teachers.teacher'),
        ),
    ]
