# Generated by Django 2.1.5 on 2019-10-22 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_new', models.BooleanField(default=True)),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True)),
                ('days', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Processing'), (3, 'Approved'), (4, 'Rejected'), (5, 'Cancelled')], default=1)),
                ('reason', models.TextField(max_length=200)),
                ('time_generated', models.DateTimeField(auto_now_add=True)),
                ('time_received', models.DateTimeField(null=True)),
                ('time_approved', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('original', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave_app.leave')),
            ],
            options={
                'ordering': ['time_generated'],
            },
        ),
    ]
