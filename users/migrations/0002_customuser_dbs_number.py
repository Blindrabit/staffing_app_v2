# Generated by Django 3.1 on 2020-09-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dbs_number',
            field=models.CharField(default='DBS_num_place', max_length=13),
        ),
    ]