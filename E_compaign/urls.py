from django.urls import path

from .views import Home, dashboard,setting


urlpatterns = [
    path('', Home, name='home'),
    path('dashboard/<int:pk>', dashboard, name='dashboard'),
    path('dashboard', dashboard, name='dashboard'),
    path('settings',setting,name='setting')
]
