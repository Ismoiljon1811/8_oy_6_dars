from rest_framework import serializers
from .models import Company, Area, Building

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'