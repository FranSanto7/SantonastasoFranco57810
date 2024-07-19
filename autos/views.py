from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from .forms import AutoForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        elif 'logout' in request.POST:
            logout(request)
            return redirect('home')
    return render(request, 'autos/home.html')

def auto_detail(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/auto_detail.html', {'auto': auto})

def auto_create(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutoForm()
    return render(request, 'autos/auto_form.html', {'form': form})

def auto_edit(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('auto_detail', id=id)
    else:
        form = AutoForm(instance=auto)
    return render(request, 'autos/auto_form.html', {'form': form})

def auto_delete(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('home')
    return render(request, 'autos/auto_confirm_delete.html', {'auto': auto})

def buscar_autos(request):
    marca = request.GET.get('marca', '')
    modelo = request.GET.get('modelo', '')
    autos = Auto.objects.filter(marca__icontains=marca, modelo__icontains=modelo)
    return render(request, 'autos/buscar_autos.html', {'autos': autos, 'marca': marca, 'modelo': modelo})