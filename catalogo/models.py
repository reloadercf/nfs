from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(max_length=100)

    def __str__(self):
        return self.categoria

class Producto(models.Model):

    titulo=models.CharField(max_length=100)
    categorias = models.ManyToManyField(Categoria, related_name='categorias')
    descargable=models.FileField(upload_to='exp/', null=True, blank=True)
    descripcion=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.titulo