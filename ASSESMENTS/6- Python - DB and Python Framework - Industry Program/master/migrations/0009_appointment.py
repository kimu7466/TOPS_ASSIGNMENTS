# Generated by Django 5.0.1 on 2024-01-22 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_signed_up_gender_alter_signed_up_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('additional_info', models.TextField(blank=True)),
                ('approval_status', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='master.signed_up')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.signed_up')),
            ],
        ),
    ]