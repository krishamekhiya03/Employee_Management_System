from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null= False)
    last_name = models.CharField(max_length=100, null=False)
    Date_Of_Birth =models.DateField(max_length=100, null=False)
    email =models.EmailField(max_length=100, null=False,unique=True)
    phone_number =models.CharField(max_length=10,null=False,unique=True)
    address =models.TextField(max_length=300,null=False)

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" %(self.first_name,self.last_name,self.Date_Of_Birth,self.email,self.phone_number,self.address)