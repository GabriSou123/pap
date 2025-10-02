from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(max_length=2)
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome