# Generated by Django 3.1.3 on 2020-12-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_member_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='posnum',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]