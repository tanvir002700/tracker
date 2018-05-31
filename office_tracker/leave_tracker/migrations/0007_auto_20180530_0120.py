# Generated by Django 2.0.4 on 2018-05-29 19:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave_tracker', '0006_leave_user_season'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userseason',
            unique_together={('user', 'season')},
        ),
    ]