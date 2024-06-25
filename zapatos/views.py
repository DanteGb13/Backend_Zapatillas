from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def comprar(request):
    return render(request, 'zapatos/comprar.html')

def contacto(request):
    return render(request, 'zapatos/contacto.html')

def clima(request):
    return render(request, 'zapatos/clima.html')

def ingreso(request):
    return render(request, 'zapatos/ingreso.html')

def registro(request):
    return render(request, 'zapatos/registro.html')

def zapatillas(request):
    return render(request, 'zapatos/zapatillas.html')

def ingreso_view(request):
    # Lógica para la vista de ingreso
    return render(request, 'ingreso.html')  # Renderiza el template de ingreso.html
