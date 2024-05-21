from django.shortcuts import render


def dashboard_index_view(request):
    return render(request, 'dashboard/index.html')