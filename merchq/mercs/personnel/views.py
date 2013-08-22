from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the personnel index.")

def force_personnel(request, force_id):
    return HttpResponse("Hello, world. You're seeing a force")
