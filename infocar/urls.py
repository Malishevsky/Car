from django.urls import path
from .views import index,create_auto,delete_auto,edit_auto,get_mechanical

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_auto ,name='create'),
    path('delete/<int:id>', delete_auto ,name='delete'),
    path('edit/<int:id>',edit_auto,name='edit'),
    path('transmission/<int:id>',get_mechanical,name='get_mechanical'),

]
