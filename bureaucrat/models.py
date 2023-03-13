from django.db import models

# Create your models here.

class bureaucrat(models.Model):
    pName = models.CharField(max_length=100)
    pSurname = models.CharField(max_length=100)
    Dateofbirth = models.DateField(auto_now_add=True)
    Exam=models.CharField(max_length=100)
    joiningDate=models.DateField()

    
    def __str__(self):
        return self.pName
    
    class Meta:
        db_table = 'bureaucrat'
