"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', studentlar),
    path('rejalar/', rejalar),
    path('bitiruvchilar_rejalari/', BitiruvchilarRejalari),
    path('bajarilmagan/', bajarilmagan_rejalar),
    path('bituruvchilar/', u_kurslar),
    path('b_t_reja/<int:son>', bitta_talaba_rejasi),
]
