from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('issuer', models.CharField(blank=True, max_length=200, verbose_name='Emisor')),
                ('issued_date', models.DateField(blank=True, null=True, verbose_name='Fecha de emisión')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('credential_url', models.URLField(blank=True, verbose_name='URL de credencial')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'ordering': ['-issued_date', 'order'],
                'verbose_name': 'Certificación',
                'verbose_name_plural': 'Certificaciones',
            },
        ),
    ]
