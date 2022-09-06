from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    typeid = models.ForeignKey('TipoCuentas', models.DO_NOTHING, db_column='typeId')

    class Meta:
        db_table = 'cuenta'

class TipoCuentas(models.Model):
    tipoid = models.AutoField(db_column='TipoId', primary_key=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        db_table = 'tipo_cuentas'