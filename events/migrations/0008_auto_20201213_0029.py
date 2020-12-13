# Generated by Django 3.1.3 on 2020-12-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20201213_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('phoneNum', models.CharField(blank=True, max_length=10)),
                ('whatsapp', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('type1', models.BooleanField(blank=True, default=False)),
                ('type2', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='mrmssattva',
            name='talent',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
