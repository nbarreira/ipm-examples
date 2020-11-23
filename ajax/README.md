# Instalación y ejecución

## Servidor API REST

```bash
cd server
virtualenv flaskenv
source flaskenv/bin/activate
pip3 install -r requirements.txt
flask run
```

## Web-client

```bash
cd web-client
python3 -m http.server
```

Abrir un navegador y acceder a la url http://localhost:8000/