from rest_framework import serializers
from .models import Users, Cars, Accidents, Reports, Evaluation, WorkshopsData, ImageAccident, ImageCar
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # أو حدد الحقول التي تريد عرضها فقط
        read_only_fields = fields  # جميع الحقول قراءة فقط

class ImageCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = '__all__'
        read_only_fields = fields

class ImageAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAccident
        fields = '__all__'
        read_only_fields = fields

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
        fields = '__all__'
        read_only_fields = fields

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'
        read_only_fields = fields

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopsData
        fields = '__all__'
        read_only_fields = fields

class EvaluationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    
    class Meta:
        model = Evaluation
        fields = '__all__'
        read_only_fields = fields
