# Generated by Django 4.1.5 on 2023-01-17 21:28

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to=projects.models.image_upload)),
                ('open_at', models.DateTimeField(auto_now=True)),
                ('goal', models.CharField(max_length=50)),
                ('minimum_investment', models.CharField(max_length=50)),
                ('open_type', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close'), ('Coming Soon', 'Coming Soon')], max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]