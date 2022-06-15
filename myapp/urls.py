from django.urls import path
from . import views

urlpatterns = [
    path('no-rest/',views.no_rest_no_model)
    
]