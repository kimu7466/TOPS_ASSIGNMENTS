# Generated by Django 5.0.1 on 2024-01-22 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_id',
        ),
    ]
