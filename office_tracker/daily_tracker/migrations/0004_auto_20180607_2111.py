# Generated by Django 2.0.4 on 2018-06-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_tracker', '0003_attandance_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attandance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]