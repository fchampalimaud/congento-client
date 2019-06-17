# Generated by Django 2.1.8 on 2019-06-17 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190617_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='users.Group'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='Designates whether the user has permissions to manage all group entries in the database.', verbose_name='manager'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_responsible',
            field=models.BooleanField(default=False, help_text='Designates whether the user is the POC.', verbose_name='responsible'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL),
        ),
    ]