# Usa a imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para o container
COPY . /app

# Instala dependências (se tiver requirements.txt)
# RUN pip install -r requirements.txt

# Comando padrão para rodar o programa
CMD ["python", "main.py"]

