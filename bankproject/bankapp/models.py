
from django.urls import reverse
from django.db import models

# Create your models here.
class Branch(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='branch'
        verbose_name_plural='branches'
    def get_url(self):
        return reverse('bankapp:branch_by_dist',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class Sbranch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    available=models.BooleanField(default=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    class Meta:
        ordering=('name',)
        verbose_name='sbranch'
        verbose_name_plural='sbranchs'
    def __str__(self):
        return '{}'.format(self.name)

class RegForm(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField(auto_now_add=True)
    email=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=300)
    district=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True ,null=True)
    city = models.ForeignKey(Sbranch, on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    materials_provided = models.CharField(max_length=50)
    def __str__(self):
        return self.name