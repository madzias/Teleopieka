# Generated by Django 3.1.2 on 2020-10-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacjenci', '0008_auto_20201022_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='zgloszenie',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
