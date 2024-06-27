from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'zapatos/index.html', context)


# def comprar(request):
#     context={}
#     return render(request, 'zapatos/comprar.html',context)

# def contacto(request):
#     context={}
#     return render(request, 'zapatos/contacto.html',context)

# def clima(request):
#     context={}
#     return render(request, 'zapatos/clima.html',context)

# def ingreso(request):
#     context={}
#     return render(request, 'zapatos/ingreso.html',context)

# def registro(request):
#     context={}
#     return render(request, 'zapatos/registro.html',context)

# def zapatillas(request):
#     context={}
#     return render(request, 'zapatos/zapatillas.html',context)

# def ingreso_view(request):
#     # Lógica para la vista de ingreso
#     context={}
#     return render(request, 'ingreso.html',context)  # Renderiza el template de ingreso.html
