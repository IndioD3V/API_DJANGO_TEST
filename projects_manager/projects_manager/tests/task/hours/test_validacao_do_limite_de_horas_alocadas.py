import pytest
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient
from datetime import datetime
from rest_framework import status

import environ
import os

env = environ.Env()
env.read_env('.env')

@pytest.mark.django_db
def test_task_hours_within_project_limit_valid():

    from projects_manager.models.project import Project
    from projects_manager.models.task import Task
    from projects_manager.models.developer import Developer
    from projects_manager.models import Technology, DeveloperTechnology, ProjectTechnology
    
    
    project = Project.objects.create(
        name="Project 1", 
        start_date="2025-01-01", 
        end_date="2025-12-31",
        code="123",
        status_id=1
    )
    
    developer = Developer.objects.create(name="Dev 1", cpf="12345678901", level_id=1, status_id=1)
    
    technology = Technology.objects.create(
        name='Python',
        alias='PY'
    )
    
    DeveloperTechnology.objects.create(
        developer_id=developer.id,
        technology_id=technology.id
    )
    
    ProjectTechnology.objects.create(
        project_id=project.id,
        technology_id=technology.id
    )
    
    client = APIClient()
    data = {
        "username": env.str('DEFAULT_USER'),
        "password": env.str('DEFAULT_PASSWORD') 
    }
    
    response = client.post(
        '/api/v1/token',
        data,
        format="json"
    )

    token = response.json()['access']
    payload = {
        "project": project.code,
        "developer": developer.cpf,
        "hours": 45,
        "status": 'Ativo',
        "description": 'Teste'
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"  
    }

    response = client.post(
        path='/api/v1/alocacao/',
        data=payload,
        headers=headers,
        format='json'
    )

    assert response.status_code == status.HTTP_201_CREATED
    
@pytest.mark.django_db
def test_task_hours_exceeding_project_limit():
    from projects_manager.models.project import Project
    from projects_manager.models.task import Task
    from projects_manager.models.developer import Developer
    from projects_manager.models import Technology, DeveloperTechnology, ProjectTechnology
    
    
    project = Project.objects.create(
        name="Project 1", 
        start_date="2025-01-01", 
        end_date="2025-12-31",
        code="123",
        status_id=1
    )
    
    developer = Developer.objects.create(name="Dev 1", cpf="12345678901", level_id=1, status_id=1)
    
    technology = Technology.objects.create(
        name='Python',
        alias='PY'
    )
    
    DeveloperTechnology.objects.create(
        developer_id=developer.id,
        technology_id=technology.id
    )
    
    ProjectTechnology.objects.create(
        project_id=project.id,
        technology_id=technology.id
    )
    
    client = APIClient()
    data = {
        "username": env.str('DEFAULT_USER'),
        "password": env.str('DEFAULT_PASSWORD') 
    }
    
    response = client.post(
        '/api/v1/token',
        data,
        format="json"
    )

    token = response.json()['access']
    payload = {
        "project": project.code,
        "developer": developer.cpf,
        "hours": 20000,
        "status": 'Ativo',
        "description": 'Teste'
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"  
    }

    response = client.post(
        path='/api/v1/alocacao/',
        data=payload,
        headers=headers,
        format='json'
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST