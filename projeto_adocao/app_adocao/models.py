from django.db import models

class Animal(models.Model):
    ESPECIES = (
        ('gato', 'Gato'),
        ('cao', 'Cão'),
    )
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(choices=ESPECIES)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome
    


class PerfilUtilizador(models.Model):
    username = models.CharField(max_length=100, unique=True, default=' ')
    email = models.EmailField(unique=True)
    palavraPasse = models.CharField(max_length=100)

    def __str__(self):
        return self.username