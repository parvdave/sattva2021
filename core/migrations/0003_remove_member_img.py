# Generated by Django 3.1.3 on 2020-12-07 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_member_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='img',
        ),
    ]
