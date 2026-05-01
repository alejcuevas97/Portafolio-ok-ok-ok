from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Project


# === Principio S (Single Responsibility) ===
# Servicio separado para la lógica de negocios
class ProjectService:
    """Encargado únicamente de la lógica de proyectos"""
    
    @staticmethod
    def get_all_projects():
        """Obtiene todos los proyectos del base de datos"""
        return Project.objects.all().order_by('-created')
    
    @staticmethod
    def get_project_count():
        """Obtiene el conteo de proyectos"""
        return Project.objects.count()


# === Principio O (Open/Closed) ===
# Usar vistas genéricas de Django para ser extensibles
class ProjectListView(ListView):
    """Vista genérica para listar proyectos - extensible sin modificar"""
    model = Project
    template_name = 'proyectos.html'
    context_object_name = 'proyectos'
    paginate_by = 12
    
    def get_queryset(self):
        """Usa el servicio para obtener proyectos (DIP)"""
        return ProjectService.get_all_projects()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_projects'] = ProjectService.get_project_count()
        return context


# === Compatibilidad con URL antigua ===
# Mantén esta función por compatibilidad, pero usa LinkedView
def Proyectos(request):
    """Vista funcional - DEPRECADA. Usa ProjectListView en urls.py"""
    service = ProjectService()
    proyectos = service.get_all_projects()
    context = {
        'proyectos': proyectos,
    }
    return render(request, 'proyectos.html', context)
