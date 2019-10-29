# Generated by Django 2.2.6 on 2019-10-29 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='hostel',
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.Room'),
        ),
    ]
