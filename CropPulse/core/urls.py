from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, AboutView, SignupView, FormsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('signup/', SignupView.as_view(), name='signup'),

    # Use Django's built-in LoginView with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # LogoutView with redirect to login page after logout
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('forms/', FormsView.as_view(), name='forms'),
]
