# Generated by Django 4.1.5 on 2023-01-18 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('compinformation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informations',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
    ]