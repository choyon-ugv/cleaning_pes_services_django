from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import AboutInfo, EmergencyContact, Service, Staff, Testimonial, Project, HeroSection, IntroSection, Footer

def home_view(request):
    hero_section = HeroSection.objects.first()
    contact = EmergencyContact.objects.last()
    about_info = AboutInfo.objects.first()
    emergency_contact = EmergencyContact.objects.first()
    services = Service.objects.all()
    staff_list = Staff.objects.all()
    pest_services = Service.objects.filter(category='pest_control').order_by('created_at')
    cleaning_services = Service.objects.filter(category='cleaning').order_by('created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')[:5] 
    projects = Project.objects.all()
    intro_section = IntroSection.objects.first()
    footer = Footer.objects.first()

    
    context = {
        'hero_section': hero_section,
        'contact': contact,
        'about_info': about_info,
        'emergency_contact': emergency_contact,
        'services': services,
        'staff_list': staff_list,
        'pest_services': pest_services,
        'cleaning_services': cleaning_services,
        'testimonials': testimonials,
        'projects': projects,
        'intro_section': intro_section,
        'footer': footer,
    }
    return render(request, 'index.html', context)

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def about_view(request):
    contact = EmergencyContact.objects.last()
    about_info = AboutInfo.objects.first()
    emergency_contact = EmergencyContact.objects.first()
    services = Service.objects.all()
    staff_list = Staff.objects.all()
    pest_services = Service.objects.filter(category='pest_control').order_by('created_at')
    cleaning_services = Service.objects.filter(category='cleaning').order_by('created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')[:5]
    intro_section = IntroSection.objects.first()

    context = {
        'contact': contact,
        'about_info': about_info,
        'emergency_contact': emergency_contact,
        'services': services,
        'staff_list': staff_list,
        'pest_services': pest_services,
        'cleaning_services': cleaning_services,
        'testimonials': testimonials,
        'intro_section': intro_section,
    }

    return render(request, 'about.html', context)

def services_view(request):
    services = Service.objects.all()
    pest_services = Service.objects.filter(category='pest_control').order_by('created_at')
    cleaning_services = Service.objects.filter(category='cleaning').order_by('created_at')
    context = {
        'services': services,
        'pest_services': pest_services,
        'cleaning_services': cleaning_services,
    }

    return render(request, 'services.html', context)

def contact_view(request):
    return render(request, 'contact.html')

