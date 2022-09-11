

from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),
    
    # Country
    path('kyrgyzstan/',views.kyrgyzstan,name="kyrgyzstan"),
    path('kazakhstan/',views.kazakhstan,name="kazakhstan"),
    path('barbados/',views.barbados,name="barbados"),
    
    
    
    
] 