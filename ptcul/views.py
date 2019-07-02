from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class daily_load_curve_list(APIView):
    def get(self,request):
        obj = daily_load_curve.objects.all()
        serializer = daily_load_curve_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
class details_of_substation_list(APIView):
    def get(self,request):
        obj = details_of_substation_line.objects.all()
        serializer = details_of_substation_line_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
class details_of_transmission_list(APIView):
    def get(self,request):
        obj = details_of_transmission_line.objects.all()
        serializer = details_of_transmission_line_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
class finance_mis_list(APIView):
    def get(self,request):
        obj = finance_mis.objects.all()
        serializer = finance_mis_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
class hr_mis_list(APIView):
    def get(self,request):
        obj = hr_mis.objects.all()
        serializer = hr_mis_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
class kpi_list(APIView):
    def get(self,request):
        obj = kpi.objects.all()
        serializer = kpi_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
class manpower_requirement_list(APIView):
    def get(self,request):
        obj = manpower_requirement.objects.all()
        serializer = manpower_requirement_serializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data)
        
        