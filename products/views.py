from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from products.models import Item
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

# Create your views here.

class ItemsView(ListView):
    model = Item


class ItemView(DetailView):
    model = Item


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print(user)
                login(request, user)
                return render(request, 'dashboard.html')
            else:
                pass
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    redirect('/login')
