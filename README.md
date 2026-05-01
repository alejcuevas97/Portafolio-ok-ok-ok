# 🎯 Portafolio Personal

Portafolio personal desarrollado con Django para mostrar habilidades, experiencia y proyectos como Ingeniero Industrial y Desarrollador Backend. Incluye secciones de información personal, habilidades técnicas, currículum y contacto. Cuenta con una arquitectura basada en los principios SOLID para mayor mantenibilidad.

## Enlace de Portfolio
https://portafolio-ok-ok-ok.onrender.com


## 🚀 Tecnologías Utilizadas

- **Backend**: Django 6.0
- **API**: Django Rest Framework (DRF) 3.17.1
- **Autenticación**: Django REST Framework Simple JWT
- **Frontend**: HTML, CSS, Tailwind CSS 4.2.4
- **Base de Datos**: PostgreSQL o SQLite
- **Despliegue**: Gunicorn, WhiteNoise
- **Otros**: Django Environ, Pillow, Psycopg2

## ✨ Características

### Páginas Web
- **Inicio**: Página de bienvenida con diseño responsivo
- **Perfil**: Información personal del desarrollador
- **Acerca de Mí**: Formación académica y habilidades técnicas
- **Currículum**: Descripción profesional detallada
- **Contacto**: Información de contacto
- **Proyectos**: Lista de proyectos realizados con paginación

### Modelo de Datos
- **Proyecto**: Modelo para gestionar proyectos con campos como título, descripción, imagen y enlace

### Arquitectura
- Implementación de los principios SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
- Servicios separados para lógica de negocio
- Vistas genéricas extensibles
- Validadores personalizados

### API REST (Preparada)
- Serializers para operaciones CRUD en proyectos
- Estructura preparada para endpoints de API

## 🔧 Instalación

### Prerrequisitos
- Python 3.8+
- Node.js (para Tailwind CSS)
- PostgreSQL (opcional, SQLite por defecto)

### Pasos

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/alejcuevas97/PORTAFOLIO_PROPIO.git
   cd Portafolio
   ```

2. **Crea entorno virtual:**
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # Linux/Mac
   ```

3. **Instala dependencias de Python:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instala dependencias de Node.js:**
   ```bash
   npm install
   ```

5. **Configura variables de entorno (.env):**
   Crea un archivo `.env` en la raíz del proyecto con:
   ```
   DEBUG=True
   SECRET_KEY=tu_clave_secreta_aqui
   DATABASE_URL=sqlite:///db.sqlite3  # o tu URL de PostgreSQL
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Ejecuta migraciones:**
   ```bash
   python manage.py makemigrations porfolio
   python manage.py migrate
   ```

7. **Recopila archivos estáticos:**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```
   Accede a http://localhost:8000

## 📁 Estructura del Proyecto

```
Portafolio/
├── Portafolio/          # Configuración principal
│   ├── settings.py      # Configuraciones de Django
│   ├── urls.py          # URLs principales
│   ├── views.py         # Vistas de páginas
│   └── serializers.py   # Serializers para API
├── porfolio/            # App de portafolio
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas de proyectos
│   ├── forms.py         # Formularios
│   └── services.py      # Servicios de negocio
├── templates/           # Plantillas HTML
├── static/              # Archivos estáticos
├── media/               # Archivos multimedia
└── requirements.txt     # Dependencias Python
```

## 🚀 Uso

- Navega por las diferentes secciones usando la barra de navegación
- En la sección de proyectos, puedes ver la lista de proyectos realizados
- El panel de administración está disponible en `/config/` (requiere credenciales de superusuario)

## 🤝 Contribución

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia ISC.

## 📞 Contacto

- **Autor**: Alejandro Cuevas Gonzalez
- **GitHub**: [alejcuevas97](https://github.com/alejcuevas97)
- **Repositorio**: [PORTAFOLIO_PROPIO](https://github.com/alejcuevas97/PORTAFOLIO_PROPIO)</content>
<parameter name="filePath">d:\Almacen\CURSOS\backend con django\Portafolio\README.md
