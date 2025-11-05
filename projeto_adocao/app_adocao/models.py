from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    ESPECIES = (
        ('gato', 'Gato'),
        ('cao', 'Cão'),
    )
    
    nome = models.CharField(max_length=15)
    idade = models.IntegerField()
    especie = models.CharField(choices=ESPECIES)
    descricao = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to='imgAnimal/')


    padrinho = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='animais_apadrinhados'
        )

    def __str__(self):
        return self.nome
    

