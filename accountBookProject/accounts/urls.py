from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    # path('auth/', include('rest_framework.urls')),
    # path('accounts/profile/', views.login ),
    path('rest-auth/', include('dj_rest_auth.urls')),
]