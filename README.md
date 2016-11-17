ipm-examples
============

Ejemplos de la asignatura Interfaces Persona Máquina para el curso 16/17.
Facultade de Informática, Universidade da Coruña.

##Ajax

Aplicación que muestra el uso de peticiones AJAX utilizando la API REST de The Movie DB como origen de datos.

### Funcionalidades implementadas
* Buscar por título y mostrar la lista de películas encontradas https://developers.themoviedb.org/3/search/search-movies

* Mostrar detalles de una película https://developers.themoviedb.org/3/movies/get-movie-details

* Valorar una película https://developers.themoviedb.org/3/movies/rate-movie
Nota: Es necesario crear un id de sesión o un id de sesión invitado para valorar una película. En este ejemplo, se obtendrá un id de sesión invitado: https://developers.themoviedb.org/3/authentication/create-guest-session



### Instrucciones

1. Edita los ficheros *index.html* y *js/api.js* para sustituir la cadena de caracteres **COPY_YOUR_API_KEY_HERE** por la API_KEY obtenida en The Movie DB.

2. Copia los ficheros en un servidor web (apache, nginx, ...). Si no dispones de un servidor web puedes utilizar el servidor HTTP básico que incorpora python: 
```bash
$ cd ipm-examples/ajax
$ python -m SimpleHTTPServer   # python 2.7
$ python -m http.server        # python 3
```
3. Abre un navegador y accede a la dirección y puerto del servidor (http://localhost:8000, por ejemplo).

## Web Mobile

* Recursos HTML5 y CSS3 para web mobile.

* Blog Responsive

* Blog responsive con Bootstrap
