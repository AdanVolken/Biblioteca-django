
from django.shortcuts import render,redirect
from biblioteca.models import LibroCompra,Cliente,Compra,Genero
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
import stripe
from config import settings

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
    compras_usuario = Compra.objects.filter(cliente=request.user.cliente, descargado=True)
    libros_descargados = [compra.libro for compra in compras_usuario]

    return render(request, 'miLibro.html', {'libros_descargados': libros_descargados})

def libro_id(request, id):
    libro = LibroCompra.objects.get(id = id)

    return render(request, 'libro_id.html' ,{
        'libro': libro
    })



stripe.api_key = 'sk_test_51ORfZLHv2WvnwEKoM5xUkuBgl8cr8JmQEFCJrMcPxwYKqxAF2vj2u92geVi8Vo2Zrc1PS2MIWWsj7ayAyFLRX3Ks00vtr11vzv'
dominio = 'http://localhost:8000'

def pagos(request, id):
    
    checkout_session = stripe.checkout.Session.create(
        
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1ORgRBHv2WvnwEKo6vb36qm2',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{dominio}/pagado/{id}',
            cancel_url=dominio,
        )
    return redirect(checkout_session.url) 

def pagado (request,id):
    libro = LibroCompra.objects.get(id=id)

    compra = Compra.objects.get(cliente=request.user.cliente, libro=libro)
    compra.descargado = True
    compra.save()

    return render(request, 'pagado.html',{'libro': libro})