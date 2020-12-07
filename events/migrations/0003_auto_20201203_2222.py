# Generated by Django 3.1.3 on 2020-12-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201203_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupEventPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='solosinging',
            options={'verbose_name_plural': 'Solo Singing Form'},
        ),
        migrations.AddField(
            model_name='event',
            name='eventType',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='eventslug',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='solosinging',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]