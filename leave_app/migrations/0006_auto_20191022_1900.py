# Generated by Django 2.1.5 on 2019-10-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0005_auto_20191022_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_model',
            name='dept_name',
            field=models.IntegerField(choices=[(0, 'CSE'), (1, 'IT'), (2, 'ECE'), (3, 'ME'), (4, 'TEX'), (5, 'BBA')]),
        ),
    ]