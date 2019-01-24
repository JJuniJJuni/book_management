from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View


def check_email(original_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.email.endswith('@rgpkorea.co.kr'):
            return original_func(request, *args, **kwargs)
        else:
            messages.error(request, "옳지 않은 email 입니다.")
            User.objects.get(email=request.user.email).delete()
            return redirect(reverse('logout'))
    return wrapper_func


@method_decorator(login_required, name='dispatch')
@method_decorator(check_email, name='dispatch')
class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')


class LoginView(View):
    def get(self, request):
        return render(request, template_name='login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
