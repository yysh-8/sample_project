from django.http import JsonResponse
from datetime import datetime
from .models import User

#case 1 no rest no model
def no_rest_no_model(request):
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    server_time={
           'id':'123',
           'name':'cairo',
           'time': current_time
        }
    return JsonResponse(server_time,safe=False)
 
 #case 2 no rest and from model
def no_rest_from_model(request):
   data=User.objects.all()
   response={
      'users':list(data.values('name','age'))
   }
   return JsonResponse(response,safe=False)