from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="index"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('deactivate/<int:id>', views.deactivate, name="deactivate"),
]
