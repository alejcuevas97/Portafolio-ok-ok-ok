"""
=== PRINCIPIO D: DEPENDENCY INVERSION ===

Este módulo encapsula la lógica de negocios separada del acceso a datos.
Las vistas dependen de este servicio, no directamente de los modelos.
"""

from django.db.models import QuerySet
from django.core.cache import cache
from .models import Project


class ProjectService:
    """
    Servicio de proyectos - encapsular lógica de negocio.
    
    Beneficios SOLID:
    - Single Responsibility: Solo responsable de la lógica de proyectos
    - Dependency Inversion: Las vistas usan este servicio, no acceden directamente a BD
    - Open/Closed: Fácil de extender sin modificar vistas existentes
    """
    
    CACHE_KEY = 'projects_all'
    CACHE_TIMEOUT = 3600  # 1 hora
    
    @staticmethod
    def get_all_projects(active_only: bool = True) -> QuerySet:
        """
        Obtiene todos los proyectos.
        
        Args:
            active_only: Si True, solo retorna proyectos activos
            
        Returns:
            QuerySet de proyectos ordenados por fecha de creación
        """
        queryset = Project.objects.all()
        if active_only:
            queryset = queryset.filter(is_active=True)
        return queryset.order_by('-created')
    
    @staticmethod
    def get_project_by_slug(slug: str) -> Project:
        """
        Obtiene un proyecto por su slug.
        
        Args:
            slug: Identificador único del proyecto
            
        Returns:
            Instancia de Project o None
        """
        return Project.objects.filter(slug=slug, is_active=True).first()
    
    @staticmethod
    def get_recent_projects(limit: int = 6) -> QuerySet:
        """
        Obtiene los proyectos más recientes.
        
        Args:
            limit: Número máximo de proyectos a retornar
            
        Returns:
            QuerySet con los proyectos más recientes
        """
        return ProjectService.get_all_projects()[:limit]
    
    @staticmethod
    def get_project_count() -> int:
        """Retorna el número total de proyectos activos"""
        return Project.objects.filter(is_active=True).count()
    
    @staticmethod
    def search_projects(query: str) -> QuerySet:
        """
        Busca proyectos por título o descripción.
        
        Args:
            query: Texto a buscar
            
        Returns:
            QuerySet con proyectos coincidentes
        """
        from django.db.models import Q
        
        return Project.objects.filter(
            Q(title__icontains=query) | Q(descriptions__icontains=query),
            is_active=True
        ).order_by('-created')
    
    @staticmethod
    def get_cached_projects():
        """
        Obtiene proyectos de caché.
        
        Returns:
            Lista de proyectos desde caché o BD
        """
        projects = cache.get(ProjectService.CACHE_KEY)
        
        if projects is None:
            projects = list(ProjectService.get_all_projects())
            cache.set(ProjectService.CACHE_KEY, projects, ProjectService.CACHE_TIMEOUT)
        
        return projects
    
    @staticmethod
    def invalidate_cache():
        """Invalida el caché de proyectos"""
        cache.delete(ProjectService.CACHE_KEY)
    
    @staticmethod
    def get_projects_by_year(year: int) -> QuerySet:
        """
        Obtiene proyectos creados en un año específico.
        
        Args:
            year: Año a filtrar
            
        Returns:
            QuerySet con proyectos del año especificado
        """
        return Project.objects.filter(
            created__year=year,
            is_active=True
        ).order_by('-created')
    
    @staticmethod
    def create_project(title: str, descriptions: str, image, link: str) -> Project:
        """
        Crea un nuevo proyecto.
        
        Args:
            title: Título del proyecto
            descriptions: Descripción del proyecto
            image: Archivo de imagen
            link: URL del proyecto
            
        Returns:
            Instancia de Project creada
            
        Raises:
            ValueError: Si los datos no son válidos
        """
        from .models import ProjectValidator
        
        # Validar datos
        ProjectValidator.validate_title(title)
        ProjectValidator.validate_link(link)
        
        # Crear proyecto
        project = Project.objects.create(
            title=title,
            descriptions=descriptions,
            image=image,
            link=link
        )
        
        # Invalidar caché
        ProjectService.invalidate_cache()
        
        return project
    
    @staticmethod
    def update_project(project_id: int, **kwargs) -> Project:
        """
        Actualiza un proyecto.
        
        Args:
            project_id: ID del proyecto a actualizar
            **kwargs: Campos a actualizar
            
        Returns:
            Instancia de Project actualizada
            
        Raises:
            Project.DoesNotExist: Si el proyecto no existe
        """
        project = Project.objects.get(id=project_id)
        
        # Validar si se actualiza el título o enlace
        if 'title' in kwargs:
            from .models import ProjectValidator
            ProjectValidator.validate_title(kwargs['title'])
        
        if 'link' in kwargs:
            from .models import ProjectValidator
            ProjectValidator.validate_link(kwargs['link'])
        
        # Actualizar
        for key, value in kwargs.items():
            setattr(project, key, value)
        project.save()
        
        # Invalidar caché
        ProjectService.invalidate_cache()
        
        return project
    
    @staticmethod
    def delete_project(project_id: int) -> bool:
        """
        Elimina (desactiva) un proyecto.
        
        Args:
            project_id: ID del proyecto a eliminar
            
        Returns:
            True si se eliminó exitosamente
        """
        try:
            project = Project.objects.get(id=project_id)
            project.is_active = False
            project.save()
            ProjectService.invalidate_cache()
            return True
        except Project.DoesNotExist:
            return False
