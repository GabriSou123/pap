from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome
    

class PerfilUtilizador(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    palavraPasse = models.CharField(max_length=50)
    confirmarPalavraPasse = models.CharField(max_length=50)

    def __str__(self):
        return self.username
