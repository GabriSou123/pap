from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imgAnimal/', blank=False, null=False)

    def __str__(self):
        return self.nome