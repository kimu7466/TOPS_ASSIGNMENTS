# Generated by Django 5.0.1 on 2024-01-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_signed_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='signed_up',
            name='credentials_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='signed_up',
            name='is_activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='signed_up',
            name='password',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
