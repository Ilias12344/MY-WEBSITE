from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Experience, Contact
from django.views.decorators.csrf import csrf_exempt
import json

# WEB-PAGES VIEWS

def home(request):
    """
    Renders the main portfolio page
    """
    return render(request, "index.html")


def resume(request):
    """
    Simple resume page or PDF placeholder
    """
    return HttpResponse("<h1>Resume coming soon</h1>")

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render(request, 'contact.html')



# API VIEWS


def experience_list(request):
    data = list(Experience.objects.values())
    return JsonResponse(data, safe=False)


@csrf_exempt
def contact_form(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Contact.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            message=data.get("message")
        )

        return JsonResponse({"status": "success"})
