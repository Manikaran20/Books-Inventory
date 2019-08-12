from django.urls import path

from . import views

app_name= 'googlebooks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inventory', views.InventoryView.as_view(), name= 'inventory'),
    path('<str:ID>/edit', views.BooksUpdate.as_view(), name='books_edit'),
    path('<str:ID>/delete', views.BooksDelete.as_view(), name= 'books_delete'),
    path('add', views.BooksAdd.as_view(), name='books_add')
]