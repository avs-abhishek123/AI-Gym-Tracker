# Generated by Django 2.2.6 on 2019-11-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exID', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('primary', models.CharField(max_length=32)),
            ],
        ),
    ]
