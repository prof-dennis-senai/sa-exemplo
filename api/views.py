from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Pessoa, Produto

# Create your views here.
@csrf_exempt
def obter_todas_pessoas(request):
    if request.POST:
        data:dict = request.POST
        nome=data.get("nome")
        idade=data.get("idade")
        email=data.get("email")
        if all((nome, idade, email)):
            Pessoa.objects.create(nome=nome,idade=idade,email=email)
            return JsonResponse({"menssagem":"Pessoa criado com sucesso","data": {"nome":nome,"idade":idade,"email":email}}, safe=False)
        else:
            return JsonResponse({"menssagem":"Pessoa não foi criada"}, safe=False)
        data = []
        
    else:
        data = [{
                    "nome":row.nome,
                    "idade":row.idade,
                    "email":row.email
                } for row in Pessoa.objects.all()] 
    
    return JsonResponse(data, safe=False)

@csrf_exempt
def obter_todos_produtos(request):
    
    data = [{
                "titulo":row.titulo,
                "preco":row.preco
            } for row in Produto.objects.all()] 
    
    return JsonResponse(data, safe=False)