"""
URL configuration for golfScore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from golfScore_app import views


urlpatterns = [
    path('round', views.round_views.list_golfHouse_View, name='listGolfHouse'),
    path('round/<str:pk>', views.round_views.input_round_View,  name='inputRound'),
    path('round2', views.round_views.GolfHouseListView.as_view(), name='listGolfHouse2'),
    
    
    # hayashida start
    path('login/', views.user_views.UserLoginView.as_view(), name='login'),
    # hayashida end
    
]


