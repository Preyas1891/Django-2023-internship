from django.db import models
# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    pQty=models.IntegerField()
    pdescription=models.TextField(max_length=100,null=True)
    pstatus=models.BooleanField(default=True)
    pColor=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.pname

    class Meta:
        db_table='Product'


class Employees(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    salary=models.IntegerField()
    age=models.IntegerField()
    joiningDate=models.DateField()
    
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.name)

    class Meta:
        db_table='Employees'


class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    desc = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = 'categories'
        
    def __str__(self):
        return self.name





