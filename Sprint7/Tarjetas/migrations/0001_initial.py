# Generated by Django 4.1.1 on 2022-09-06 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0002_tipoclientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcasTarjetas',
            fields=[
                ('marcaid', models.AutoField(db_column='MarcaId', primary_key=True, serialize=False)),
                ('marca', models.TextField(db_column='Marca')),
            ],
            options={
                'db_table': 'marcas_tarjetas',
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('mov_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField(blank=True, null=True)),
                ('mov_total', models.IntegerField(blank=True, null=True)),
                ('mov_type', models.TextField(blank=True, null=True)),
                ('mov_datetime', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
            },
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('tarjetaid', models.AutoField(db_column='TarjetaId', primary_key=True, serialize=False)),
                ('numero', models.IntegerField(db_column='Numero')),
                ('cvv', models.IntegerField(db_column='CVV')),
                ('fechaotorgamiento', models.TextField(db_column='FechaOtorgamiento')),
                ('fechaexpiracion', models.TextField(db_column='FechaExpiracion')),
                ('tipo', models.TextField(db_column='Tipo')),
                ('customerid', models.ForeignKey(db_column='CustomerId', on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.cliente')),
                ('marcaid', models.ForeignKey(db_column='MarcaId', on_delete=django.db.models.deletion.DO_NOTHING, to='Tarjetas.marcastarjetas')),
            ],
            options={
                'db_table': 'tarjetas',
            },
        ),
    ]
