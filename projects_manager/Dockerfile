# Base image
FROM python:3.11-slim

# Definir variáveis de ambiente para o Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt /app/

# Instalar dependências do sistema e Python
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar o restante do código
COPY . /app/

# Expor a porta do Django
EXPOSE 8000

# Comando para executar migrações e rodar o servidor
CMD ["sh", "-c",  "python manage.py makemigrations && python manage.py migrate && python manage.py makemigrations projects_manager && python manage.py migrate projects_manager && python manage.py runserver 0.0.0.0:8000"]
