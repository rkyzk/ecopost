# Generated by Django 3.2.20 on 2023-08-15 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
