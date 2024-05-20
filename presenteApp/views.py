from django.shortcuts import render
from presenteApp.forms import AlunoForms
from presenteApp.models import Aluno, Turma

def home(request):
    return render(request,'presente/home.html')

def cad_aluno(request):
    form =AlunoForms(request.POST)
    if request.method == "POST":
        form =AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form=AlunoForms()
    context = {'form':form}
    return render(request,'presente/cad_aluno.html', context)

def mostrar_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'presente/mostrar_aluno.html',{'alunos':alunos})