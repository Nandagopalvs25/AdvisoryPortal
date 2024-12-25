from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    is_advisor=models.BooleanField(default=False)
    USER_TYPES = [
        ('admin', 'Admin'),
        ('advisor', 'Advisor'),
        ('student', 'Student'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    def __str__(self):
        return self.username
    
    
    
class College(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.college.name})"

class Batch(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name='batches', on_delete=models.CASCADE)
    batch_id=models.CharField(max_length=15)
    gdrive_folder_url=models.CharField(max_length=300,blank=True)

    def __str__(self):
        return f"{self.name} ({self.department.name})"
    
class Advisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='advisor_profile')
    department = models.ForeignKey(Department, related_name='advisors', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username



class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    batch = models.ForeignKey(Batch, related_name='students', on_delete=models.CASCADE)   
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)  # New field
    admission_number=models.CharField(max_length=30,null=True)
    roll_number=models.CharField(max_length=20,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,default="Male")
    phone_no=models.CharField(null=True,blank=True,max_length=20);
    guardian=models.CharField(max_length=40,null=True,blank=True);
    guardian_no=models.CharField(null=True,blank=True,max_length=20);
    teacher_remarks=models.CharField(null=True,blank=True,max_length=200);
    gdrive_folder_id=models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.user.username

    

    
class Internships(models.Model):
     user = models.ForeignKey(CustomUser,related_name="internship", on_delete=models.CASCADE,null=False)
     name=models.CharField(max_length=50)
     company=models.CharField(max_length=50)
     no_of_days=models.IntegerField()
     start_date=models.CharField(max_length=50)
     end_date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
     is_approved=models.BooleanField(default=False)
     ktu_points=models.IntegerField(blank=True,null=True)

       
     def __str__(self):
          return self.name


    
class Mooc(models.Model):
     user = models.ForeignKey(CustomUser,related_name="mooc", on_delete=models.CASCADE,null=False)
     course_title=models.CharField(max_length=100)
     course_type=models.CharField(max_length=50)
     start_date=models.CharField(max_length=50)
     end_date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
     is_approved=models.BooleanField(default=False)
     ktu_points=models.IntegerField(blank=True,null=True)
     def __str__(self):
          return self.course_title
     


class Extracurriculur(models.Model):
     user = models.ForeignKey(CustomUser,related_name="extrac", on_delete=models.CASCADE,null=False) 
     event_title=models.CharField(max_length=100)
     event_organiser=models.CharField(max_length=70)
     event_date=models.CharField(max_length=20)
     event_type = models.CharField(max_length=30)
     event_level = models.CharField(max_length=30)
     event_position=models.CharField(max_length=30)
     file_url=models.CharField(max_length=300)
     is_approved=models.BooleanField(default=False)
     ktu_points=models.IntegerField(blank=True,null=True)

     def __str__(self):
          return self.event_title
     


class Workshops(models.Model):
     user = models.ForeignKey(CustomUser,related_name="workshops", on_delete=models.CASCADE,null=False)
     name=models.CharField(max_length=50)
     organiser=models.CharField(max_length=100)
     no_of_days=models.IntegerField()
     date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
     is_approved=models.BooleanField(default=False)
     ktu_points=models.IntegerField(blank=True,null=True)

     def __str__(self):
          return self.name





