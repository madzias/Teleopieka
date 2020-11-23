from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import *
# Create your views here.

from .models import *
from .forms import *
from .filters import *
from .decorators import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='asystent')
            user.groups.add(group)
            Asystent.objects.create(
                user=user
            )

            messages.success(request, 'Konto zostało zarejestrowane.')
            return redirect('login')

    context = {'form': form}
    return render(request, 'pacjenci/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nazwa użytkownika lub hasło są niepoprawne')

    context = {}
    return render(request, 'pacjenci/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    asystenci = Asystent.objects.all()
    liczba_asystentow = asystenci.count()

    pacjenci = Pacjent.objects.all()
    liczba_pacjentow = pacjenci.count()

    zgloszenia = Zgloszenie.objects.all()
    liczba_zgloszen = zgloszenia.count()

    lista = {'asystenci':asystenci,
             'liczba_asystentow':liczba_asystentow,
             'pacjenci':pacjenci,
             'liczba_pacjentow':liczba_pacjentow,
             'zgloszenia':zgloszenia,
             'liczba_zgloszen':liczba_zgloszen}

    return render(request, 'pacjenci/dashboard.html', lista)

@login_required(login_url='login')
@allowed_users(allowed_roles=['asystent'])
def userPage(request):
    asystent = request.user.asystent
    a_dom = asystent.dom

    pacjenci = Pacjent.objects.filter(dom=a_dom)
    liczba_pacjentow = pacjenci.count()
    zgloszenia = Zgloszenie.objects.filter(pacjent__in=pacjenci)
    liczba_zgloszen = zgloszenia.count()

    myFilterPacjent = PacjentFilter(request.GET, queryset=pacjenci)
    pacjenci = myFilterPacjent.qs

    myFilterZgloszenie = ZglosznieFilter(request.GET, queryset=zgloszenia)
    zgloszenia = myFilterZgloszenie.qs

    context = {'asystent':asystent,
               'pacjenci':pacjenci,
               'liczba_pacjentow':liczba_pacjentow,
               'myFilterPacjent': myFilterPacjent,
               'zgloszenia':zgloszenia,
               'myFilterZgloszenie':myFilterZgloszenie,
               'liczba_zgloszen':liczba_zgloszen}
    return render(request, 'pacjenci/profil_asystenta.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrator','asystent'])
def pacjenci(request):

    pacjenci = Pacjent.objects.all()
    myFilterPacjentAll = PacjentFilterAll(request.GET, queryset=pacjenci)
    pacjenci = myFilterPacjentAll.qs


    return render(request, 'pacjenci/pacjenci.html', {'pacjenci':pacjenci, 'myFilterPacjentAll': myFilterPacjentAll})

@login_required(login_url='login')
@allowed_users(allowed_roles=['asystent'])
def pacjenci_asystent(request):
    asystent = request.user.asystent
    a_dom = asystent.dom

    pacjenci = Pacjent.objects.filter(dom=a_dom)

    myFilterPacjent = PacjentFilter(request.GET, queryset=pacjenci)
    pacjenci = myFilterPacjent.qs
    return render(request, 'pacjenci/pacjenci_asystent.html', {'pacjenci':pacjenci, 'myFilterPacjent': myFilterPacjent})


@login_required(login_url='login')
#@allowed_users(allowed_roles=['administrator'])
def asystenci(request, pk_test):

    asystent = Asystent.objects.get(id=pk_test)
    a_dom = asystent.dom

    pacjenci = Pacjent.objects.filter(dom=a_dom)
    liczba_pacjentow = pacjenci.count()

    zgloszenia = Zgloszenie.objects.filter(pacjent__in=pacjenci)

    myFilterPacjent = PacjentFilter(request.GET, queryset=pacjenci)
    pacjenci = myFilterPacjent.qs

    myFilterZgloszenie = ZglosznieFilter(request.GET, queryset=zgloszenia)
    zgloszenia = myFilterZgloszenie.qs

    context = {'asystent':asystent,
               'pacjenci':pacjenci,
               'liczba_pacjentow':liczba_pacjentow,
               'myFilterPacjent': myFilterPacjent,
               'zgloszenia':zgloszenia,
               'myFilterZgloszenie':myFilterZgloszenie}

    return render(request, 'pacjenci/asystenci.html', context)

@login_required(login_url='login')
def pacjent_podglad(request, pk_test):

    pacjent = Pacjent.objects.get(id=pk_test)
    p_dom = pacjent.dom

    asystenci = Asystent.objects.filter(dom=p_dom)

    zgloszenia = Zgloszenie.objects.filter(pacjent=pacjent)

    context = {'pacjent':pacjent,
               'asystenci':asystenci,
               'zgloszenia':zgloszenia
               }

    return render(request, 'pacjenci/pacjent_podglad.html', context)

@login_required(login_url='login')
def dodajZgloszenie(request):
    form = DodajZgloszenie()
    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = DodajZgloszenie(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'pacjenci/dodaj_zgloszenie.html', context)

@login_required(login_url='login')
def aktualizujZgloszenie(request, pk):
    zgloszenie = Zgloszenie.objects.get(id=pk)
    form = DodajZgloszenie(instance=zgloszenie)

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = DodajZgloszenie(request.POST, instance=zgloszenie)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'pacjenci/dodaj_zgloszenie.html', context)

@login_required(login_url='login')
def usunZgloszenie(request, pk):
    zgloszenie = Zgloszenie.objects.get(id=pk)
    if request.method == 'POST':
        zgloszenie.delete()
        return redirect('/')

    context = {'zgloszenie':zgloszenie}
    return render(request, 'pacjenci/delete.html', context)

@login_required(login_url='login')
def aktualizujPacjenta(request, pk):
    pacjent = Pacjent.objects.get(id=pk)
    form = DodajPacjenta(instance=pacjent)

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = DodajPacjenta(request.POST, instance=pacjent)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'pacjenci/dodaj_pacjenta.html', context)

@login_required(login_url='login')
def usunPacjenta(request, pk):
    pacjent = Pacjent.objects.get(id=pk)
    if request.method == 'POST':
        pacjent.delete()
        return redirect('/')

    context = {'pacjent':pacjent}
    return render(request, 'pacjenci/usun_pacjenta.html', context)

@login_required(login_url='login')
def aktualizujAsystenta(request, pk):
    asystent = request.user.asystent
    form = DodajAsystenta(instance=asystent)

    if request.method == 'POST':
        form = DodajAsystenta(request.POST, instance=asystent)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'pacjenci/dodaj_asystenta.html', context)
