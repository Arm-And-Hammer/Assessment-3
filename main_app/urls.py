from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index, name='index'),
    path('delete/<int:widgit_id>/', views.delete_widgit, name='delete_widgit')
]