from django.shortcuts import render, get_object_or_404, redirect
from presenteApp.forms import AlunoForms
from presenteApp.models import Aluno, Turma

def home(request):
    return render(request,'presente/index.html')

def cad_aluno(request):
    form =AlunoForms(request.POST)
    alunos =Aluno.objects.all()

    if request.method == "POST":
        form =AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form=AlunoForms()
    context = {'form':form, 'alunos':alunos}
    return render(request,'presente/cad_aluno.html', context)


def editar_aluno(request,id):
    aluno =get_object_or_404(Aluno, pk =id)
    form =AlunoForms(instance=aluno)
    alunos = Aluno.objects.all()
    context ={'aluno':aluno, 'alunos':alunos, 'form':form}
    if request.method =="POST":
        form=AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('cad_aluno')
        else:
            return render(request,'presente/editar_aluno.html', context)
    else:
        return render(request, 'presente/editar_aluno.html', context)

def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno,pk=id)
    form = AlunoForms(instance=aluno)
    alunos = Aluno.objects.all()
    if request.method == "POST":
        aluno.delete()
        return redirect('cad_aluno')
    return render(request,'presente/deletar_aluno.html',{"alunos":alunos,
                                                         "aluno":aluno,
                                                         "form":form})


def mostrar_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'presente/mostrar_aluno.html',{'alunos':alunos})