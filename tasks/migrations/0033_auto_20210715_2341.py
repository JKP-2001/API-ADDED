# Generated by Django 3.2.4 on 2021-07-15 18:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0032_auto_20210715_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bt',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bt',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ce',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ch',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 631144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 632144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 632144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 632144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 632144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cl',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 632144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='codingclub',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cse',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 633139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='des',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ece',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 634138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 635136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 635136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 635136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 635136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eee',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 635136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ma',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='me',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 636131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ph',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='swc',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 637129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 576293, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 630115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 630115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 630115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 630115, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ASTROCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('event_type', models.CharField(choices=[('0', 'CLUB RELATED ACTIVITIES')], default='Academic Activities', max_length=40)),
                ('sub_event', models.CharField(choices=[('0', 'Select'), ('MEETINGS', 'MEETINGS'), ('PARTIES', 'PARTIES'), ('TUTORIALS', 'TUTORIALS'), ('SHOWCASES', 'SHOWCASES')], default='0', max_length=40)),
                ('target_batch', models.CharField(choices=[('0', 'Select'), ('Self', 'Self'), ('All Batches', 'All Batches'), ('B.Tech', 'B.Tech'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 19', 'B.Tech 19'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 16', 'B.Tech 16'), ('B.Des', 'B.Des'), ('B.Des 20', 'B.Des 20'), ('B.Des 19', 'B.Des 19'), ('B.Des 18', 'B.Des 18'), ('B.Des 17', 'B.Des 17'), ('B.Des 16', 'B.Des 16'), ('M.Tech', 'M.Tech'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 16', 'M.Tech 16'), ('PhD', 'PhD'), ('PhD 20', 'PhD 20'), ('PhD 19', 'PhD 19'), ('PhD 18', 'PhD 18'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16')], default='Self', max_length=13)),
                ('target_branch', models.CharField(choices=[('0', 'ASTRONOMY CLUB'), ('Self', 'Self')], default='Self', max_length=45)),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 639123, tzinfo=utc))),
                ('time_from', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 639123, tzinfo=utc))),
                ('time_to', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 639123, tzinfo=utc))),
                ('remainder_date', models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 639123, tzinfo=utc))),
                ('remainder_time', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 639123, tzinfo=utc))),
                ('remainder', models.CharField(choices=[('0', 'Select'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Week before', 'Week before'), ('Custom', 'Custom')], default='None', max_length=12)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AEROCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('event_type', models.CharField(choices=[('0', 'CLUB RELATED ACTIVITIES')], default='Academic Activities', max_length=40)),
                ('sub_event', models.CharField(choices=[('0', 'Select'), ('MEETINGS', 'MEETINGS'), ('PARTIES', 'PARTIES'), ('TUTORIALS', 'TUTORIALS'), ('SHOWCASES', 'SHOWCASES')], default='0', max_length=40)),
                ('target_batch', models.CharField(choices=[('0', 'Select'), ('Self', 'Self'), ('All Batches', 'All Batches'), ('B.Tech', 'B.Tech'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 19', 'B.Tech 19'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 16', 'B.Tech 16'), ('B.Des', 'B.Des'), ('B.Des 20', 'B.Des 20'), ('B.Des 19', 'B.Des 19'), ('B.Des 18', 'B.Des 18'), ('B.Des 17', 'B.Des 17'), ('B.Des 16', 'B.Des 16'), ('M.Tech', 'M.Tech'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 16', 'M.Tech 16'), ('PhD', 'PhD'), ('PhD 20', 'PhD 20'), ('PhD 19', 'PhD 19'), ('PhD 18', 'PhD 18'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16')], default='Self', max_length=13)),
                ('target_branch', models.CharField(choices=[('0', 'AERO-MODELLING CLUB'), ('Self', 'Self')], default='Self', max_length=45)),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc))),
                ('time_from', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc))),
                ('time_to', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc))),
                ('remainder_date', models.DateField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc))),
                ('remainder_time', models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 11, 6, 638128, tzinfo=utc))),
                ('remainder', models.CharField(choices=[('0', 'Select'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Week before', 'Week before'), ('Custom', 'Custom')], default='None', max_length=12)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
