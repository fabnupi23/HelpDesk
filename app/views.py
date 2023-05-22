from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos 
    }
    return render(request, 'app/home.html', data)

def contacto(request): 
    data = {
        'form': ContactoForm()
    }
    return render(request, 'app/contacto.html', data)

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formmulario 


def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario


    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/producto/listar.html', data)