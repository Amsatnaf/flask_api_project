
FROM python:3.11-slim

WORKDIR /opt/app-root/src

# Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Porta
ENV PORT=8080
EXPOSE 8080

# Permissões para UID arbitrário (grupo root = 0)
# Boa prática em OpenShift: permitir g=u no diretório da app
RUN chgrp -R 0 /opt/app-root && chmod -R g=u /opt/app-root

# Servidor WSGI recomendado
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]

