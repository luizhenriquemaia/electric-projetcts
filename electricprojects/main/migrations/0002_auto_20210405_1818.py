# Generated by Django 3.1.7 on 2021-04-05 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='a04NumberOfChargedConductors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('circuit_esqueme', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='a05CurrentCapacity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nominal_section', models.DecimalField(decimal_places=4, max_digits=12)),
                ('number_of_charged_conductors', models.IntegerField(default=1)),
                ('cable_type', models.CharField(max_length=20)),
                ('capacity', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='a06TemperatureCorrection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=20)),
                ('temperature', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='a08UndergroundCorrection',
            new_name='a07UndergroundCorrection',
        ),
        migrations.RemoveField(
            model_name='a04temperatureconductors',
            name='isolation_type',
        ),
        migrations.DeleteModel(
            name='a05NumberOfChargedConductors',
        ),
        migrations.RemoveField(
            model_name='a06currentcapacity',
            name='isolation_type',
        ),
        migrations.RemoveField(
            model_name='a06currentcapacity',
            name='reference_method',
        ),
        migrations.RemoveField(
            model_name='a07temperaturecorrection',
            name='isolation_type',
        ),
        migrations.AddField(
            model_name='a03isolationtype',
            name='max_temperature',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='a03isolationtype',
            name='overload_temperature',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='a03isolationtype',
            name='short_circuit_temperature',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='a09groupingcorrection',
            name='circuit_number',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='a04TemperatureConductors',
        ),
        migrations.DeleteModel(
            name='a06CurrentCapacity',
        ),
        migrations.DeleteModel(
            name='a07TemperatureCorrection',
        ),
        migrations.AddField(
            model_name='a06temperaturecorrection',
            name='isolation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.a03isolationtype'),
        ),
        migrations.AddField(
            model_name='a05currentcapacity',
            name='isolation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.a03isolationtype'),
        ),
        migrations.AddField(
            model_name='a05currentcapacity',
            name='reference_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.a01methodsref'),
        ),
    ]
