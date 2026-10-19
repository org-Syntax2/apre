from django.db import models

class ArchivoSubido(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Archivo")
    archivo = models.FileField(upload_to='archivos_usuarios/', verbose_name="Archivo")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")

    def __str__(self):
        return self.titulo