# Generated by Django 3.2.18 on 2023-05-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('animals', 'Protecting animals'), ('aquatic system', 'Protecting the aquatic system'), ('saving soil & trees', 'Protecting soil & trees'), ('saving resources', 'Saving resources'), ('eco-conscious diet', 'Eco-conscious diet'), ('others', 'Others')], default='others', max_length=30),
        ),
    ]
