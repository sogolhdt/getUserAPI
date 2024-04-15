from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django_ratelimit.decorators import ratelimit

from .models import Student
from .serializers import StudentSerializer,StudentInfoSerializer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@ratelimit(key='ip', rate='10/h', method='GET', block=True)
def get_students_list(request):
    students = Student.objects.all()
    serializer = StudentInfoSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@ratelimit(key='ip', rate='10/h', method='GET', block=True)

def add_student(request):
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@ratelimit(key='ip', rate='10/h', method='GET', block=True)
def get_student_by_name(request):
    name = request.GET.get('name', None)
    if name:
        students = Student.objects.filter(first_name=name)
        if students.exists():
            serializer = StudentInfoSerializer(students, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
