from django.contrib import admin
from django.urls import path, include
from .views import HomeViews, AboutView, PerfilView, ResumeView, ContactView, HomeView
from porfolio.views import ProjectListView, Proyectos  # Proyectos deprecated


# === SOLID Principles Applied ===
# D (Dependency Inversion): Importar clases genéricas, no funciones específicas
# O (Open/Closed): Usar .as_view() para vistas basadas en clases
urlpatterns = [
    path('config/', admin.site.urls),
    
    # MEJORADO: Usar HomeView (nueva) en lugar de HomeViews (deprecated)
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('perfil/', PerfilView.as_view(), name="profile"),
    path('resume/', ResumeView.as_view(), name="resume"),
    path('contact/', ContactView.as_view(), name="contact"),
    
    # MEJORADO: Usar ProjectListView en lugar de función Proyectos
    path('proyectos/', ProjectListView.as_view(), name='projects'),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]