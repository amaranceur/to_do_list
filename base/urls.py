from django.urls import path 
from .views import TaskList , TaskDetail , TaskCreate , TaskUpdate , TaskDelete , Tasklogin,TaskRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TaskList.as_view(),name='task'),
    
    path('login/',Tasklogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', TaskRegister.as_view(),name='register'),   
    path('task/<int:pk>/',TaskDetail.as_view(),name='detail'),
    path('create-view',TaskCreate.as_view(),name='create-view'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete')

]
