# Generated by Django 4.1.5 on 2023-02-12 21:15

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='about_company',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=company.models.image_upload),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]