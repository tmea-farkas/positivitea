# Generated by Django 4.2 on 2025-01-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
