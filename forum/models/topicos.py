from django.db import models


class Topicos(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)
    conteudo = models.TextField('Conteudo', null=False)

    categorias = models.ManyToManyField('blog.Categorias')
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='topicos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "forum"