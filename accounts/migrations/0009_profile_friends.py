# Generated by Django 4.1.2 on 2022-10-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.profile'),
        ),
    ]
