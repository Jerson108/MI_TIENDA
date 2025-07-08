from django.db import models
import os

CATEGORIAS = [
    ('tecnologia', 'Tecnología'),
    ('muebles', 'Muebles'),
    ('moda', 'Moda'),
    ('decoracion', 'Decoración'),
    ('electrohogar', 'Electrohogar'),
    ('otras', 'Otras categorías'),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)  
    precio_proveedor = models.DecimalField(max_digits=10, decimal_places=2)
    precio_sugerido = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField("Descripción detallada", null=False, blank=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes_productos/')

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"

class Recurso(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='recursos')
    archivo = models.FileField(upload_to='recursos/')

    def __str__(self):
        return f"Recurso de {self.producto.nombre}"

    def nombre_archivo(self):
        return os.path.basename(self.archivo.name)