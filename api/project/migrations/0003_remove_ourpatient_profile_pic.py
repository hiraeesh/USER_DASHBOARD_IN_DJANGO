# Generated by Django 4.0.3 on 2022-04-07 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_ourpatient_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourpatient',
            name='profile_pic',
        ),
    ]
