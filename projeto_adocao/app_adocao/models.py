from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imgAnimal/')

    def __str__(self):
        return self.nome
    
class PerfilUtilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def criar_ou_atualizar_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUtilizador.objects.create(user=instance)
    else:
        instance.perfilutilizador.save()