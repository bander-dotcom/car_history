from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Users, Cars, Accidents, ImageAccident, ImageCar, Reports, Evaluation, WorkshopsData
from .serializers import (UserSerializer, CarSerializer, AccidentSerializer,
                          ImageAccidentSerializer, ImageCarSerializer, ReportSerializer,
                          EvaluationSerializer, WorkshopSerializer)
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # المستخدم العادي لا يصلح له تعديل المستخدمين


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = WorkshopsData.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAdminOrReadOnly]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.select_related('owner').all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AccidentViewSet(viewsets.ModelViewSet):
    queryset = Accidents.objects.select_related('car').prefetch_related('images').all()
    serializer_class = AccidentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # car_id يأتي من serializer.car_id
        serializer.save()


class ImageCarViewSet(viewsets.ModelViewSet):
    queryset = ImageCar.objects.select_related('car').all()
    serializer_class = ImageCarSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ImageAccidentViewSet(viewsets.ModelViewSet):
    queryset = ImageAccident.objects.select_related('accident').all()
    serializer_class = ImageAccidentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.select_related('accident', 'author').all()
    serializer_class = ReportSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.select_related('workshop', 'author').all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
