from rest_framework import serializers
from .models import *

class daily_load_curve_serializer(serializers.ModelSerializer):
    class Meta:
        model=daily_load_curve
        fields = '__all__'
        
class details_of_substation_line_serializer(serializers.ModelSerializer):
    class Meta:
        model=details_of_substation_line
        fields = '__all__'
        
class details_of_transmission_line_serializer(serializers.ModelSerializer):
    class Meta:
        model=details_of_transmission_line
        fields = '__all__'
        
class finance_mis_serializer(serializers.ModelSerializer):
    class Meta:
        model=finance_mis
        fields = '__all__'
        
class hr_mis_serializer(serializers.ModelSerializer):
    class Meta:
        model=hr_mis
        fields = '__all__'
        
class kpi_serializer(serializers.ModelSerializer):
    class Meta:
        model=kpi
        fields = '__all__'
        
class manpower_requirement_serializer(serializers.ModelSerializer):
    class Meta:
        model=manpower_requirement
        fields = '__all__'
