ipm-examples
============

Ejemplos de la asignatura Interfaces Persona Máquina para el curso 20/21
Facultade de Informática, Universidade da Coruña.

## AJAX

Aplicación que muestra como usar fetch para realizar distintos tipos de peticiones AJAX a Dog API y a una API ad hoc implementada en python con el framework Flask.

### Instrucciones

1. Instalación y ejecución del servidor API REST Flask

   ```bash
   $ cd ipm-examples/ajax/server
   
   $ virtualenv flaskenv
   
   $ source flaskenv/bin/activate
   
   $ pip3 install -r requirements.txt
   
   $ flask run
   ```

   

2. Copia los ficheros en un servidor web (apache, nginx, ...). Si no dispones de un servidor web puedes utilizar el servidor HTTP básico que incorpora python: 
```bash
$ cd ipm-examples/ajax/web-client
$ python -m http.server        # python 3
```
3. Abre un navegador y accede a la dirección y puerto del servidor (http://localhost:8000, por ejemplo).

## Web Mobile

* Recursos HTML5 y CSS3 para web mobile

* Página web con Responsive Web Design

* Página web responsive con Bootstrap

### Instrucciones

1. Copia los ficheros en un servidor web (apache, nginx, ...). Si no dispones de un servidor web puedes utilizar el servidor HTTP básico que incorpora python: 
```bash
$ cd ipm-examples/web-mobile/
$ python -m http.server        # python 3
```
2. Abre un navegador y accede a la dirección y puerto del servidor (http://localhost:8000, por ejemplo).
