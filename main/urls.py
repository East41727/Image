from django.urls import path
from .views import Homepage,Gallery,All_of_pictues,delete_picture
from django.utils.translation import gettext_lazy as _




urlpatterns =   [
   
  
    path('gallery/', Gallery, name='galleries'),
    path('picture/', All_of_pictues,name='pi'),
    path('delete_img/<int:pk>/',delete_picture, name='delete-picture'),
    path('', Homepage.as_view(), name='index'),
    



]