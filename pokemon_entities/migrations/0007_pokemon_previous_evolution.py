# Generated by Django 3.1.14 on 2022-04-18 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20220418_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon'),
        ),
    ]
