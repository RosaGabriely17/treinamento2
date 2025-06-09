from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Tarefas


def cadastroUsuarios(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Usuario.objects.create(name=name, email=email)
        return redirect('cadastroUsuarios')
    else:
        return render(request, 'cadastroUsuarios.html')

def cadastroTarefas(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        id_usuario = request.POST.get('usuario')
        prioridade = request.POST.get('prioridade')
        usuario = Usuario.objects.get(id=id_usuario)
        Tarefas.objects.create(descricao=descricao, setor=setor, usuario=usuario, prioridade=prioridade)
        return redirect('gerenciarTarefas')
    else:
        return render(request, 'cadastroTarefas.html',{'usuarios':usuarios})
    

def gerenciarTarefas(request):
    tarefas = Tarefas.objects.all()
    tarefas_por_status = {
        'afazer': tarefas.filter(status='A Fazer'),
        'fazendo': tarefas.filter(status='Fazendo'),
        'pronto': tarefas.filter(status='Pronto'),
    }
    return render(request, 'gerenciarTarefas.html', {'tarefas': tarefas_por_status})

def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, id=id)
    if request.method == "POST":
        tarefa.descricao = request.POST['descricao']
        tarefa.setor = request.POST['setor']
        tarefa.prioridade = request.POST['prioridade']
        tarefa.status = request.POST['status']
        tarefa.vinculado_a_id = request.POST['vinculado_a']
        tarefa.save()
        return redirect('gerenciarTarefas')
    usuarios = Usuario.objects.all()
    return render(request, 'editarTarefa.html', {'tarefa': tarefa, 'usuarios': usuarios})

def excluirTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, id=id)
    tarefa.delete()
    return redirect('gerenciarTarefas')

def alterarStatus(request, id):
    tarefa = get_object_or_404(Tarefas, id=id)
    if request.method == "POST":
        tarefa.status = request.POST['status']
        tarefa.save()
    return redirect('gerenciarTarefas')