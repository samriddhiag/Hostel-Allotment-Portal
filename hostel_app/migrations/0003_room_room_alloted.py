# Generated by Django 2.2.6 on 2019-10-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0002_auto_20191029_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_alloted',
            field=models.BooleanField(default=False),
        ),
    ]
