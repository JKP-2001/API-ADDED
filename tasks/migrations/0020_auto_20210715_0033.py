# Generated by Django 3.2.4 on 2021-07-14 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20210715_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 14, 19, 3, 51, 552168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 14, 19, 3, 51, 620020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 14, 19, 3, 51, 620020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 14, 19, 3, 51, 620020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 14, 19, 3, 51, 620020, tzinfo=utc)),
        ),
    ]
