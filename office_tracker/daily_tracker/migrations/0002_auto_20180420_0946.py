# Generated by Django 2.0.4 on 2018-04-20 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daily_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attandance',
            name='enter_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attandance',
            name='out_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attandance',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
