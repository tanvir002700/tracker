# Generated by Django 2.0.4 on 2018-04-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_attandance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attandance',
            name='out_at',
            field=models.DateTimeField(null=True),
        ),
    ]
