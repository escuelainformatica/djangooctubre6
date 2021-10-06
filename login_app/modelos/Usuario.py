from django.db import models


# Create your models here.

class Usuario(models.Model):
    cuenta = models.CharField(max_length=50, primary_key=True)
    clave = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=200)

    def constructor(self,kwargs):
        self.cuenta=kwargs['cuenta']
        self.clave=kwargs['clave']
        self.nombre_completo=kwargs['nombre_completo']


    class Meta:
        db_table = 'usuarios'  # nombre de la tabla
        app_label='login_app'
