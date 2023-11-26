from django.db import IntegrityError
from django.shortcuts import redirect, render
# cuando ejecute esto me va a retornar un formulario, y tambien un formulario de autenticacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# usamos la clase proporcionada por django para crear un usuario
from django.contrib.auth.models import User

# para facilitar la autenticacion y el logueo login va a encargarse de crear la cookie del usuario1
from django.contrib.auth import login, logout, authenticate


from django.http import HttpResponse








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
            return redirect('home')
        

    


# -------------------------------------------------------------------------------
# logout

def sign_out(request):
    logout(request)
    return redirect('home')






# -------------------------------------------------------------------------------
# Parte de productos
# -------------------------------------------------------------------------------

def productos(request):

    return render(request, 'productos.html')






