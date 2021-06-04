from django.urls import path
from . import views

urlpatterns = [
    path('api/get', views.TodoList.as_view()),
    path('api/create', views.CreateTodo.as_view()),
    path('api/update/<int:pk>', views.UpdateTodo.as_view()),
    path('api/delete/<int:pk>', views.DeleteTodo.as_view()),
]

