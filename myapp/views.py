from django.http import JsonResponse


def no_rest_no_model(request):
    guests=[
        {
           'id':'123',
           'name':'omar',
           'age':'12' 
        },
        {
           'id':'345',
           'name':'ahmed',
           'age':'15' 
        }
        ]
    return JsonResponse(guests,safe=False)