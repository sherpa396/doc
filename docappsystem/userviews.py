from django.shortcuts import render, redirect, HttpResponse
from dasapp.models import *
import random
import re
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .scheduler import FCFSQueueScheduler  # Import the scheduler
from dasapp.models import Appointment, DoctorReg


def USERBASE(request):
    return render(request, "userbase.html", context)

def PAYMENT(request):
    if request.method == "POST":
        patient_name = request.POST.get('patientname')
        amount = request.POST.get('amount')
        cardnumbers = request.POST.get('cardnumber')
        expirydate = request.POST.get('expirydate')
        cvv = request.POST.get('cvv')

        print('Patient Name: ', patient_name, '\nAmount: ', amount,
            '\nCard Numbers: ', cardnumbers, '\nExpiry Date: ', expirydate, '\nCVV: ', cvv)
    
    # Save data to db and display a success message
        payment_details = Payment(
                patient_name=patient_name,
                amount=amount,
                cardnumbers=cardnumbers,
                expirydate=expirydate,
                cvv=cvv,
            )
        payment_details.save()
        
        messages.success(request, "Payment Successful !!")
        return redirect("appointment")

def Index(request):
    doctorview = DoctorReg.objects.all()
    page = Page.objects.all()

    context = {
        "doctorview": doctorview,
        "page": page,
    }
    return render(request, "index.html", context)


scheduler = FCFSQueueScheduler()  # Instantiate scheduler globally

def create_appointment(request):
    doctorview = DoctorReg.objects.all()
    page = Page.objects.all()

    if request.method == "POST":
        appointment_data = {
            'doctor_id': int(request.POST.get("doctor_id")),
            'patient_name': request.POST.get("fullname"),
            'email': request.POST.get("email"),
            'phone': request.POST.get("mobilenumber"),
            'preferred_date': request.POST.get("date_of_appointment"),
        }
        
        # Add to scheduler queue
        appointment_id = scheduler.add_to_queue(appointment_data)
        
        # Process the queue
        processed = scheduler.process_queue()
        
        # Retrieve our appointment from the processed list
        our_appointment = next((a for a in processed if a['appointment_id'] == appointment_id), None)
        
        if our_appointment:
            # Create and save appointment in database
            new_appointment = Appointment(
                appointmentnumber=appointment_id,
                fullname=appointment_data['patient_name'],
                email=appointment_data['email'],
                mobilenumber=appointment_data['phone'],
                date_of_appointment=our_appointment['date'],
                time_of_appointment=our_appointment['time'],
                doctor_id_id=appointment_data['doctor_id'],
                # status=AppointmentState.EXIT
            )
            new_appointment.save()
            
            messages.success(
                request,
                f"Appointment scheduled for {our_appointment['date']} at {our_appointment['time']}"
            )
        else:
            messages.error(request, "Could not schedule appointment at this time.")
        
        return redirect("appointment")
    
    context = {
        "doctorview": doctorview,"page": page
    }
    return render(request, "appointment.html", context)




def User_Search_Appointments(request):
    page = Page.objects.all()
    
    if request.method == "GET":
        query = request.GET.get('query', '')
        
        if query:
            # Check if the query is a valid email or 10-digit phone number
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Regex for validating an email
            phone_pattern = r'^\d{10}$'  # Regex for exactly 10 digits
            
            # Validate email or phone number
            if re.match(email_pattern, query):  # If it's a valid email
                patient = Appointment.objects.filter(email=query)
                messages.info(request, "Search results for email: " + query)
            elif re.match(phone_pattern, query):  # If it's a valid 10-digit phone number
                patient = Appointment.objects.filter(mobilenumber=query)
                messages.info(request, "Search results for phone number: " + query)
            else:
                # If it doesn't match any pattern
                patient = None
                messages.error(request, "Please enter a valid email or 10-digit phone number.")
            
            context = {'patient': patient, 'query': query, 'page': page}
            return render(request, 'search-appointment.html', context)
        
        else:
            messages.error(request, "No query entered. Please provide an email or phone number.")
            context = {'page': page}
            return render(request, 'search-appointment.html', context)
    
    # If the request method is not GET
    context = {'page': page}
    return render(request, 'search-appointment.html', context)



def View_Appointment_Details(request, id):
    page = Page.objects.all()
    specialization = Specialization.objects.all()
    patientdetails = Appointment.objects.filter(id=id).select_related('doctor_id')  # Use select_related for optimization
    context = {
        'patientdetails': patientdetails,
        'page': page,
        'id': id,
    }

    return render(request, 'user_appointment-details.html', context)