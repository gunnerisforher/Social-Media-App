# Generated by Django 4.1.2 on 2022-10-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequests',
            name='accepted',
        ),
    ]
