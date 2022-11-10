from rest_framework.response import Response
from rest_framework.decorators import api_view

from digiresume.models import (
    Me, CodingSkill, Clients, Frameworks, Portfolio, Certificates,
    Testimonials
)
from .serializers import (
    MeSerializer, CodingSkillSerializer, ClientSerializer,
    FrameworksSerializer, PortfolioSerializer, CertificateSerializer,
    TestimonySerializer,
)

@api_view(['GET'])
def getDetailMe(request):
    me = Me.objects.all()
    serializer = MeSerializer(me, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getContactMessage(request):
    info = Clients.objects.all()
    serializer = ClientSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCodingSkillsList(request):
    skill = CodingSkill.objects.all()
    serializer = CodingSkillSerializer(skill, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFrameworksList(request):
    framework = Frameworks.objects.all()
    serializer = FrameworksSerializer(framework, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPortfolioList(request):
    portfolio = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCertificateList(request):
    certificate = Certificates.objects.all()
    serializer = CertificateSerializer(certificate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTestimonyList(request):
    testimony = Testimonials.objects.all()
    serializer = TestimonySerializer(testimony, many=True)
    return Response(serializer.data)