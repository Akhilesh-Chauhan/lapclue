from django.db import models

# Create your models here.

class SignUp(models.Model):
    name=models.CharField(max_length=150)
    phoneno=models.IntegerField()
    email=models.CharField(primary_key=True,max_length=200)
    password=models.CharField(max_length=20)
    atype=models.CharField(max_length=20,default='customer')

class AcountDetails(models.Model):
    name=models.CharField(max_length=150)
    phoneno=models.IntegerField()
    email=models.CharField(primary_key=True,max_length=200)
    image=models.ImageField(upload_to='profileimages')
    dateofbirth=models.CharField(max_length=64)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=300)
    pincode=models.IntegerField(default=000000)

CATEGORY=(('Gaming','Gaming'),('Business','Business'),('Professional','Professional'),('Student','Student'))
class AllProducts(models.Model):
    id=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    modelno=models.CharField(unique=True ,max_length=100)
    image=models.ImageField(upload_to='laptopimages')
    category=models.CharField(choices=CATEGORY,max_length=20)
    price=models.CharField(max_length=30)
    screen=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    graphics=models.CharField(max_length=200)
    memory=models.CharField(max_length=50, blank=True)
    storage=models.CharField(max_length=100, blank=True)
    ioports=models.CharField(max_length=200, blank=True)
    dimensions=models.CharField(max_length=200, blank=True)
    description=models.TextField()
    def __str__(self):
        return self.cname

class Cart(models.Model):
    id=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    modelno=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=800)
    category=models.CharField(max_length=150)
    image=models.ImageField(upload_to='cart/pictures',default='')
    status=models.CharField(default='unordered',max_length=100)
    
    def __str__(self):
        return self.cname
    

    class Meta:
        db_table='Cart'
