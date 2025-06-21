from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='appointments')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Appointment for {self.name} on {self.date} at {self.time}'
    

class CompanyInfo(models.Model):
    welcome_subheading = models.CharField(max_length=100, default="Welcome to Cleaning Company")
    welcome_heading = models.CharField(max_length=200, default="Let's make you fresher than ever")
    description = models.TextField(default="Far far away, behind the word mountains...")
    image = models.ImageField(upload_to='company_images/', default='company_images/default.jpg')
    
    class Meta:
        verbose_name_plural = "Company Info"

    def __str__(self):
        return f"{self.welcome_heading} - {self.welcome_subheading}"

class BusinessHours(models.Model):
    monday_friday_hours = models.CharField(max_length=50, default="9am to 20 pm")
    saturday_hours = models.CharField(max_length=50, default="9am to 17 pm")
    vacation_days = models.TextField(default="All Sunday Days\nAll Official Holidays")

    class Meta:
        verbose_name_plural = "Business Hours"

    def __str__(self):
        return f"Business Hours: {self.monday_friday_hours}, {self.saturday_hours}"

class EmergencyContact(models.Model):
    phone = models.CharField(max_length=20, default="(+01) 123 456 7890")

    class Meta:
        verbose_name_plural = "Emergency Contacts"
    
    def __str__(self):
        return f"Emergency Contact: {self.phone}"

class CounterStat(models.Model):
    years_experience = models.IntegerField(default=45)
    happy_customers = models.IntegerField(default=2342)
    service_deliver = models.IntegerField(default=30)

    class Meta:
        verbose_name_plural = "Counter Statistics"

    def __str__(self):  
        return f"Experience: {self.years_experience} years, Customers: {self.happy_customers}, Services Delivered: {self.service_deliver}"