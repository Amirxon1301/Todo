from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "kurs"]
    search_fields = ["ism"]
    list_filter = ["kurs"]
    list_display_links = ["ism"]

@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display = ["id", "sarlavha", "bajarilgan"]
    search_fields = ["sarlavha"]
    list_filter = ["bajarilgan"]
    list_display_links = ["sarlavha"]


# admin.site.register(Student)
# admin.site.register(Reja)
