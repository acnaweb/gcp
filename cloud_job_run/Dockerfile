# Usa uma imagem Python leve
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /opt/app

# Copia o script para o container
COPY src src

# Comando padrão ao executar o container
ENTRYPOINT ["python", "src/app.py"]
