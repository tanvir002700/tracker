# Generated by Django 2.0.4 on 2018-04-20 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily_attandance', '0003_attandance_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attandance',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
