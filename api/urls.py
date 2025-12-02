from rest_framework import routers
from django.urls import path, include
from .views import (UserViewSet, CarViewSet, AccidentViewSet, ImageAccidentViewSet,
                    ImageCarViewSet, ReportViewSet, EvaluationViewSet, WorkshopViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'accidents', AccidentViewSet, basename='accident')
router.register(r'images/car', ImageCarViewSet, basename='imagecar')
router.register(r'images/accident', ImageAccidentViewSet, basename='imageaccident')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'evaluations', EvaluationViewSet, basename='evaluation')
router.register(r'workshops', WorkshopViewSet, basename='workshop')

urlpatterns = [
    path('', include(router.urls)),
]
