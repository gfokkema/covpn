from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:logentry_id>/', views.logentry, name='logentry'),
]
