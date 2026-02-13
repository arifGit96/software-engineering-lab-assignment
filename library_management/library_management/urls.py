from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('transactions/', include('transactions.urls')),
    path('', home, name='home'),


]
