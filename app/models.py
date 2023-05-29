from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=100)
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    

opciones_consultas =[
    [0, "Asesoría Técnica"],
    [1, "Concepto Técnico"],
    [2, "Instalación Equipo"],
    [3, "Instalación Hardware"],
    [4, "Instalación Software"],
    [5, "Instalación Preiféricos"],
    [6, "Mantenimiento Preventivo"],
    [7, "Revisión equipo de Computo"],
    [8, "Revisión Periferico"],
    [9, "Videoconferencia"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre