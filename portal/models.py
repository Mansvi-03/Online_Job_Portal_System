from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, default="Pending")

    interview_date = models.DateField(null=True, blank=True)
    interview_time = models.TimeField(null=True, blank=True)
    interview_mode = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.candidate.name} applied for {self.job.title}"
