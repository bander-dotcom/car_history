# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Accidents(models.Model):
    accident_id = models.IntegerField(primary_key=True)
    car = models.ForeignKey('Cars', models.DO_NOTHING, blank=True, null=True)
    report = models.ForeignKey('Reports', models.DO_NOTHING, blank=True, null=True)
    type_accident = models.TextField(blank=True, null=True) 
    damaged_parts = models.TextField()
    accident_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Accidents'


class Cars(models.Model):
    car_id = models.IntegerField(primary_key=True)
    report = models.ForeignKey('Reports', models.DO_NOTHING, blank=True, null=True)
    vin = models.TextField(db_column='VIN') 
    plate_number=models.IntegerField(blank=True, null=True) 
    name_car = models.TextField()
    make = models.TextField()  
    model = models.TextField()  
    year = models.IntegerField()
    color = models.TextField()  
    engine_size = models.TextField()  
    fuel_type = models.TextField()  
    engine_capecity = models.IntegerField()
    gear_type = models.IntegerField()
    receipt_number = models.IntegerField(blank=True, null=True)
    receipt_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    mileage = models.IntegerField()

    class Meta:
        db_table = 'Cars'

class Reports(models.Model):
    report_id = models.IntegerField(primary_key=True)
    import_type = models.TextField() 
    import_file = models.TextField()
    rating = models.TextField() 
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Reports'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.TextField()
    password_hash = models.TextField()
    email = models.TextField()  


    class Meta:
        db_table = 'Users'


class WorkshopsData(models.Model):
    workshop_id = models.IntegerField(primary_key=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    mech_insp_desc = models.TextField(blank=True, null=True) 
    comp_scan_desc = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Workshops_data'


class Evaluation(models.Model):
    evaluation_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'evaluation'


class ImageAccident(models.Model):
    img_acc_id = models.IntegerField(primary_key=True)
    accident = models.ForeignKey(Accidents, models.DO_NOTHING, blank=True, null=True)
    img_accident = models.BinaryField(blank=True, null=True)
    uploaded_at = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'image_accident'


class ImageCar(models.Model):
    img_car_id = models.IntegerField(primary_key=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    img_car = models.BinaryField(blank=True, null=True)
    uploaded_at = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'image_car'