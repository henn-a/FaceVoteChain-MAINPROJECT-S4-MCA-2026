from django.db import models

# Create your models here.

class login_table(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class student_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    Fname= models.CharField(max_length=50)
    Lname= models.CharField(max_length=50)
    DOB= models.DateField()
    gender= models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    RollNo=models.CharField(max_length=50)
    phone_no= models.BigIntegerField()
    image= models.FileField()

class course_table(models.Model):
    course= models.CharField(max_length=50)
    description= models.CharField(max_length=100)

class electiondate_table(models.Model):
    post= models.CharField(max_length=50)
    date= models.DateField()
    election_date= models.DateField()
    details= models.CharField(max_length=50)

class nominees_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    ELECTION_DATE = models.ForeignKey(electiondate_table, on_delete=models.CASCADE)
    date = models.DateField()
    status= models.CharField(max_length=50)

class complaint_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    complaint= models.CharField(max_length=50)
    date= models.DateField()
    reply= models.CharField(max_length=50)

class Feedback_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)
    date = models.DateField()


class notification_table(models.Model):
    Notification = models.CharField(max_length=50)
    date = models.DateField()


class result_table(models.Model):
    NOMINEES= models.ForeignKey(nominees_table, on_delete=models.CASCADE)
    STUDENT= models.ForeignKey(student_table, on_delete=models.CASCADE)
    vote= models.IntegerField()

class electioncoordinator_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # Lname = models.CharField(max_length=50)
    DOB = models.DateField()
    image = models.FileField()
    phone_no = models.BigIntegerField()
    Email = models.CharField(max_length=100)