# Generated by Django 5.1.3 on 2025-01-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_name_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank='true', max_length=200, null='true'),
        ),
    ]
