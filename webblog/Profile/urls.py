from django.urls import path
 
# importing views from views..py
from .views import Name , viewProfile
 
urlpatterns = [
    path('', Name),
    path("<str:name>",viewProfile)
]