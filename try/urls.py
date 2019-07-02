"""try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from ptcul import views

urlpatterns = [
    path('daily_load/',views.daily_load_curve_list.as_view()),
    path('substation_line/',views.details_of_substation_list.as_view()),
    path('transmission_line/',views.details_of_transmission_list.as_view()),
    path('finance_mis/',views.finance_mis_list.as_view()),
    path('hr_mis/',views.hr_mis_list.as_view()),
    path('kpi/',views.kpi_list.as_view()),
    path('manpower_requirement/',views.manpower_requirement_list.as_view()),
    path('admin/', admin.site.urls),
]
