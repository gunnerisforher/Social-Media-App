# Generated by Django 4.1.2 on 2022-10-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_like_comment_alter_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='posts/%y/%m/%d'),
        ),
    ]
