# Generated by Django 4.2 on 2023-04-19 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0009_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
