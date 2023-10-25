from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self,first_name, surname,username, email, password=None):
        if not email:
            raise ValueError("Put an email address")
        if not username:
            raise ValueError("Put an username")
        
        user = self.model(
            email = email,
            username = user,
            first_name = first_name,
            surname = surname,
        )
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self,first_name, surname,username, email, password=None):
        if not email:
            raise ValueError("Put an email address")
        if not username:
            raise ValueError("Put an username")
        
        user = self.create_user(
            email = self.normalize_email(email=email),
            username = user,
            password=password,
            first_name = first_name,
            surname = surname,
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff= True
        user.is_superadmin = True
        user.save(using=self.db)
        
        return user
    

class User(AbstractBaseUser):
    
    first_name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100,  blank=False)
    username = models.CharField(max_length=30, unique=True,  blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
        
class LegalPerson(models.Model):
    legal_person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="legal_person_User")
    born_date = models.CharField(max_length=10, blank=False)
    cpf = models.CharField(max_length=11, blank=False, primary_key=True)
    rg = models.CharField(max_length=9, blank=False)
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
    

class JuridicPerson(models.Model):
    juridic_person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="juridic_person_User")
    state_registration = models.CharField(max_length=11)
    open_date = models.CharField(max_length=10, blank=False)
    cnpj = models.CharField(max_length=14, primary_key=True)
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        
        
class Account(models.Model):
    agency = models.IntegerField()
    number = models.IntegerField()
    number_verificate = models.IntegerField()
    type_account = models.CharField(max_length=20)
    limit = models.IntegerField()
    active = models.BooleanField()
    legal_person = models.ForeignKey(LegalPerson, on_delete=models.CASCADE)
    juridic_person = models.ForeignKey(JuridicPerson, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.legal_person != None:
            super(LegalPerson, self).save(*args, **kwargs)
        else:
            super(JuridicPerson, self).save(*args, **kwargs)