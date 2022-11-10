from rest_framework import serializers
from digiresume.models import *

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Me
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class CodingSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingSkill
        fields = '__all__'

class FrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'
