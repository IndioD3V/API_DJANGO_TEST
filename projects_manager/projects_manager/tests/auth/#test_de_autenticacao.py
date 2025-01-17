import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
class TestAuthentication:
    def setup_method(self):
        # Criação de um superusuário para o teste
        #self.user = User.objects.create_superuser(
        #    username='admin', password='123'
        #)
        # Definindo o endpoint de autenticação
        self.token_url = '/v1/token'  # Corrigindo o caminho para o endpoint correto
        self.client = APIClient()

    def test_token_obtain_success(self):
        data = {
            "username": "admin",
            "password": "123"
        }
        # Requisição POST para obter o token
        response = self.client.post(self.token_url, data, format='json')

        # Verificar se o status da resposta é 200 (OK)
        assert response.status_code == status.HTTP_200_OK

        # Verificar se o token foi retornado
        assert 'access' in response.json()

    def test_token_obtain_failure_wrong_credentials(self):
        data = {
            "username": "admin",
            "password": "wrong_password"
        }
        response = self.client.post(self.token_url, data, format='json')

        # Verificar se o status da resposta é 401 (Unauthorized)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_request(self):
        # Obtenção do token primeiro
        data = {
            "username": "admin",
            "password": "123"
        }
        response = self.client.post(self.token_url, data, format='json')
        token = response.json()['access']

        # Autenticando com o token e fazendo a requisição
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get('/api/v1/protected-endpoint/')  # Substitua pelo endpoint real

        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_request(self):
        response = self.client.get('/api/v1/protected-endpoint/')  # Substitua pelo endpoint real
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
