from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('pest_control', 'Pest Control'),
        ('cleaning', 'Cleaning'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='cleaning')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff_images/', blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.position}"
    
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
    welcome_subheading = models.CharField(max_length=100, blank=True, null=True)
    welcome_heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Company Info"

    def __str__(self):
        return f"{self.welcome_heading} - {self.welcome_subheading}"

class BusinessHours(models.Model):
    working_hours = models.CharField(max_length=50, null=True, blank=True)
    saturday_hours = models.CharField(max_length=50, null=True, blank=True)
    vacation_days = models.TextField(default="All Sunday Days\nAll Official Holidays")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Business Hours"

    def __str__(self):
        return f"Business Hours: {self.working_hours}, {self.saturday_hours}"

class EmergencyContact(models.Model):
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Emergency Contacts"
    
    def __str__(self):
        return f"Emergency Contact: {self.phone}"

class CounterStat(models.Model):
    years_experience = models.IntegerField()
    happy_customers = models.IntegerField()
    service_deliver = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Counter Statistics"

    def __str__(self):  
        return f"Experience: {self.years_experience} years, Customers: {self.happy_customers}, Services Delivered: {self.service_deliver}"
    
