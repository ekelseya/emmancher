# Generated by Django 3.1 on 2020-08-26 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patterns', '0005_auto_20200826_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]