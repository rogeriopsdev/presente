from django.db import models

# Create your models here.
class Aluno(models.Model):
    id_aluno =models.AutoField(primary_key=True)
    nome_aluno=models.CharField(max_length=200,blank=True, null=True)
    matricula_aluno=models.CharField(max_length=200,blank=True, null=True)
    cidade_aluno=models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.nome_aluno

class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma=models.CharField(max_length=200, blank=True, null=True)
    aluno_turma = models.ForeignKey(Aluno,models.DO_NOTHING,db_column='id_aluno')

    def __str__(self):
        return self.nome_turma