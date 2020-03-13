from django.db import models


class Perguntas(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)
    descricao = models.TextField('Descrição', null=False)
    a = models.CharField('A', max_length=254, null=False)
    b = models.CharField('B', max_length=254, null=False)
    c = models.CharField('C', max_length=254, null=False)
    d = models.CharField('D', max_length=254, null=False)
    resposta = models.CharField('Resposta', max_length=254, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "questoes"