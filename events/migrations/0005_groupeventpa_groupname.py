# Generated by Django 3.1.3 on 2020-12-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201203_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupeventpa',
            name='groupname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
