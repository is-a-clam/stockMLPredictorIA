# Generated by Django 3.2 on 2021-09-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0015_alter_userprofile_dash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dash',
            field=models.JSONField(default=dict),
        ),
    ]
