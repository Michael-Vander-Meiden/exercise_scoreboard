# Generated by Django 2.1.1 on 2020-04-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_auto_20200404_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionexercise',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
