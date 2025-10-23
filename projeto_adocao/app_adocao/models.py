from django.db import models

class Animal(models.Model):
    ESPECIES = (
        ('gato', 'Gato'),
        ('cao', 'Cão'),
    )
    
    nome = models.CharField(max_length=15)
    idade = models.IntegerField()
    especie = models.CharField(choices=ESPECIES)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome
    

