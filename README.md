# web-Jhon-Jairo
despliegue web personal

=============================================================================
conda update -n base -c defaults conda

conda create -n py37 python=3.7.4

conda activate py37
conda deactivate

=============================================================================
conda create -n django3 python=3.7.4
conda activate django3
conda deactivate
pip install django==2.2.6

pip install django
pip list
django-admin startproject webpersonal

=============================================================================

python -m django --version => verfica la actual version de django
conda install pylint => comprobador de sintaxis

=============================================================================
python manage.py startapp core

=============================================================================
crear directorio media en la raiz del proyecto para guradar las imagenes

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


configurar en el campo del modelo 
image = models.ImageField(verbose_name="Imagen", upload_to="projects")

============================================================================================
configuracion para visualizacion de imagen si DEBUG esta en true en urls.py de proyecto raiz

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
