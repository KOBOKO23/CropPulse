from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        personal_number = request.POST.get('personal_number')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'registration/login.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'registration/login.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully. You can now login to your account.")
        return redirect('login')


class FormsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'forms.html')
