  
from django.urls import path
 
# importing views from views..py
from .views import geeks_view,viewBlog
 
urlpatterns = [
    path('', geeks_view),
    path('<str:blogname>',viewBlog),
]