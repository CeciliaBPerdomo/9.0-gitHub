from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Hola Mundo!, bienvenida a mi aplicación de Django"}
    return render(request, "myapp/index.html", context)