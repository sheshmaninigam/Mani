# Generated by Django 4.2.4 on 2023-09-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
    ]
