from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion') #Se ingresa la fecha cuando se crea
    updated =  models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion') #Se actualiza la fecha cuando se modifica
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]
    
    def __str__(self) :
        return self.title