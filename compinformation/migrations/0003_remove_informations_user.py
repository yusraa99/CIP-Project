# Generated by Django 4.1.5 on 2023-01-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compinformation', '0002_informations_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informations',
            name='user',
        ),
    ]
