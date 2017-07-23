from django.db import models


# Create your models here.



class Etiqueta(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):

    nif = models.CharField(max_length=15)
    customer = models.CharField(max_length=150)

    def __str__(self):
        return  self.customer



class Tiket(models.Model):
    PRIORIDADES = (('A','Alta'),
                   ('M','Media'),
                   ('B','Baja'))
    TIPOS =(('I', 'Interno'),
            ('E', 'Externo'))

    nombre = models.CharField(max_length=150)
    tipologia = models.CharField(max_length=1, choices=TIPOS, default='E')
    prioridad = models.CharField(max_length=1, choices=PRIORIDADES, default='B')
    cliente = models.ForeignKey(Cliente)
    descripcion = models.TextField(blank=True, default='')
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.cliente + " " + self.tipologia





