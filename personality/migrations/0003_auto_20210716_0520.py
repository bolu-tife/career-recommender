# Generated by Django 3.2.5 on 2021-07-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0002_auto_20210715_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_personality',
            name='Artistic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_personality',
            name='Conventional',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_personality',
            name='Enterprising',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_personality',
            name='Investigative',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_personality',
            name='Realistic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_personality',
            name='Social',
            field=models.FloatField(),
        ),
    ]