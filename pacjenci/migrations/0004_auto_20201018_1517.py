# Generated by Django 3.1.2 on 2020-10-18 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacjenci', '0003_dom_pacjent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asystent',
            options={'verbose_name_plural': 'Asystenci'},
        ),
        migrations.AlterModelOptions(
            name='dom',
            options={'verbose_name_plural': 'Domy sąsiedzkie'},
        ),
        migrations.AlterModelOptions(
            name='pacjent',
            options={'verbose_name_plural': 'Pacjenci'},
        ),
        migrations.AlterField(
            model_name='asystent',
            name='dom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacjenci.dom'),
        ),
    ]