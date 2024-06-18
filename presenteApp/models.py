from django.db import models
import  PIL
from PIL import Image
# Create your models here.
class Aluno(models.Model):
    id_aluno =models.AutoField(primary_key=True)
    nome_aluno=models.CharField(max_length=200,blank=True, null=True)
    matricula_aluno=models.CharField(max_length=200,blank=True, null=True)
    cidade_aluno=models.CharField(max_length=200,blank=True, null=True)
    foto_aluno = models.ImageField(blank=True, null=False)

    def save(self):
        super().save()
        im = Image.open(self.foto_aluno.path)
        novo_tamanho = (40, 40)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_aluno.path)

    def foto_url(self):
        if self.foto_aluno and hasattr(self.foto_aluno, 'url'):
            return self.foto_aluno.url
        else:
            return self.nome_aluno

    def __str__(self):
        return self.nome_aluno

class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma=models.CharField(max_length=200, blank=True, null=True)
    aluno_turma = models.ForeignKey(Aluno,models.DO_NOTHING,db_column='id_aluno')

    def __str__(self):
        return self.nome_turma