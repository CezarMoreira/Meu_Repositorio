"""
criar uma fução que vai retornar uma http como resposta e adicionar o caminho ate esse arquivo html tem qu tar em uma pasta 
com o nome de templates tentro do app
"""




from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html')


