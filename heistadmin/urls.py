from django.urls import path

from heistadmin.views import createView, defaultView, deleteView, updateView, listView

app_name = "heistadmin"

urlpatterns = [
   path('', defaultView, name='dashboard'),
   path('<str:slug>/', listView, name='list'),
   path('create/<str:slug>/', createView, name='create'),
   path('update/<str:slug>/<int:pk>/', updateView, name='update'),
   path('delete/<str:slug>/<int:pk>/', deleteView, name='delete'),
]