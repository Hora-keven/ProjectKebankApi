from django.contrib import admin
from .models import *

admin.site.register(PhysicalPerson)
admin.site.register(JuridicPerson)

admin.site.register(User)
admin.site.register(Address)
admin.site.register(CreditCard)

admin.site.register(Account)
# Register your models here.


