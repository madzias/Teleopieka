# Generated by Django 3.1.2 on 2020-10-22 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacjenci', '0006_zgloszenia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Zgloszenia',
            new_name='Zgloszenie',
        ),
    ]