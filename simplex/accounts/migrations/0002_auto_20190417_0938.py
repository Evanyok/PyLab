# Generated by Django 2.2 on 2019-04-17 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='TUser',
        ),
    ]