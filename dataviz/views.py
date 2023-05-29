from django.shortcuts import render

def dashapp_view(request):
    return render(request, 'dashapp.html')


