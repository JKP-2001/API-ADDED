# Generated by Django 3.2.4 on 2021-07-16 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0064_auto_20210716_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 82448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 82448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 82448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 82448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 77461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 69483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 70483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 76433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 71480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 72475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 78459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 73480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 74469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 79458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 80454, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 75468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 16629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 68488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 82448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 83446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 14, 42, 4, 81453, tzinfo=utc)),
        ),
    ]
