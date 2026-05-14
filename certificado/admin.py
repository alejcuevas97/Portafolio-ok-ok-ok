from django.contrib import admin
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issued_date', 'active', 'order')
    list_filter = ('active', 'issuer')
    search_fields = ('title', 'issuer', 'description')
    ordering = ('-issued_date', 'order')
    fields = ('title', 'issuer', 'issued_date', 'description', 'credential_url', 'order', 'active')
