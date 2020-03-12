from django.db import models


class Postagens(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)
    resumo = models.TextField('Resumo', null=False)
    conteudo = models.TextField('Conteúdo', null=False)

    categorias = models.ManyToManyField('blog.Categorias')
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='postagens')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "blog"
