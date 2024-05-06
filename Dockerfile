FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta 5000 (a porta em que o Flask normalmente é executado)
EXPOSE 5000

# Defina o comando padrão para iniciar o aplicativo Flask
CMD ["python", "app.py"]
