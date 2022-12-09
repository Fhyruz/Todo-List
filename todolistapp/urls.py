from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add', views.addTodo, name='add'),
  path('complete/<list_id>', views.complete, name='complete'),
  path('deletecompleted', views.deletecompleted, name='deletecompleted'),
  path('deleteAll', views.deleteAll, name='deleteAll'),
]
