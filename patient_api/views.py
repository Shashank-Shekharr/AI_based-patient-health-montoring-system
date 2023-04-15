from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([])
@permission_classes([])
@api_view(['POST'])

def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
