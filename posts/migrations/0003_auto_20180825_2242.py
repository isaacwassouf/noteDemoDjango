# Generated by Django 2.0.6 on 2018-08-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180819_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='lock_password',
            field=models.CharField(default='', max_length=255),
        ),
    ]