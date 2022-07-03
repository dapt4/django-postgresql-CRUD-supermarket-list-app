from django.shortcuts import render,redirect
from .models import Item

# Create your views here.
def list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {"items": items})

def new(request):
    if request.method == 'POST':
        item = Item(
            nombre=request.POST["nombre"],
            cantidad=request.POST["cantidad"],
            hecho=False)
        item.save()
        return redirect('/')
    return render(request, 'new.html')

def edit(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item.nombre = request.POST["nombre"]
        item.cantidad = request.POST["cantidad"]
        item.save()
        return redirect('/')
    item = Item.objects.get(id=id)
    return render(request, 'edit.html', {"item": item})

def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('/')

def deactivate(request, id):
    item = Item.objects.get(id=id)
    item.hecho = True
    item.save()
    return redirect('/')
