from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self,first_name, surname, username, email, password=None):
        if not email:
            raise ValueError("Put an email address")
        if not username:
            raise ValueError("Put an username")
        
        user = self.model(
            email = email,
            username = username,
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
            username = username,
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
    username = models.CharField(max_length=30, unique=True,  blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin =  models.BooleanField(default=False)
    is_active =  models.BooleanField(default=False)
    is_staff=  models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [ "first_name", "surname", "email"]
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
        
class LegalPerson(models.Model):
    legal_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="legal_person_User")
    born_date = models.CharField(max_length=10, blank=False)
    cpf = models.CharField(max_length=11, blank=False, primary_key=True)
    rg = models.CharField(max_length=9, blank=False)
    
    def save(self, *args, **kwargs):
        super(LegalPerson, self).save(*args, **kwargs)
    

class JuridicPerson(models.Model):
    juridic_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="juridic_person_User")
    state_registration = models.CharField(max_length=11)
    open_date = models.CharField(max_length=10, blank=False)
    cnpj = models.CharField(max_length=14, primary_key=True)
    
    def save(self, *args, **kwargs):
        super(JuridicPerson, self).save(*args, **kwargs)
        
        
class Account(models.Model):
    agency = models.IntegerField(blank=True)
    number = models.IntegerField(blank=True)
    number_verificate = models.IntegerField(blank=True)
    type_account = models.CharField(max_length=20)
    limit = models.DecimalField(max_digits=10, decimal_places=2 )
    active = models.BooleanField(default=True)
    legal_person = models.ForeignKey(LegalPerson, on_delete=models.CASCADE,  null=True, related_name="legal_person_LegalPerson")
    juridic_person = models.ForeignKey(JuridicPerson, on_delete=models.CASCADE, null=True, related_name="juridic_person_JuridicPerson")
    
    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
 