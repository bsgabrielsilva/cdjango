from django.db import models


class Simulados(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)
    descricao = models.TextField('Descricao', null=False)

    categorias = models.ManyToManyField('blog.Categorias')
    perguntas = models.ManyToManyField('questoes.Perguntas')
    nivel = models.ForeignKey('questoes.Niveis', on_delete=models.PROTECT, related_name='simulados')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "questoes"
