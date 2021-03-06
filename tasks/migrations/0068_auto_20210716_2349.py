# Generated by Django 3.2.4 on 2021-07-16 18:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0067_auto_20210716_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aeroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 200765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 200765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aiclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alcherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 190792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='astroclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 184808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 173838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='caclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 174835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 175832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 183811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 176830, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 177827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='edclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eeclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 185806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 178824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fncclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 187800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 179821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 180832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 192787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 181816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prakriticlub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 186803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roboticsclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 188798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sailclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 193784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 182814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 107016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 172840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 172840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 172840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 172840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 172840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='technicheclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 191790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ugclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 189795, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='CCDCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('event_type', models.CharField(choices=[('0', 'Organisation Activities')], default='0', max_length=40)),
                ('sub_event', models.CharField(choices=[('0', 'Select'), ('INTERNSHIP', 'INTERNSHIP'), ('PLACEMENT', 'PLACEMENT'), ('HACKATHONS', 'HACKATHONS'), ('PROJECTS', 'PROJECTS'), ('TALKS', 'TALKS'), ('OTHER', 'OTHER')], default='0', max_length=40)),
                ('ORGANISATION', models.CharField(choices=[('0', 'CCD ')], default='0', max_length=40)),
                ('target_batch', models.CharField(choices=[('0', 'Select'), ('All Batches', 'All Batches'), ('B.Tech', 'B.Tech'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 19', 'B.Tech 19'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 16', 'B.Tech 16'), ('B.Des', 'B.Des'), ('B.Des 20', 'B.Des 20'), ('B.Des 19', 'B.Des 19'), ('B.Des 18', 'B.Des 18'), ('B.Des 17', 'B.Des 17'), ('B.Des 16', 'B.Des 16'), ('M.Tech', 'M.Tech'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 16', 'M.Tech 16'), ('PhD', 'PhD'), ('PhD 20', 'PhD 20'), ('PhD 19', 'PhD 19'), ('PhD 18', 'PhD 18'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16')], default='Self', max_length=13)),
                ('target_branch', models.CharField(choices=[('0', 'Select'), ('All Branches', 'All Branches'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Chemistry', 'Chemistry'), ('Design', 'Design'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Engineering Physics', 'Engineering Physics'), ('Humanities and Social Sciences', 'Humanities and Social Sciences')], default='Self', max_length=45)),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('deadline', models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('time_from', models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('time_to', models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('remainder_date', models.DateField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('remainder_time', models.TimeField(default=datetime.datetime(2021, 7, 16, 18, 19, 2, 201763, tzinfo=utc))),
                ('remainder', models.CharField(choices=[('0', 'Select'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Week before', 'Week before'), ('Custom', 'Custom')], default='None', max_length=12)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
