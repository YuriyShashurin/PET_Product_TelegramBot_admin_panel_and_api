from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from products.models import Item, BotType
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

# Create your views here.


def main_page(request):
    return redirect('/admin-area/login')


class ItemsView(ListView):
    template_name = 'bot_info.html'
    model = Item

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/admin-area/login')

        return super().dispatch(request, *args, **kwargs)


class ItemView(DetailView):
    model = Item


class BotsViews(ListView):
    model = BotType
    template_name = 'dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/admin-area/login')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            user_id = self.request.user
            queryset = BotType.objects.filter(name__contains=search, allowed_users=user_id)
            if len(queryset) > 0:
                return queryset
            else:

                return None

        else:
            user_id = self.request.user
            queryset = BotType.objects.filter(allowed_users=user_id)
            return queryset


class CreateBotView(CreateView):
    model = BotType
    fields = '__all__'
    template_name = 'create_bot.html'
    success_url = '/admin-area/dashboard/'


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin-area/dashboard/')
            else:
                return render(request, 'login.html', {'form': form, 'error_text': "Введен неверный логин/пароль"})
    else:
        if request.user.is_authenticated:
            return redirect('/admin-area/dashboard/')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/admin-area/login')


