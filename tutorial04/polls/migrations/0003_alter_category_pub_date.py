# Generated by Django 3.2.5 on 2022-03-18 10:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220318_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 10, 22, 50, 144183, tzinfo=utc)),
        ),
    ]
