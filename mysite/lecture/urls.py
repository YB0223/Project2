from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('read/<id>',views.read, name='read'),
    path('update/<id>',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
]