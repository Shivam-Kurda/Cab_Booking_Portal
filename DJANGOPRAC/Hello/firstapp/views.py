from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,Driver,Ride,Vehicle,Payment
from django.contrib.auth import authenticate
import mysql.connector
import random
import datetime
from django.contrib import messages
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Shivam@02"

)
mycurs=mydb.cursor()
mycurs.execute("USE ula")
def index(request):
    customers=Customer.objects.all()
    
    


    return render(request,'index.html', {'customers':customers})
def counter(request):
    text=request.GET['text']
    textlen=len(text.split())
    return render(request,'counter.html',{'textln':textlen})
def register(request):
    if(request.method=='POST'):
        custobj=Customer.objects.filter(email=request.POST['email'])
        if(custobj.exists()):
            messages.error(request,"Sorry this user exists,please login instead")
            return redirect('register')
        else:

            cust=Customer()
            cust.first_name=request.POST['firstname']
            cust.last_name=request.POST['lastname']
            cust.email=request.POST['email']
            cust.phone=request.POST['phone_no']
            cust.pswd=request.POST['password']

            cust.save()
            return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    if(request.method=='POST'):
        email1=request.POST['email']
        paswd1=request.POST['pswd']
        try:

            cust=Customer.objects.get(email=email1,pswd=paswd1)
        
            request.session['custobj']=cust.customer_id
            return redirect('home')
        except:
            cust=None
            messages.error(request,"Sorry invaliid credentials, try again")
            return redirect('login')
            



        

            # return render(request,'home.html',{'cust':cust})
        # else:
        #     return render(request,'login.html')
    return render(request,'login.html')
   
def registerdrive(request):
    if(request.method=='POST'):

        driveobj=Driver.objects.filter(email=request.POST['email'])
        if(driveobj.exists()):
             messages.error(request,"Sorry this driver already exists,please login instead")
             return redirect('registerdrive')
        else:


            drive=Driver()

            drive.first_name=request.POST['firstname']
            drive.last_name=request.POST['lastname']
            drive.email=request.POST['email']
            drive.phone=request.POST['phone_no']
            drive.pswd=request.POST['password']
            drive.dl_id=request.POST['dlid']

     
            drive.save()
            return redirect('driverlogin')
    else:
        return render(request,'registerdrive.html')
def driverlogin(request):
    if(request.method=='POST'):
        email1=request.POST['email']
        paswd1=request.POST['pswd']
        try:

            drive=Driver.objects.get(email=email1,pswd=paswd1)
            return render(request,'driverhome.html',{'driverobj':drive})
        
            
        except:

            messages.error(request,"Sorry invaliid credentials, try again")

            
            return render(request,'driverlogin.html')
    
    return render(request,'driverlogin.html')
    
def home(request):
    custobj_id=request.session['custobj']
    custobj=Customer.objects.get(customer_id=custobj_id)
    if request.method =='POST':
        request.session['custobj']=custobj_id
        return redirect(book_ride)
    else:




        return render(request,'home.html',{'cust':custobj}) 

def driverhome(request):
    return render(request,'driverhome.html')
def book_ride(request):
    custobj_id=request.session['custobj']
    custobj=Customer.objects.get(customer_id=custobj_id)
    if request.method=='POST':
        pickup=request.POST['pickup']
        drop=request.POST['drop']
        request.session['pickup']=pickup
        request.session['drop']=drop
        # ride=Ride.objects.get(pickup_loc=pickup)
        # for rides in ride:
        #     rides.desc
        return redirect(show_rides)
    else:
        return render(request,'book_ride.html',{'cust':custobj}) 
def show_rides(request):

    custobj_id=request.session['custobj']
    custobj=Customer.objects.get(customer_id=custobj_id)
    
    if request.method=='POST':
        ride_id=request.POST['ride_otp']
        price=request.POST['price']

        ride=Ride.objects.get(ride_otp=ride_id)
        # print(type(ride.driver))

       
        request.session['ride.driver_id']=ride.driver.driver_id
        request.session['ride.vehicle']=ride.vehicle_plate.vehicle_plate
        request.session['price']=price
        return redirect('driver_accept')

        # driveobj=Driver.objects.get(driver_id=ride.driver)
        return redirect(payment_ride)
        


    pickup=request.session['pickup']
    drop=request.session['drop']
    
    rides=Ride.objects.filter(drop_loc=pickup)
    if(rides.exists()):
        # rides=rides.values()
        ride_fares=[]
        for i in range(0,len(rides)):
            ride_fares.append(random.randint(200,250))

        ride_obj_fare=[]
        for i in range(0,len(rides)):
            ride_obj_fare.append([rides[i],ride_fares[i]])
        
            
        return render(request,'show_rides.html',{'rides':ride_obj_fare}) 
    
    # for rides in ride:

    




   

    
def payment_ride(request):
    custobj=Customer.objects.get(customer_id=request.session['custobj'])

    driver=Driver.objects.get(driver_id=request.session['ride.driver_id'])
    vehicle=Vehicle.objects.get(vehicle_plate=request.session['ride.vehicle'])
    payment_am=request.session['price']
    if request.method=='POST':
        payment=Payment()
        # payment.payment_id=101
        payment.customer=custobj
        payment.driver=driver
        payment.vehicle_plate=vehicle
        payment.amount=payment_am
        payment.method=request.POST['payment_method']
        payment.paytime=(datetime.datetime.now()).strftime('%d-%m-%Y')
        payment.save()
        return redirect('ratings')


    return render(request,'payment_ride.html',{'objs':[custobj,driver,vehicle,payment_am]})


def driver_accept(request):
    if request.method=='POST':
        if(request.POST['choice']=="yes"):
            custobj=Customer.objects.get(customer_id=request.session['custobj'])

            driver=Driver.objects.get(driver_id=request.session['ride.driver_id'])
            vehicle=Vehicle.objects.get(vehicle_plate=request.session['ride.vehicle'])
            rideobj=Ride()
            rideobj.customer=custobj
            rideobj.driver=driver
            rideobj.vehicle_plate=vehicle
            rideobj.pickup_loc=request.session['pickup']
            rideobj.drop_loc=request.session['drop']
            rideobj.ride_date=(datetime.datetime.now()).strftime('%d-%m-%Y')
            rideobj.ride_time=(datetime.datetime.now()).strftime('%I:%M:%p')
            rideobj.completion_status='False'
            rideobj.ride_otp=random.randint(5000,9000)
            rideobj.save()
            request.session['ride']=rideobj.ride_otp

            return redirect('journey')
        else:
            return redirect('show_rides')


    return render(request,'driver_accept.html')


def journey(request):
    driver=Driver.objects.get(driver_id=request.session['ride.driver_id'])
    if request.method=='POST':
        rideobj=Ride.objects.get(ride_otp=request.session['ride'])
        rideobj.completion_status='True'
        rideobj.save()
        return redirect(payment_ride)
    return render(request,'journey.html',{'driver':driver})
def ride_his(request):
    if request.method=='POST':
        custobj=Customer.objects.get(customer_id=request.session['custobj'])
        rides=Ride.objects.filter(customer=custobj)
        payments=Payment.objects.filter(customer=custobj)
        ride_pay=[]
        for i in range(0,len(rides)):
            for j in range(0,len(payments)):
                
                if(rides[i].completion_status=='False' or rides[i].completion_status=='FALSE'):
                    ride_pay.append([rides[i]])
                    break
                else:
                    if(rides[i].driver==payments[j].driver and rides[i].vehicle_plate==payments[j].vehicle_plate):
                        ride_pay.append([rides[i],payments[j]])
        return render(request,'ride_his.html',{'rides':ride_pay})
def cancel_ride(request):
    if request.method=='POST':
        rideobj=Ride.objects.get(ride_otp=request.POST['rideotp'])
        rideobj.delete()
        return render(request,'cancel_ride.html')


def ratings(request):
    rideobj=Ride.objects.get(ride_otp=request.session['ride'])
    if request.method=='POST':
        if(request.POST['rating']!=-1):
            rideobj.rating=request.POST['rating']
            rideobj.save()
        return redirect('home')
    return render(request,'ratings.html')
def driver_his(request):
    if request.method=='POST':
        driver_obj=Driver.objects.get(driver_id=request.POST['driver_id'])
        rides=Ride.objects.filter(driver=driver_obj)
        payments=Payment.objects.filter(driver=driver_obj)
        ride_pay=[]
        for i in range(0,len(rides)):
            for j in range(0,len(payments)):
                
                if(rides[i].completion_status=='False' or rides[i].completion_status=='FALSE'):
                    ride_pay.append([rides[i]])
                    break
                else:
                    if(rides[i].customer==payments[j].customer and rides[i].vehicle_plate==payments[j].vehicle_plate):
                        ride_pay.append([rides[i],payments[j]])
        return render(request,'driver_his.html',{'ridepay':ride_pay})