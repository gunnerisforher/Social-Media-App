# Generated by Django 4.1.2 on 2022-10-29 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_page_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='active',
        ),
    ]