from django.urls import path
from .views import TodoCrudView

urlpatterns = [
    path('todo/', TodoCrudView.as_view(), name='todo-crud'),
]
