# Generated by Django 3.1.3 on 2020-12-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_groupeventpa_groupname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('age', models.IntegerField(default=2, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('address', models.TextField(blank=True, max_length=300)),
                ('phoneNum', models.CharField(blank=True, max_length=10)),
                ('whatsapp', models.CharField(blank=True, max_length=10)),
                ('contacted', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='rules',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
