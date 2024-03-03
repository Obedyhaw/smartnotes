from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,SetPasswordForm
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class SignupView(CreateView):
    form_class = UserRegisterForm
    template_name='firstapp/signup.html'
    success_url='/smart/notes'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/smart/notes')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name='firstapp/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/smart/notes')
        return super().get(request, *args, **kwargs)




    

# class LogoutInterfaceView(LogoutView):
#     template_name='firstapp/logout.html'
def logout_view(request):
    logout(request)
    return render(request, 'firstapp/logout.html')
    

# Create your views here.
class HomeView(TemplateView):
    template_name='firstapp/welcome.html'
    extra_context={'today':datetime.today()}

# class AuthorizedView(LoginRequiredMixin,TemplateView):
#     template_name='firstapp/authorized.html'
#     login_url='/login'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request,, {})