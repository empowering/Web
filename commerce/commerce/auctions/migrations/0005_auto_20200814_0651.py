# Generated by Django 3.1 on 2020-08-14 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200814_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='auto_increment_id',
            new_name='list_id',
        ),
    ]
