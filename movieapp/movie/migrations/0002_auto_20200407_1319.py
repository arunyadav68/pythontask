# Generated by Django 3.0.5 on 2020-04-07 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='movies',
            new_name='movie',
        ),
    ]
