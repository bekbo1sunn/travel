# Generated by Django 4.2.1 on 2023-06-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_tiket_departure_alter_country_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiket',
            name='departure',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='main.country'),
            preserve_default=False,
        ),
    ]
