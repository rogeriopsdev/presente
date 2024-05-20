from django import forms
from presenteApp.models import Aluno, Turma

class AlunoForms(forms.ModelForm):
    class Meta:
        model=Aluno
        fields= "__all__"