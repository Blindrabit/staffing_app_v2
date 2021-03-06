# Generated by Django 3.1 on 2020-09-30 14:29

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Busy', 'Busy')], max_length=10)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('manage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
