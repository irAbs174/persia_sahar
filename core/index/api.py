from django.http import JsonResponse


def index_content(request):
    return JsonResponse({
        'status' : 200,
        'success' : True,
    })