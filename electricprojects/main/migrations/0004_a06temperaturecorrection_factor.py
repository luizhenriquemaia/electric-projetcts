# Generated by Django 3.1.7 on 2021-04-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210406_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='a06temperaturecorrection',
            name='factor',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=12),
        ),
    ]
