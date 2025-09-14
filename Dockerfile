# Usar imagem base do Python
FROM python:3.10-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar dependências (mesmo que vazio, requirements.txt precisa existir)
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao rodar o container
CMD ["python", "main.py"]
