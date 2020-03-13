from django.db import models


class Categorias(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "blog"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
