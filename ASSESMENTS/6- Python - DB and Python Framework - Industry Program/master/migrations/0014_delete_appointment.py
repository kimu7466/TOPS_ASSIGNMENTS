# Generated by Django 5.0.1 on 2024-01-22 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_alter_appointment_patient_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]