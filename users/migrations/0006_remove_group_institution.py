# Generated by Django 2.2.5 on 2019-09-26 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190802_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='institution',
        ),
    ]
