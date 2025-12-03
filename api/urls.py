from django.urls import path
from .views import register_user, login_user
from rest_framework import routers
from .views import (
    UserViewSet, CarViewSet, AccidentViewSet,
    ReportViewSet, EvaluationViewSet, WorkshopViewSet,
    ImageAccidentViewSet, ImageCarViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet)
router.register(r'accidents', AccidentViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'evaluations', EvaluationViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'image_accidents', ImageAccidentViewSet)
router.register(r'image_cars', ImageCarViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
]