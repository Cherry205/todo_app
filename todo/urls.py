from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset, todo_list_html,todo_update_html,todo_delete_html


router = DefaultRouter()
router.register(r'todos',TodoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('todos-html/', todo_list_html, name ='todo-html'),
    path('todos-html/update/<int:pk>/', todo_update_html, name ='todo-Update'),
    path('todos-html/delete/<int:pk>', todo_delete_html, name ='todo-delete'),] 
    





