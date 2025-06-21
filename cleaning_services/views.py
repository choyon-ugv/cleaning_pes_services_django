from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import CompanyInfo, BusinessHours, EmergencyContact, CounterStat

def home_view(request):
    company_info = CompanyInfo.objects.first()
    business_hours = BusinessHours.objects.first()
    emergency_contact = EmergencyContact.objects.first()
    counter_stat = CounterStat.objects.first()
    
    context = {
        'company_info': company_info,
        'business_hours': business_hours,
        'emergency_contact': emergency_contact,
        'counter_stat': counter_stat,
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

