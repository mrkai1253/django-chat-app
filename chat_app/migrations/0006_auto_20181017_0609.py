# Generated by Django 2.1 on 2018-10-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0005_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
