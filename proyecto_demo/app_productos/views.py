from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/inicio/')
        form = LoginForm()
        ctx = {'form':form}
        return render(request, 'login.html', ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def inicio_view(request):
    productos = Producto.objects.all()
    ctx = {'productos':productos}
    return render(request, 'index.html',ctx)

def nuevo_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        ctx = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('/inicio/')
    else:
        form = ProductoForm()
        ctx = {'form':form}
    return render(request, 'nuevo.html', ctx)

# def editar_stock_view(request, id):
#     p = Producto.objects.get(id=id)
#     if request.method == 'POST':
#         c = request.POST.get("cantidad")
#         p.cantidad = p.cantidad + int(c)
#         p.save()
#         form = StockForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.fk_producto = Producto.objects.get(pk = id)
#             instance.save()
#             return HttpResponseRedirect('/inicio/')
#     else:
#         form = StockForm()
    
#     return render(request, 'editar_stock.html', {'form':form})


def editar_stock_view(request, id):
    p = Producto.objects.get(id=id)
    if request.method == 'POST':
        c = request.POST.get("cantidad")
        p.cantidad = p.cantidad + int(c)
        p.save()
        s = Stock()
        m = request.POST.get("movimiento")
        s.cantidad = c
        s.movimiento = m
        s.fk_producto = Producto.objects.get(pk = id)
        s.save()
        return HttpResponseRedirect('/inicio/')
    else:
        form = StockForm()
    
    return render(request, 'editar_stock.html', {'form':form})

def editar_view(request, id):
    p = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio/')
        else:
            form = ProductoForm(intance=p)
    else:
        form = ProductoForm(instance=p)
    return render(request, 'editar.html', {'p':p,'form':form})

def eliminar_view(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/inicio/') 


def stock_view(request,id):
    stocks = Stock.objects.filter(fk_producto=id)
    ctx = {'stocks':stocks}
    return render(request, 'historial.html',ctx)



