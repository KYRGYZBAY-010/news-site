from django.urls import path
from .import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetalView.as_view(), name='news-detail'),
    path('update/<int:pk>', views.NewsUpdateView.as_view(), name='news-update')
]