from django.contrib import admin

# Register your models here.
from .models import Order, Smsa,Aramex,SPL
admin.site.register(Order)
admin.site.register(Smsa)
admin.site.register(Aramex)
admin.site.register(SPL)