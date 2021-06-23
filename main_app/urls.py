from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>', views.cats_show, name='cats_show')

]