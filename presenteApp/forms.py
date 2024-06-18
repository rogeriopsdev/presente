from django import forms
from presenteApp.models import Aluno, Turma

class AlunoForms(forms.ModelForm):
    class Meta:
        model=Aluno
        #fields= "__all__"
        fields= ['id_aluno','nome_aluno','matricula_aluno','cidade_aluno','foto_aluno']
        id_aluno =forms.CharField(label="Id do Aluno:")
        nome_aluno =forms.CharField(label='Nome do Aluno:')
        matricula_aluno =forms.CharField(label='Matrícula:')
        cidade_aluno =forms.CharField(label='Cidade:')