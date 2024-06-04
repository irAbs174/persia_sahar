from django.http import JsonResponse


def dashboard_content(request):
    return JsonResponse({
        'status' : '200',
        'success' : True,
    })