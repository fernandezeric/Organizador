# Generated by Django 3.0.6 on 2020-05-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hogar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_administrador',
            field=models.BooleanField(default=True),
        ),
    ]
