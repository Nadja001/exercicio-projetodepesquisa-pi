from django.db import models

# Create your models here.
class campus (models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)

class areaprojeto (models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

class pessoa (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    email = models.EmailField()
    is_professor = models.BooleanField()

class projeto (models.Model):
     nome = models.CharField(max_length=100)
     objetivo = models.TextField()
     resumo = models.TextField()
     pessoas = models.ManyToManyField(pessoa)
     area = models.ForeignKey(areaprojeto, on_delete=models.CASCADE)
     campus = models.ForeignKey(campus, on_delete=models.CASCADE)

class bolsa (models.Model):
    valor = models.FloatField()
    data_pagamento = models.DateField()
    bolsista = models.ForeignKey(pessoa, on_delete=models.CASCADE)
    projeto = models.ForeignKey(projeto, on_delete=models.CASCADE)

class meta (models.Model):
    descricao = models.CharField(max_length=200)
    detalhe = models.TextField()
    date_inicial = models.DateField()
    data_final = models.DateField()
    projeto = models.ForeignKey(projeto,on_delete=models.CASCADE)
