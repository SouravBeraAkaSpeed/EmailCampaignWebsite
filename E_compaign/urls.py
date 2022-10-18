from django.urls import path

from .views import Home, dashboard, setting, download_file


urlpatterns = [
    path('', Home, name='home'),
    path('dashboard/<int:pk>', dashboard, name='dashboard'),
    path('settings/<int:pk>', setting, name='setting'),
    path('dashboard', dashboard, name='dashboard'),
    path('settings', setting, name='setting'),
    path('download/<str:filename>', download_file, name='download_file'),
]
