# Generated by Django 4.2.1 on 2023-06-14 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='dt_cadatro',
            new_name='dt_cadastro',
        ),
    ]
