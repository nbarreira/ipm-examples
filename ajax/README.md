# Instalación y ejecución

## Servidor API REST

```bash
cd server
virtualenv flaskenv
source flaskenv/bin/activate
pip3 install -r requirements.txt
flask run
```
### API REST

1. Login
- Ruta: /login
- Método: POST
- Variables FormData/JSON: username, password
- Resultados:
   - Código de estado 200,
     JSON: { 'accessToken': string }
   - Código de estado 400,
     JSON: {'msg': string}
   - Código de estado 401,
     JSON: {'msg': string}

2. Acceso a datos protegidos
- Ruta: /protected
- Método: POST
- Cabecera: 'Authorization': 'Bearer ' + token
- Resultados:
   - Código de estado 200,
     JSON: { 'logged_in_as': string }
   - Código de estado 401,
     JSON: {'msg': string}

3. Obtener imagen
- Ruta: /image
- Método: GET
- Cabeceras: 
    - 'pragma': 'no-cache'
    - 'cache-control': 'no-cache'
- Resultados:
   - Código de estado 200,
     BLOB: mimetype 'image/png'

## Web-client

```bash
cd web-client
python3 -m http.server
```

Abrir un navegador y acceder a la url http://localhost:8000/

