from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome
    
class PerfilUtilizador(models.Model):
    usename = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    palavraPasse = models.CharField(max_length=20)
    confirmarPalavraPasse = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username