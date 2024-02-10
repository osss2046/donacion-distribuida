from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación de Django
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
