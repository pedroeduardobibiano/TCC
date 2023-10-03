from django.db import models


class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=200)    


class TCC(models.Model):
    id_tcc = models.AutoField(primary_key=True)
    nome_autores = models.CharField(max_length=255)
    ano = models.IntegerField()
    tema = models.CharField(max_length=255)
    descricao = models.TextField()
    curso_graduacao = models.CharField(max_length=255)
    arquivo_tcc = models.FileField(upload_to='tccs/')

    def __str__(self):
        return self.nome_autores
