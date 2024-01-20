FROM python:3.8

WORKDIR /app

# Copiar apenas o arquivo requirements.txt primeiro
COPY requirements.txt .

# Criar e ativar um ambiente virtual
RUN python -m venv venv \
    && . venv/bin/activate

# Instalar as dependências
RUN pip install -r requirements.txt \
    && rm -rf /root/.cache

# Copiar o restante do código
COPY . .


EXPOSE 5000
CMD [ "python", "app.py" ]
