from django.db import models
from django.contrib.auth.models import AbstractUser



class College(models.Model):
     college_name=models.CharField(max_length=200)
     college_address=models.CharField(max_length=350)

     def __str__(self) -> str:
          return self.college_name


class Department(models.Model):
     dept_name=models.CharField(max_length=150)
     college = models.ForeignKey(College,related_name="college", on_delete=models.CASCADE,null=True)
      
     def __str__(self) -> str:
          return self.dept_name


class Batch(models.Model):
     batch_id=models.CharField(max_length=15)
     gdrive_folder_url=models.CharField(max_length=300,blank=True)
     department = models.ForeignKey(Department,related_name="department", on_delete=models.CASCADE,null=True)

     def __str__(self):
        return self.batch_id
    

class CustomUser(AbstractUser):
    roll_number=models.CharField(max_length=20,null=True)
    admission_number= models.IntegerField(null=True)
    dob = models.DateField(null=True)
    is_advisor=models.BooleanField(default=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ROLES = (
        ('S', 'Student'),
        ('A', 'Advisor'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="M")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,null=True)
    department=models.OneToOneField(Department,on_delete=models.CASCADE,null=True)
    role = models.CharField(max_length=7,choices=ROLES,default="S")
    phone_no=models.CharField(null=True,blank=True,max_length=20);
    guardian=models.CharField(max_length=40,null=True,blank=True);
    guardian_no=models.CharField(null=True,blank=True,max_length=20);
    teacher_remarks=models.CharField(null=True,blank=True,max_length=200);
    student_name=models.CharField(max_length=40,null=True,blank=True)
    # add additional fields in here

    def __str__(self):
        return self.username
    


    
class Internships(models.Model):
     user = models.ForeignKey(CustomUser,related_name="internship", on_delete=models.CASCADE,null=False)
     name=models.CharField(max_length=50)
     company=models.CharField(max_length=50)
     no_of_days=models.IntegerField()
     start_date=models.CharField(max_length=50)
     end_date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
       
     def __str__(self):
          return self.name


    
class Mooc(models.Model):
     user = models.ForeignKey(CustomUser,related_name="mooc", on_delete=models.CASCADE,null=False)
     course_title=models.CharField(max_length=100)
     course_type=models.CharField(max_length=50)
     start_date=models.CharField(max_length=50)
     end_date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
       
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
     def __str__(self):
          return self.event_title
     


class Workshops(models.Model):
     user = models.ForeignKey(CustomUser,related_name="workshops", on_delete=models.CASCADE,null=False)
     name=models.CharField(max_length=50)
     organiser=models.CharField(max_length=100)
     no_of_days=models.IntegerField()
     date=models.CharField(max_length=50)
     file_url=models.CharField(max_length=300)
       
     def __str__(self):
          return self.name





