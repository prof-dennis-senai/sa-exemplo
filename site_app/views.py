from django.shortcuts import render, redirect

from site_app.models import Pessoa
dados = []

# Create your views here.
def home(request):
    nome = ""
    email = ""
    idade = 0
    dados = Pessoa.objects.all().order_by('-id')[:10] 

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade = request.POST.get("idade",0)
        Pessoa.objects.create(nome=nome,email=email,idade=idade)
        
    return render(request, "site_app/global/home.html", context={"dados":dados,"nome":nome,"email":email})

def criar(request):
    nome = ""
    email = ""
    idade = 0

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        idade = request.POST.get("idade",0)
        Pessoa.objects.create(nome=nome,email=email,idade=idade)
        
    return render(request, "site_app/partials/criar.html", context={"nome":nome,"email":email,"idade":idade})



def pesquisar(request):
    pessoa = {}
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()

    return render(request, "site_app/partials/pesquisar.html",pessoa)

def deletar(request,id=0):
    pessoa = {}

    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect(deletar)
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()
    return render(request, "site_app/partials/deletar.html", context=pessoa)

def atualizar(request,id=0):
    pessoa = {}
    if id:   
        if request.POST:
            pessoa = Pessoa.objects.get(id=id)
            pessoa.nome = request.POST.get("nome",pessoa.nome)
            pessoa.email = request.POST.get("email",pessoa.email)
            pessoa.idade = request.POST.get("idade",pessoa.idade)

            pessoa.save()

            return redirect(atualizar)
        
        pessoa["pessoa"] = Pessoa.objects.get(id=id)
        return render(request, "site_app/partials/update.html",pessoa)
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()

    return render(request, "site_app/partials/atualizar.html", context=pessoa)









### Excluir
def produtos(request):
    return render(request, "site_app/global/produtos.html")

def precos(request, id=0):
    dados = [
        {
            "id":1,
            "titulo" : "X bacon",
            "descricao" : "Double Bacon, Dois super hamburgueres de 100g, queijo cheddar, cebola caramelizada",
            "img": "https://img.restaurantguru.com/r483-ItaGastroPub-burger-2021-09.jpg"
        },
        {
            "id":2,
            "titulo" : "X Galinha",
            "descricao" : "Dois super hamburgueres de Frango 100g, queijo Mussarela e tomate",
            "img": "https://imagens.jotaja.com/produtos/6dcc15bd-80cb-426f-acd7-2f52de6f75cb.jpg"
        },
        {
            "id":3,
            "titulo" : "Mafioso",
            "descricao" : "Dois super hamburgueres de 100g, queijo Mussarela, cebola caramelizada e Jack Daniels",
            "img": "https://img.restaurantguru.com/rcb4-burger-ItaGastroPub.jpg"
        },
    ]

    if id:
        # import ipdb; ipdb.set_trace()
        dados = [dados[id - 1]]
    return render(request, "site_app/global/precos.html", context={"dados":dados})