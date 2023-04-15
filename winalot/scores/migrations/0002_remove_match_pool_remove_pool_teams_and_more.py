# Generated by Django 4.2 on 2023-04-15 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='pool',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='teams',
        ),
        migrations.AddField(
            model_name='team',
            name='pool',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='scores.pool'),
            preserve_default=False,
        ),
    ]