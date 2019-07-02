from django.db import models

# Create your models here.
class daily_load_curve(models.Model):
    Date = models.CharField(max_length=10)
    Demand = models.IntegerField()
    class Meta():
        db_table = "daily_load_curve"
        
class details_of_substation_line(models.Model):
    zone = models.CharField(max_length=10)
    Name_of_the_Sub_Station = models.CharField(max_length=500)
    Voltage_Ratio = models.CharField(max_length=15)
    No_of_ICTs_x_MVA_Capacity = models.CharField(max_length=15)
    Total_MVA_Capacity_of_ICTs = models.CharField(max_length=15)
    Date_of_Commissioning = models.CharField(max_length=10)
    class Meta():
        db_table = "details_of_substation_line"

class details_of_transmission_line(models.Model):
    zone = models.CharField(max_length=10)
    Name_of_transmission_line = models.CharField(max_length=500)
    voltage_level_KV = models.CharField(max_length=20)
    sc_or_dc = models.CharField(max_length=10)
    line_length_ckt_km = models.FloatField()
    conductor_type = models.CharField(max_length=10)
    Date_of_comissioning = models.CharField(max_length=10)
    class Meta():
        db_table = "details_of_transmission_line"

class finance_mis(models.Model):
    Year = models.CharField(max_length=10)
    Parameter = models.CharField(max_length=50)
    Target = models.FloatField()
    Achieved = models.FloatField()
    class Meta():
        db_table = "finance_mis"
        
class hr_mis(models.Model):
    Year = models.CharField(max_length=10)
    Parameter = models.CharField(max_length=50)
    Target = models.FloatField()
    Achieved = models.FloatField()
    class Meta():
        db_table = "hr_mis"

class kpi(models.Model):
    Year = models.CharField(max_length=10)
    Parameter = models.CharField(max_length=30)
    Target = models.FloatField()
    Achieved = models.FloatField()
    class Meta():
        db_table = "kpi"
        
class manpower_requirement(models.Model):
    payscale = models.CharField(max_length=25)
    Post = models.CharField(max_length=100)
    Total_proposed_post = models.IntegerField()
    
    class Meta():
        db_table = "manpower_requirement"

    
