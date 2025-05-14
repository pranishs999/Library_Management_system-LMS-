from django.contrib import admin
from .models import Book, Patron, Borrow

# Register your models here.
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Patron)