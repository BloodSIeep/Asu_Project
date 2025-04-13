"""
proj_maths URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms-list/', views.terms_list, name='terms_list'),
    path('add-term/', views.add_term, name='add_term'),
    path('send-term/', views.send_term, name='send_term'),
    path('i2c_decoder/', views.decode_i2c_packet, name='i2c_decoder'),
    path('texts-list/', views.texts_list, name='texts_list'),
    path('i2c_explanation/', views.i2c_explanation, name='i2c_explanation'),
    path('test-input/', views.test_input, name='test-input')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
