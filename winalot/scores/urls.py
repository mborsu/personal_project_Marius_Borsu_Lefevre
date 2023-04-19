from django.urls import include, path
from django.contrib.auth.views import LoginView


from . import views

app_name = 'scores'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PoolView.as_view(), name='pool'),
    path('pool/<int:pk>/', views.MatchView.as_view(), name='match'),
    
]

