from rest_framework import serializers
from porfolio.models import Project


# === Principio S (Single Responsibility) ===
# Serializador específico para listar proyectos
class ProjectListSerializer(serializers.ModelSerializer):
    """Serializador para listar proyectos - vista de lectura"""
    class Meta:
        model = Project
        fields = ['id', 'title', 'descriptions', 'image', 'link', 'created']
        read_only_fields = ['id', 'created']


# === Principio S (Single Responsibility) ===
# Serializador específico para crear/actualizar proyectos
class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serializador para detalle y operaciones CRUD"""
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['created', 'update']


# === Compatibilidad hacia atrás ===
class PortafolioSerializers(ProjectDetailSerializer):
    """DEPRECADA - usa ProjectDetailSerializer en su lugar"""
    pass


# Nombre antiguo en minúscula (DEPRECADO)
portafolioSerializers = PortafolioSerializers
