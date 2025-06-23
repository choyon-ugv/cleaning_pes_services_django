from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import CompanyInfo, BusinessHours, EmergencyContact, CounterStat, Service, Staff, Testimonial, Project

def home_view(request):
    company_info = CompanyInfo.objects.first()
    business_hours = BusinessHours.objects.first()
    emergency_contact = EmergencyContact.objects.first()
    counter_stat = CounterStat.objects.first()
    services = Service.objects.all()
    staff_list = Staff.objects.all()
    pest_services = Service.objects.filter(category='pest_control').order_by('created_at')
    cleaning_services = Service.objects.filter(category='cleaning').order_by('created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')[:5] 
    projects = Project.objects.all()

    
    context = {
        'company_info': company_info,
        'business_hours': business_hours,
        'emergency_contact': emergency_contact,
        'counter_stat': counter_stat,
        'services': services,
        'staff_list': staff_list,
        'pest_services': pest_services,
        'cleaning_services': cleaning_services,
        'testimonials': testimonials,
        'projects': projects,
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

