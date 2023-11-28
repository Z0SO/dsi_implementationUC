from django.db import IntegrityError
from django.shortcuts import redirect, render
# cuando ejecute esto me va a retornar un formulario, y tambien un formulario de autenticacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# usamos la clase proporcionada por django para crear un usuario
from django.contrib.auth.models import User

# para facilitar la autenticacion y el logueo login va a encargarse de crear la cookie del usuario1
from django.contrib.auth import login, logout, authenticate


from django.http import HttpResponse


from .forms import ProductosForm
from .models import Productos





# creacion de una vista home

def home(request):
    return render(request, 'home.html')


# -------------------------------------------------------------------------------
# parte autenticacion
# -------------------------------------------------------------------------------
# vista sign_up
# -------------------------------------------------------------------------------
def sign_up(request):
    if request.method == 'GET':     
        # si visita por get muestra el formulario
        return render(request,'sign-up.html', {'form_sign_up': UserCreationForm} )
    else:
        # la vista se ejecuta por un post
        # print(request.POST)
        
        if (request.POST['password1'] == request.POST['password2']):
            
            # para interactuar con la db se debe manejar posibles errores...
            try:
                # user_instance va a tener la instancia del usuario que quiere registrarse
                user_instance = User.objects.create_user(
                    username= request.POST['username'],
                    password= request.POST['password1']
                )
            
                # guardamos esa instancia
                user_instance.save()
        
                login(request, user_instance)
        
                return redirect('productos')
            except IntegrityError: 
                        
                return render(request,'sign-up.html', {
                    'error': 'Error: Usuario ya existente.',
                    'form_sign_up': UserCreationForm
                })                       
        else:
        
            return render(request,'sign-up.html', {
                'error': 'Error: Contraseñas incorrectas.',
                'form_sign_up': UserCreationForm
            })


# -------------------------------------------------------------------------------
# login

def log_in(request):
    if (request.method == 'GET'):
        return render(request, 'log-in.html', { 'form': AuthenticationForm })
    else:
        # caso de que venga por otro metodo http
        
        # se guarda en usuario el resultado de la autenticacion
        usuario = authenticate(request, 
            username= request.POST['username'],
            password= request.POST['password']
        )
        
        if usuario is None:
            return render(request,
                'log-in.html',
                { 'form': AuthenticationForm, 'error': 'Error: Usuario o contraseña incorrectos.' }
            )
        else:
            login(request, usuario)
            return redirect('lista_productos')
        

    


# -------------------------------------------------------------------------------
# logout

def sign_out(request):
    logout(request)
    return redirect('log-in')






# -------------------------------------------------------------------------------
# Parte de productos
# -------------------------------------------------------------------------------

def productos(request):

    return render(request, 'productos.html')


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:
                return render(request, 'registrarse.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registrarse.html', {"form": UserCreationForm, "error": "Passwords did not match."})



def crear_producto(request):
    if request.method == "GET":
        return render(request, 'crear_producto.html', {"form": ProductosForm})
    else:
        try:
            form = ProductosForm(request.POST, request.FILES)
            nuevo_producto = form.save(commit=False)
            nuevo_producto.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'Productos.html', {"form": ProductosForm, "error": "Error creando producto."})


def lista_productos(request):
    lista = Productos.objects.all
    return render(request, 'lista_productos.html', {"lista": lista})


def detalle_prod(request, prod_id):
    prod = Productos.objects.get(pk=prod_id)
    return render(request, 'detalle_producto.html' , {'prod': prod})