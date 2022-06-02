from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('creates/', views.creates, name='creates'),
    path('<int:pk>', views.HomeDetail.as_view(), name='detail_home'),
    path('community/', views.community, name='community')
]