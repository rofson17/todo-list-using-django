from django.urls import path
from .views import index, add, deleteItem, editItem

urlpatterns = [
    path('', index),
    path('add/', add),
    path('delete/<int:id>/', deleteItem),
    path('edit/<int:id>/', editItem)
]
