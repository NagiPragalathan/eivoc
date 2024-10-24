from django.db import models
from django.contrib.auth.models import User

class StudentCategory(models.Model):
    UNDERGRADUATE = 'Undergraduate'
    POSTGRADUATE = 'Postgraduate'
    CATEGORY_CHOICES = [
        (UNDERGRADUATE, 'Undergraduate'),
        (POSTGRADUATE, 'Postgraduate'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    bona_fide = models.FileField(upload_to='bona_fide/', null=True, blank=True)

    def __str__(self):
        return self.category

class UserProfile(models.Model):
    PREFIX_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    institute = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    highest_education = models.CharField(max_length=255)
    category = models.CharField(max_length=10)
    student_category = models.OneToOneField(StudentCategory, null=True, blank=True, on_delete=models.CASCADE)
    regular_category = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
