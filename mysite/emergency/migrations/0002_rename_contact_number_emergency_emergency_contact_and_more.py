# Generated by Django 5.1.3 on 2025-01-05 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergency',
            old_name='contact_number',
            new_name='emergency_contact',
        ),
        migrations.RenameField(
            model_name='emergency',
            old_name='patient_name',
            new_name='emergency_name',
        ),
    ]
