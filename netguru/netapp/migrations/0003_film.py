# Generated by Django 2.2.4 on 2019-08-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netapp', '0002_auto_20190829_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=30)),
                ('opis', models.CharField(max_length=300)),
                ('is_true', models.BooleanField(default=True)),
            ],
        ),
    ]
