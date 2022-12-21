"""
aqui na url do app importar:from django.urls import path  e from recipes.views import  home  
depois adicionar o urlpatterns = [
    
                        path('', home),
    
    
                      ]
e depois ir la para views.py
"""


from django.urls import path
from recipes.views import  home





 
urlpatterns = [
    
    path('', home),
    
    
   
]