from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20,unique=True)
    duration=models.CharField(max_length=20)
    discription=models.TextField()
    image=models.FileField()    
    def __str__(self):
        return self.course_name


class YourModel(models.Model):
    name = models.CharField(max_length=255)
    time = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Staff(models.Model):
    emp_id=models.CharField(max_length=20)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    salary=models.IntegerField()
    password=models.TextField()
    doj=models.DateField()
    dor=models.DateField(null=True)
    possition=models.CharField(max_length=20)
    
class Faculty_Courses(models.Model):
    faculty=models.ForeignKey(Staff,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)



class student(models.Model):
    addmission_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    fee=models.IntegerField()
    paid_fee=models.IntegerField()
    phno=models.BigIntegerField()
    password=models.TextField()
    doj=models.DateField()

    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)


class Batch_times(models.Model):
    start_time=models.TimeField()
    end_time=models.TimeField()
    





    

    





