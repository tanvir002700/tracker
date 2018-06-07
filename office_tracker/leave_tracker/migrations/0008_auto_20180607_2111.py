# Generated by Django 2.0.4 on 2018-06-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_tracker', '0007_auto_20180530_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='season',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userseason',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userseason',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
