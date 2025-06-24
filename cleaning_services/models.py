from django.db import models

class HeroSection(models.Model):
    subheading = models.CharField(max_length=255, blank=True, null=True)
    main_heading = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)

    def __str__(self):
        return f"Hero Section: {self.main_heading or 'No Heading'}"


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
    

class AboutInfo(models.Model):
    welcome_subheading = models.CharField(max_length=100, blank=True, null=True)
    welcome_heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    years_experience = models.IntegerField(null=True, blank=True)
    happy_customers = models.IntegerField(null=True, blank=True)
    service_deliver = models.IntegerField(null=True, blank=True)
    working_hours = models.CharField(max_length=50, null=True, blank=True)
    saturday_hours = models.CharField(max_length=50, null=True, blank=True)
    vacation_days = models.TextField(default="All Sunday Days\nAll Official Holidays")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "About Info"

    def __str__(self):
        return f"About Info: {self.welcome_heading or 'No Heading'}"

class EmergencyContact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Emergency Contacts"
    
    def __str__(self):
        return f"Emergency Contact: {self.phone}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    
    def __str__(self):
        return self.title
    
class IntroSection(models.Model):
    video_file = models.FileField(upload_to='intro_videos/', null=True, blank=True)

    def __str__(self):
        return f"Intro Section: {self.video_file.name if self.video_file else 'No Video'}"

class Footer(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='footer_logos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name