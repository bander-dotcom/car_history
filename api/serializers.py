from rest_framework import serializers
from .models import (
    Users, Cars, Accidents, Reports, Evaluation,
    WorkshopsData, ImageAccident, ImageCar
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'username', 'email']
        read_only_fields = ['user_id']

class ImageCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = ['img_car_id', 'car', 'img_car', 'uploaded_at']
        read_only_fields = ['img_car_id', 'uploaded_at']

class ImageAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAccident
        fields = ['img_acc_id', 'accident', 'img_accident', 'uploaded_at']
        read_only_fields = ['img_acc_id', 'uploaded_at']


class CarSerializer(serializers.ModelSerializer):
    images = ImageCarSerializer(many=True, read_only=True, source='imagecar_set')

    class Meta:
        model = Cars
        fields = [
            'car_id', 'report', 'vin', 'name_car', 'plate_number', 'make', 'model', 'year', 'color',
            'engine_size', 'fuel_type', 'engine_capecity', 'gear_type',
            'receipt_number', 'receipt_date', 'created_at', 'mileage', 'images'
        ]
        read_only_fields = ['car_id', 'created_at']


class AccidentSerializer(serializers.ModelSerializer):
    images = ImageAccidentSerializer(many=True, read_only=True, source='imageaccident_set')

    class Meta:
        model = Accidents
        fields = [
            'accident_id', 'car', 'report', 'type_accident', 'damaged_parts',
            'accident_date', 'created_at', 'images'
        ]
        read_only_fields = ['accident_id', 'created_at']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['report_id', 'import_type', 'import_file', 'rating', 'created_at']
        read_only_fields = ['report_id', 'created_at']

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopsData
        fields = ['workshop_id', 'car', 'mech_insp_desc', 'comp_scan_desc', 'created_at']
        read_only_fields = ['workshop_id', 'created_at']

class EvaluationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    # الحقول التي نرسلها عند الإدخال
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(), source="user", write_only=True
    )
    car_id = serializers.PrimaryKeyRelatedField(
        queryset=Cars.objects.all(), source="car", write_only=True
    )

    class Meta:
        model = Evaluation
        fields = [
            'evaluation_id', 'user', 'car', 'rate',
            'user_id', 'car_id'
        ]
        read_only_fields = ['evaluation_id']
