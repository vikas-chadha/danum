from django.contrib import admin
from .models import ContactFormSubmission

@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

