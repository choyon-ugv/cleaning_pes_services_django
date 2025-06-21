from django import forms
from .models import Appointment, Service

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'address', 'service', 'message']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()
        self.fields['service'].empty_label = "Select Services"
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone umber', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Your Address', 'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your Message', 'class': 'form-control'})