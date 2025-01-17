"""
URL configuration for projects_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects_manager.views import (
    DeveloperViewSet, LevelDeveloperViewSet, 
    StatusDeveloperViewSet, RegisterView,
    ProjectTechnologyViewSet, ProjectViewSet, 
    DeveloperTechnologyViewSet, StatusProjectViewSet,
    StatusTaskViewSet, TechnologyViewSet, TaskViewSet
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


router = DefaultRouter()
# Developer
router.register(r'programadores', DeveloperViewSet, basename='developer')
router.register(r'senioridade_dev', LevelDeveloperViewSet, basename='level_developer')
router.register(r'status_dev', StatusDeveloperViewSet, basename='status_developer')
router.register(r'tecnologia_dev', DeveloperTechnologyViewSet, basename='developer_technology')

# Project
router.register(r'projetos', ProjectViewSet, basename='project')
router.register(r'status_projeto', StatusProjectViewSet, basename='status_project')
router.register(r'tecnologia_projeto', ProjectTechnologyViewSet, basename='project_technology')

# Task
router.register(r'alocacao', TaskViewSet, basename='task')
router.register(r'status_alocacao',StatusTaskViewSet, basename='status_task')

# Technology
router.register(r'tecnologias', TechnologyViewSet, basename='technology')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/register', RegisterView.as_view(), name='register'),
]