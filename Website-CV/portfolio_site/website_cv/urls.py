from django.urls import path
from .views import home, resume, experience_list, contact_form
from . import views

urlpatterns = [
    # Pages
    path("", home, name="home"),
    path("resume/", resume, name="resume"),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
    # API
    path("api/experience/", experience_list),
    path("api/contact/", contact_form),
]
