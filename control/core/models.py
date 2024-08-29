from django.db import models


#TASK MODEL


class Task(models.Model):
    STATE_CHOICES = (
        ('PEN', 'PENDIENTE'),
        ('PRO', 'PROCESADO'),
        ('FIN', 'FINALIZADO'),
        ('CAN', 'CANCELADO'),
    )
    titulo = models.CharField(max_length=200)
    estado = models.BooleanField(default=False, blank=True, null=True)
    accion = models.CharField(max_length=3, choices=STATE_CHOICES, verbose_name='accion', db_column='accion', blank=True, null=True)
    f_inicio = models.DateField(verbose_name='fecha inicial', db_column= 'f_inicio', blank=True, null=True)
    f_fin = models.DateField(verbose_name='fecha fin', db_column= 'f_fin', blank=True, null=True)

    def __str__(self):
        return self.title
    