from . import views
from django.urls import path
urlpatterns = [
    path('', views.project_list,name='proj_list'),
    path('create/', views.project_create,name='create'),
    path('<int:project_id>/edit/', views.project_edit, name='proj_edit'),
    path('<int:project_id>/delete/',views.project_delete , name='proj_delete'),
    path('register/',views.register,name='register')
    
]
