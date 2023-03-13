from django.db import models

# Create your models here.
class food(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    desc=models.TextField()
   

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'food'