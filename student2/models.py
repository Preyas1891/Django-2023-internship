from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration=models.IntegerField()
    fees=models.IntegerField()

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name
genderChoice =(("Male","male"),("Female","Female"))
class student2(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100,choices=genderChoice)
    class Meta:
        db_table ='student2'

    def __str__(self):
         return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'faculty'

    def __str__(self):
        return self.name
    

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    class Meta:
        db_table ='subjects'

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    name = models.CharField(max_length=100)
    Faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Subjects=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'batch'

    def __str__(self):
        return self.name
    


    

