from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class vaccineDetails(models.Model):
    DOSE = (
        ('None','None'),
        ('Single','Single'),
        ('Both','Both'),        
    )
    CIRCLE = (
        ('Agra','Agra'),
        ('Ahmedabad','Ahmedabad'),
        ('Bangalore','Bangalore'), 
        ('Bhopal','Bhopal'),
        ('Bhubaneswar','Bhubaneswar'),
        ('Chandigarh','Chandigarh'),
        ('Chennai','Chennai'),
        ('Delhi','Delhi'),
        ('Guwahati','Guwahati'),
        ('Headoffice','Headoffice'),
        ('Hyderabad','Hyderabad'),        
        ('Hubballi','Hubballi'),
        ('Jaipur','Jaipur'),
        ('Karnal','Karnal'),        
        ('Kolkata','Kolkata'), 
        ('Lucknow','Lucknow'),
        ('Madurai','Madurai'),
        ('Mangalore','Mangalore'),
        ('Manipal','Manipal'),
        ('Mumbai','Mumbai'),
        ('Patna','Patna'),
        ('Pune','Pune'),
        ('Ranchi','Ranchi'),
        ('Trivandrum','Trivandrum'), 
        ('Vijayawada','Vijayawada'),     
    )
    staff_name = models.CharField(max_length=50)
    staff_no = models.PositiveIntegerField(unique=True)
    dp_code = models.PositiveIntegerField()
    branch_name = models.CharField(max_length=50)
    ro_code = models.PositiveIntegerField()
    circle_name = models.CharField(max_length=11, choices=CIRCLE)
    vaccinated = models.CharField(max_length=6, choices=DOSE)
    vaccinated_date = models.DateTimeField()
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', #^\+?1?\d{9,12}$',
                                 message="Valid Phone number must be entered !!")
    contact_number = models.CharField(validators=[phone_regex], max_length=10)
    submit_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Vaccinated Details"

    def __str__(self):
        return self.staff_name