from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome