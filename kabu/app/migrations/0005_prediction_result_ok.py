# Generated by Django 3.0.3 on 2020-04-13 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200413_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='result_ok',
            field=models.BooleanField(default=False, null=True),
        ),
    ]