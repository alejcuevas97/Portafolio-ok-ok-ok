from django.views.generic import ListView
from .models import Certification


class CertificationListView(ListView):
    model = Certification
    template_name = 'certificado/certificaciones.html'
    context_object_name = 'certifications'

    def get_queryset(self):
        return Certification.objects.filter(active=True).order_by('-issued_date', 'order')
