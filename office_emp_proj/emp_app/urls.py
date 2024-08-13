from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add_emp', views.add_emp, name = 'add_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('list_emp', views.list_emp, name = 'list_emp'),
    path('list_emp/', views.list_emp, name='list_emp'),
    path('update_emp', views.update_emp, name = 'update_emp'),
    path('update_emp/', views.update_emp, name='update_emp'),
    path('update_emp/<int:emp_id>/', views.update_emp, name='update_emp'),
    path('delete_emp', views.delete_emp, name = 'delete_emp'),
    path('delete_emp/', views.delete_emp, name = 'delete_emp'),
    path('delete_emp/<int:emp_id>/', views.delete_emp, name='delete_emp'),
    path('search_emp', views.search_emp, name = 'search_emp'),
    path('search_emp/', views.search_emp, name='search_emp'),
]
