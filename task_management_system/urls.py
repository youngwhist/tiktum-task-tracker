from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Импортируем TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Новый маршрут для корня, который будет отображать стандартную страницу
    path('', TemplateView.as_view(template_name="index.html")),  # Здесь используем шаблон index.html
    
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),  
    path('api/v1/projects/', include('projects.urls')), 
    path('api/v1/tasks/', include('tasks.urls')),  
]
