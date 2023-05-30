from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tecnico
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, AgregarTecnico
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login #Funciones que permite autenticar usuario

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
    #

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario 
    
    return render(request, 'app/contacto.html', data)


def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_solicitud(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario


    return render(request, 'app/producto/agregar.html', data)

def listar_solicitud(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_solicitud")
        data["form"] = formulario 
    
    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_solicitud")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al home 
            return redirect(to="home")
        data["form"] = formulario 


    return render(request, 'registration/registro.html', data)


def tecnico(request):
    data = {
        'form': AgregarTecnico()
    }

    if request.method == 'POST':
        formulario = AgregarTecnico(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tecnico agregado"
        else: 
            data["form"] = formulario


    return render(request, 'app/producto/agregar_tecnico.html', data)

def listar_tecnico(request):
    listartec = Tecnico.objects.all()
    data = {
        'listartec': listartec
    }
    return render(request, 'app/producto/listar_tecnicos.html', data)