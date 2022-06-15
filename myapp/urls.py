from django.urls import path
from . import views

urlpatterns = [
    path('no-rest-no-model/',views.no_rest_no_model),
    path('no-rest-from-model/',views.no_rest_from_model)
    
]