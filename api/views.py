from rest_framework import viewsets
from .models import Users, Cars, Accidents, Reports, Evaluation, WorkshopsData, ImageAccident, ImageCar
from .serializers import (
    UserSerializer, CarSerializer, AccidentSerializer, 
    ReportSerializer, EvaluationSerializer, WorkshopSerializer,
    ImageAccidentSerializer, ImageCarSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Account created successfully",
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid username or password"}, status=400)

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "message": "Login successful",
        "user_id": user.id,
        "username": user.username,
        "token": token.key
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class AccidentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accidents.objects.all()
    serializer_class = AccidentSerializer

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkshopsData.objects.all()
    serializer_class = WorkshopSerializer

class EvaluationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class ImageCarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImageCar.objects.all()
    serializer_class = ImageCarSerializer

class ImageAccidentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImageAccident.objects.all()
    serializer_class = ImageAccidentSerializer
