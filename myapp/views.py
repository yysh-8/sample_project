from django.http import JsonResponse
from datetime import datetime


def no_rest_no_model(request):
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    server_time={
           'id':'123',
           'name':'cairo',
           'time': current_time
        }
    return JsonResponse(server_time,safe=False)