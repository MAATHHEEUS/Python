# Generated by Django 5.0.6 on 2024-05-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]