from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Department, Doctor, Service, Appointment, ContactMessage
from django.contrib.auth.decorators import login_required

def home(request):
    services = Service.objects.all()[:6]
    doctors = Doctor.objects.filter(is_active=True)[:4]
    return render(request, 'home.html', {'services': services, 'doctors': doctors})

def about(request):
    return render(request, 'about.html')

def doctors(request):
    department_id = request.GET.get('department')
    search_query = request.GET.get('search')
    
    doctors = Doctor.objects.filter(is_active=True)
    if department_id:
        doctors = doctors.filter(department_id=department_id)
    if search_query:
        doctors = doctors.filter(name__icontains=search_query)
        
    departments = Department.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors, 'departments': departments})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        symptoms = request.POST.get('symptoms')
        
        department = Department.objects.get(id=department_id) if department_id else None
        doctor = Doctor.objects.get(id=doctor_id) if doctor_id else None
        
        appointment = Appointment.objects.create(
            patient_user=request.user if request.user.is_authenticated else None,
            patient_name=patient_name,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            symptoms=symptoms
        )
        messages.success(request, 'Appointment booked successfully!')
        return redirect('appointment_success', id=appointment.id)

    departments = Department.objects.all()
    doctors = Doctor.objects.filter(is_active=True)
    return render(request, 'appointment.html', {'departments': departments, 'doctors': doctors})

def appointment_success(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointment_success.html', {'appointment': appointment})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, phone=phone, subject=subject, message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
        
    return render(request, 'contact.html')

def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})
