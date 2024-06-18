"""
URL configuration for presente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from presenteApp.views import home, cad_aluno,mostrar_aluno,editar_aluno,deletar_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('cad_aluno/',cad_aluno, name='cad_aluno'),
    path('mostrar_aluno/',mostrar_aluno, name='mostrar_aluno'),
    path('editar_aluno/<str:id>',editar_aluno, name='editar_aluno'),
    path('deletar_aluno/<str:id>',deletar_aluno, name='deletar_aluno'),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
