from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import task_user
from todolist.views import task_delete
from todolist.views import todolist_json
from todolist.views import todolist_add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', task_user, name='task_user'),
    path('task_delete/<int:id>', task_delete, name='task_delete'),
    path('json/', todolist_json, name='todolist_json'),
    path('add/', todolist_add, name='todolist_add'),
]