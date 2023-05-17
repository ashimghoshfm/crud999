from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('del/<int:id>', views.rem, name='rem'),
    path("add/", views.addnew, name='addnew'),
    path("edit/<int:id>", views.edit, name='edit')
]