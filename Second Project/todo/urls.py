from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_item/<int:pk>', views.deleteItem, name = 'deleteItem'),
    path('update_item<int:pk>', views.updateItem, name = 'updateItem'),
]