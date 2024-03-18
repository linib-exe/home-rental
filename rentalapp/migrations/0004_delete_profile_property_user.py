# Generated by Django 4.2.11 on 2024-03-18 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentalapp', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]