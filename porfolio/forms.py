from django import forms
from .models import Project


# === Principio S (Single Responsibility) ===
# Separar la lógica de estilos en una clase
class FormStyleMixin:
    """Mixin encargado únicamente de aplicar estilos Tailwind"""
    
    # Atributos CSS reutilizables
    INPUT_CLASS = 'w-full rounded-3xl border border-gray-300 px-4 py-3 focus:border-blue-500 focus:ring-2 focus:ring-blue-100'
    TEXTAREA_CLASS = 'w-full rounded-3xl border border-gray-300 px-4 py-3 focus:border-blue-500 focus:ring-2 focus:ring-blue-100'
    
    def apply_input_styles(self, attrs=None, placeholder=''):
        """Aplica estilos a campos de entrada"""
        if attrs is None:
            attrs = {}
        return {
            **attrs,
            'class': self.INPUT_CLASS,
            'placeholder': placeholder,
        }
    
    def apply_textarea_styles(self, attrs=None, rows=5, placeholder=''):
        """Aplica estilos a áreas de texto"""
        if attrs is None:
            attrs = {}
        return {
            **attrs,
            'class': self.TEXTAREA_CLASS,
            'rows': rows,
            'placeholder': placeholder,
        }


# === Principio O (Open/Closed) ===
# Formulario extensible sin necesidad de modificar la clase base
class ProjectForm(FormStyleMixin, forms.ModelForm):
    """Formulario para crear/editar proyectos"""
    
    class Meta:
        model = Project
        fields = ['title', 'descriptions', 'image', 'link']
        labels = {
            'title': 'Título',
            'descriptions': 'Descripción',
            'image': 'Imagen del proyecto',
            'link': 'Enlace de demostración',
        }
        widgets = {
            'title': forms.TextInput(
                attrs=FormStyleMixin().apply_input_styles(
                    placeholder='Título del proyecto'
                )
            ),
            'descriptions': forms.Textarea(
                attrs=FormStyleMixin().apply_textarea_styles(
                    rows=5,
                    placeholder='Descripción breve del proyecto'
                )
            ),
            'link': forms.URLInput(
                attrs=FormStyleMixin().apply_input_styles(
                    placeholder='https://ejemplo.com'
                )
            ),
            'image': forms.ClearableFileInput(
                attrs={'class': 'w-full'}
            ),
        }
    
    def clean(self):
        """Validación a nivel de formulario"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        descriptions = cleaned_data.get('descriptions')
        
        if title and len(title) < 5:
            self.add_error('title', 'El título debe tener al menos 5 caracteres')
        
        if descriptions and len(descriptions) < 20:
            self.add_error('descriptions', 'La descripción debe tener al menos 20 caracteres')
        
        return cleaned_data
