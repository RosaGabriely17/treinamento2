from django.db import models

class Usuario(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

class Tarefas(models.Model):

    STATUS_CHOICES = {
        ('A_FAZER', 'A Fazer'),
        ('FAZENDO', 'Fazendo'),
        ('PRONTO', 'Pronto'),
    }

    PRIORIDADE_CHOICES = {
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    }


    descricao = models.CharField(max_length=300)
    setor = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prioridade = models.CharField(choices=PRIORIDADE_CHOICES)
    status = models.CharField(choices=STATUS_CHOICES, default='A Fazer')



