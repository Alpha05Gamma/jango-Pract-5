from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.http import Http404
from .models import Enemy, Boss, NPC, Item, Weapon
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    enemys = Enemy.objects.order_by('id')
    context = {'enemys' :enemys}

    return render(request, 'users\index.html', context)

def AstelPage(request):    
    bosses = Boss.objects.order_by('id')
    context = {'bosses' :bosses}

    return render(request, 'protoWiki11\AstelPage.html', context)

def FirePotPage(request):
    items = Item.objects.order_by('id')
    context = {'items' :items}

    return render(request, 'protoWiki11\FirePotPage.html', context)

def MelinasPage(request):
    npces = NPC.objects.order_by('id')
    context = {'npces' :npces}

    return render(request, 'protoWiki11\MelinasPage.html', context)

def WeaponPage(request):
    weapons = Weapon.objects.order_by('id')
    context = {'weapons' :weapons}

    return render(request, 'protoWiki11\WeaponPage.html', context)



def header(request):
    return render(request, '\includes\header.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def create_view(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form =PlayerForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    
def person_view(request):
    dataset = Player.objects.all()
    return render(request, 'listview.html', {'dataset': dataset})
 
def person_detail_view(request, id):
    try:
        data = Player.objects.get(id=id)
    except PlayerForm.DoesNotExist:
        raise Http404('Такого не существует')
 
    return render(request, 'detailview.html', {'data': data})

def update_view(request, id):
    try:
        old_data = get_object_or_404(Player, id=id)
    except Exception:
        raise Http404('Такого не существует')
    
    if request.method =='POST':
        form = PlayerForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/{id}')
    else:
        form = PlayerForm(instance = old_data)
        context ={
            'form':form
        }
        return render(request, 'update.html', context)
    

def delete_view(request, id):
    try:
        data = get_object_or_404(Player, id=id)
    except Exception:
        raise Http404('Такого не существует')
 
    if request.method == 'POST':
        data.delete()
        return redirect('view')
    else:
        return render(request, 'delete.html')