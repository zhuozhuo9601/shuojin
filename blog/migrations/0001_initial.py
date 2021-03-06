# Generated by Django 2.0 on 2021-05-28 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='客户端名称')),
                ('fraction', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)], verbose_name='分数')),
            ],
            options={
                'verbose_name': '排行榜',
                'verbose_name_plural': '排行榜',
            },
        ),
        migrations.AlterUniqueTogether(
            name='leaderboard',
            unique_together={('name',)},
        ),
    ]
