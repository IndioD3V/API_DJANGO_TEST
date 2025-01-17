from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import environ
import os

env = environ.Env()
env.read_env('.env')

class ProjectsManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects_manager'


@receiver(post_migrate)
def create_default_admin(sender, **kwargs):

    if sender.name == "projects_manager":
        from django.contrib.auth.models import User  
        from .models import LevelDeveloper, StatusDeveloper, StatusProject, StatusTask

        username = env.str('DEFAULT_USER')
        password = env.str('DEFAULT_PASSWORD')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="admin@example.com",
                password=password
            )
            print(f"Usuário admin criado com sucesso.")
        
        for level in ('Junior', 'Pleno', 'Senior', 'Estagiario'):
            if not LevelDeveloper.objects.filter(description=level):
                LevelDeveloper.objects.create(
                    description=level
                )
        
        for status_table in (StatusDeveloper, StatusProject, StatusTask):
            for status in ('Ativo', 'Inativo'):
                if not status_table.objects.filter(description=status):
                    status_table.objects.create(
                        description=status
                    )
                    
    
