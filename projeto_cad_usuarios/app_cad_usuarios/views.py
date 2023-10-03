from .models import usuario
from .models import TCC
from django.shortcuts import render, redirect
from .form import TCCForm


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    #salvando novos usuarios no bd
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    #exibindo user
    usuarios = {'usuarios': usuario.objects.all()}

    return render(request, 'usuarios/usuarios.html', usuarios)


def recipe(request):
    return render(request, 'usuarios/recipe.html')


#----------------------------------------------------------------------

#def lista_tccs(request):
#   tccs_ = TCC()
#   return render(request, 'usuarios/lista_tccs.html')

def cria_tcc(request):
    return render(request, 'usuarios/cadastra_tcc.html')


def tccs(request):
    #salvando novos trabalhos no bd
    novo_tcc = TCC()
    novo_tcc.nome_autores = request.POST.get('nome_autores')
    novo_tcc.ano = request.POST.get('ano')
    novo_tcc.tema = request.POST.get('tema')
    novo_tcc.descricao = request.POST.get('descricao')
    novo_tcc.curso_graduacao = request.POST.get('curso_graduacao')
    novo_tcc.arquivo_tcc = request.FILES.get('arquivo_tcc')
    novo_tcc.save()
    #exibindo user
    tccs = {'tccs': TCC.objects.all()}

    return render(request, 'usuarios/lista_tcc.html', tccs)


def edita_tcc(request, pk):
    tcc = TCC.objects.get(pk=pk)
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES, instance=tcc)
        if form.is_valid():
            form.save()
            return redirect('lista_tccs')
    else:
        form = TCCForm(instance=tcc)
    return render(request, 'usuarios/edita_tcc.html')


def exclui_tcc(request, pk):
    tcc = TCC.objects.get(pk=pk)
    tcc.delete()
    return redirect('lista_tccs')


from django.shortcuts import render

def cadastrar(request):
    # Coloque aqui a lógica que deseja executar ao acessar a rota 'nova_rota/'
    # Por exemplo, você pode realizar consultas ao banco de dados ou qualquer outra operação necessária.
    
    # Em seguida, você pode renderizar a página "cadastra_user.html"
    return render(request, 'usuarios/cadastra_user.html')


def login(request):
    # Coloque aqui a lógica que deseja executar ao acessar a rota 'nova_rota/'
    # Por exemplo, você pode realizar consultas ao banco de dados ou qualquer outra operação necessária.
    
    # Em seguida, você pode renderizar a página "cadastra_user.html"
    return render(request, 'usuarios/login.html')
