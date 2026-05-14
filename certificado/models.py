from django.db import models


class Certification(models.Model):
    title = models.CharField('Título', max_length=200)
    issuer = models.CharField('Emisor', max_length=200, blank=True)
    issued_date = models.DateField('Fecha de emisión', blank=True, null=True)
    description = models.TextField('Descripción', blank=True)
    credential_url = models.URLField('URL de credencial', blank=True)
    order = models.PositiveIntegerField('Orden', default=0)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        ordering = ['-issued_date', 'order']
        verbose_name = 'Certificación'
        verbose_name_plural = 'Certificaciones'

    def __str__(self):
        return self.title
