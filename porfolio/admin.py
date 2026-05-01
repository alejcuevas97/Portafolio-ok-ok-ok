from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Project


# === Principio S (Single Responsibility) ===
class ProjectAdmin(admin.ModelAdmin):
    """Admin para gestionar proyectos del portafolio"""
    
    # Campos de solo lectura
    readonly_fields = ('created', 'update')
    
    # Campos a mostrar en la lista
    list_display = ('title', 'created', 'update', 'is_recent')
    
    # Campos para filtrar
    list_filter = ('created', 'update')
    
    # Búsqueda
    search_fields = ('title', 'descriptions')
    
    # Orden por defecto
    ordering = ('-created',)
    
    # Campos para crear/editar
    fieldsets = (
        (_('Información del Proyecto'), {
            'fields': ('title', 'descriptions', 'image', 'link')
        }),
        (_('Fechas'), {
            'fields': ('created', 'update'),
            'classes': ('collapse',),  # Colapsable
        }),
    )
    
    # Prepopulado de slug desde title (si existe)
    def is_recent(self, obj):
        """Muestra si el proyecto es reciente"""
        return obj.is_recent()
    is_recent.boolean = True
    is_recent.short_description = _('¿Reciente?')


# Registrar el modelo
admin.site.register(Project, ProjectAdmin)
