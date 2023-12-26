
from django.shortcuts import render,redirect
from biblioteca.models import LibroCompra,Cliente,Compra,Genero
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
def home(request):
    libro = LibroCompra.objects.all()
    return render(request, 'home.html', {
        "libros": libro
    })

def sesion(request):
    if request.method == 'POST':
            user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('cliente')
            else:
                return redirect('sesion', {
                    "error": "Usuario o Contraseña Incorrecta"})  # Redirigir de nuevo a la página de inicio de sesión
    else:  # Método GET
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except :
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    

def biblioteca(request):
    return render (request, 'biblioteca.html')

@login_required
def mi_libro(request):
    return render(request, 'miLibro.html')

def libro_id(request, id):
    libro = LibroCompra.objects.get(id = id)

    return render(request, 'libro_id.html' ,{
        'libro': libro
    })