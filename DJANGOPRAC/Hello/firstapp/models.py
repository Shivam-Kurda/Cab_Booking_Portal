# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', unique=True, max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    pswd = models.CharField(db_column='Pswd', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Driver(models.Model):
    driver_id = models.AutoField(db_column='Driver_id', primary_key=True)  # Field name made lowercase.
    dl_id = models.CharField(db_column='DL_ID', unique=True, max_length=10)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', unique=True, max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    pswd = models.CharField(db_column='Pswd', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Driver'


class Vehicle(models.Model):
    vehicle_plate = models.CharField(db_column='VEHICLE_PLATE', primary_key=True, max_length=20)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=256)  # Field name made lowercase.
    manu_year = models.IntegerField(db_column='Manu_year')  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLE'





class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_id', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.CASCADE, db_column='Customer_id')  # Field name made lowercase.
    driver = models.ForeignKey(Driver, models.CASCADE, db_column='Driver_id')  # Field name made lowercase.
    vehicle_plate = models.ForeignKey(Vehicle, models.CASCADE, db_column='Vehicle_PLATE')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    paytime = models.CharField(db_column='Paytime', max_length=10)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'





class Ride(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE, db_column='Customer_id')  # Field name made lowercase.
    driver = models.ForeignKey(Driver, models.CASCADE, db_column='Driver_id')  # Field name made lowercase.
    vehicle_plate = models.ForeignKey(Vehicle, models.CASCADE, db_column='Vehicle_PLATE')  # Field name made lowercase.
    ride_date = models.CharField(db_column='RIDE_DATE', max_length=20)  # Field name made lowercase.
    ride_time = models.CharField(db_column='RIDE_TIME', max_length=20)  # Field name made lowercase.
    pickup_loc = models.CharField(db_column='Pickup_loc', max_length=255)  # Field name made lowercase.
    drop_loc = models.CharField(db_column='DROP_LOC', max_length=255)  # Field name made lowercase.
    ride_otp = models.IntegerField(db_column='RIDE_OTP',primary_key=True)  # Field name made lowercase.
    completion_status = models.CharField(db_column='Completion_status', max_length=10)  # Field name made lowercase.
    rating=models.IntegerField(db_column='rating')
    class Meta:
        managed = False
        db_table = 'Ride'
        unique_together = (('customer', 'driver', 'vehicle_plate'),)






