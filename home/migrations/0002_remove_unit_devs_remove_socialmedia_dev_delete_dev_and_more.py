# Generated by Django 5.0.4 on 2024-04-25 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='devs',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='dev',
        ),
        migrations.DeleteModel(
            name='Dev',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
    ]
