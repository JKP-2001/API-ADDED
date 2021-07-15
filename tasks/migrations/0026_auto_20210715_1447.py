# Generated by Django 3.2.4 on 2021-07-15 09:17

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_auto_20210715_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Credit',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='task',
            name='Marks_Of_Task',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='task',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='instructor_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 9, 17, 48, 924896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 9, 17, 48, 979749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 9, 17, 48, 979749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 9, 17, 48, 979749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 9, 17, 48, 979749, tzinfo=utc)),
        ),
    ]
