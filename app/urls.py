"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from saep.views import cadastroUsuarios, cadastroTarefas, gerenciarTarefas, editarTarefa, excluirTarefa, alterarStatus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', cadastroUsuarios, name='cadastroUsuarios'),
    path('tarefas/', cadastroTarefas, name='cadastroTarefas'),
    path('', gerenciarTarefas, name='gerenciarTarefas'),
    path('editar/<int:id>/',editarTarefa, name='editarTarefa'),
    path('excluir/<int:id>/',excluirTarefa, name='excluirTarefa'),
    path('alterar-status/<int:id>/', alterarStatus, name='alterarStatus'),

]
