# Generated by Django 3.2.13 on 2022-10-07 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=25)),
                ('last_name', models.CharField(default=None, max_length=25)),
                ('email', models.CharField(default=None, max_length=40)),
                ('street_address1', models.CharField(default=None, max_length=60)),
                ('street_address2', models.CharField(blank=True, default=None, max_length=60)),
                ('town_or_city', models.CharField(default=None, max_length=40)),
                ('county', models.CharField(default=None, max_length=40)),
                ('postcode', models.CharField(default=None, max_length=20)),
                ('phone_number', models.CharField(default=None, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
