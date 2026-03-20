

from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('service/', views.services_page, name='services'),
    path ('submit-quote/', views.submit_quote, name='submit_quote'),
]
