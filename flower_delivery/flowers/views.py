from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, OrderForm, ReviewForm
from .models import Flower, Order
from django.http import HttpResponse


def home(request):
    return render(request, 'flowers/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('catalog')
    else:
        form = UserRegisterForm()
    return render(request, 'flowers/register.html', {'form': form})


def catalog(request):
    #flowers = Flower.objects.all()
    #return render(request, 'flowers/catalog.html', {'flowers': flowers})
    return render(request, 'flowers/catalog.html')


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()
            return redirect('order_history')
    else:
        form = OrderForm()
    return render(request, 'flowers/order.html', {'form': form})


def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'flowers/order_history.html', {'orders': orders})

