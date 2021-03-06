# Generated by Django 3.1.3 on 2020-12-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20201203_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupeventpa',
            options={'verbose_name_plural': 'Group PA Form'},
        ),
        migrations.AlterModelOptions(
            name='solosinging',
            options={'verbose_name_plural': 'Solo PA Form'},
        ),
        migrations.AddField(
            model_name='groupeventpa',
            name='college',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='groupeventpa',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='groupeventpa',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='solosinging',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='groupeventpa',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
