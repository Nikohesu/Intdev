from django.db import models

class tipos_de_usuarios(models.Model):
    nombre = models.CharField(max_length=15)
    
    def __str__ (self):
        return self.nombre
    
class tipo_pagos (models.Model):
    tipo_de_pago = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo_de_pago
    
class tipos_de_planes (models.Model):
    tipo_de_plan= models.CharField(max_length=15)
    duracion_meses = models.DurationField()
    valor = models.FloatField()
    id_pago = models.ForeignKey(tipo_pagos, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.tipo_de_plan

class usuarios (models.Model):
    correo = models.EmailField(max_length=254)
    nombre = models.CharField(max_length=15)
    telefono = models.CharField(max_length=10)
    contraseña = models.CharField (max_length=16)
    id_tipo_usuario = models.ForeignKey(tipos_de_usuarios,on_delete=models.CASCADE)
    id_plan = models.ForeignKey(tipos_de_planes,on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nombre
    


    


class sugerencias (models.Model):
    calificacion = models.IntegerField()
    comentario = models.TextField()
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.id_usuario
    
class gastos (models.Model):
    valor = models.IntegerField()
    fecha = models.DateField()
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.valor
class ingresos (models.Model):
    valor = models.IntegerField()
    fecha = models.DateField()
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.valor
    
class categoria_gastos (models.Model):
    nombre_g = models.CharField(max_length=15)
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_g
    
class ingresos (models.Model):
    nombre_i = models.CharField(max_length=15)
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_i
    
    
    
    
    
    
    
    
    
    
    
    
    