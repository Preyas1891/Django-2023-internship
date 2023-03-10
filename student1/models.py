from django.db import models

# Create your models here.
class student1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    marks=models.IntegerField()
    age=models.IntegerField()
    joiningDate=models.DateField()
    
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.name)

    class Meta:
        db_table='Student1'

