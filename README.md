# Entrega 1 - PeliBlog

*Por Delgado Alejo*👋

> Este es un proyecto que se realizó para el curso de Python en CoderHouse, el mismo consiste en un Blog de peliculas, donde se podrán agregar peliculas con su correspondiente informacion y una reseña para poder dar espacio al debate u opiniones en una seccion de comentarios. Al ser la primer entrega, solo se encuentran disponibles las funciones de agregar y buscar peliculas. Posteriormente se desea implementar la seccion de comentarios junto a la posibilidad de poder logearse en dicho blog para poder ser identificada las personas que interactuen. 

> Como se menciono anteriormente, en esta primer entrega, simplemente se puso en practica el uso de Herencias de HTML, el uso de POO con Clases, formularios para insertar datos a todas las Clases que fueron creadas y formulario para la busqueda de datos en la Base de Datos correspondiente. Se pretende hacer funcionales todas las cosas que ahora no lo son para la entrega final del proyecto(Por ejemplo el registro e inicio de sesion, una seccion de comentarios, una seccion de post aleatorios que recomienden peliculas). 

## Instalacion git clone

Para acceder al proyecto clonándolo, deberás ejecutar en consola: 
```sh
git clone https://github.com/AlejoDR13/Entrega1-Delgado-Alejo.git
```

## Instalacion entorno virtual 
```sh
pip install virtualenv

virtualenv "nameenv"

"namenev"\Scripts\activate
```
Una vez creado y activado el entorno virtual en el directorio correspondiente, se procede a ejecutar el blog donde lo podremos observar y poner a prueba:

Para correr la pagina web se debera ejecutar desde la terminal el siguiente comando:
```sh
py manage.py runserver
```

## Funcionalidades

Una vez levantado, se podra observar una pagina de inicio con un pie de pagina mostrando las distintas funcionalidades de inicio, registro, inicio de sesion, informacion, como titulo el nombre del Blog, etc. Luego, en la parte lateral derecha se observan dos tarjetas que muestran un buscador y la otra muestra los generos de las peliculas las cuales estan disponibles en el blog. 
Basicamente, cada genero (Drama, Terror, Aventura, etc) es una Clase diferente por la cual se crean objetos que son las peliculas correspondientes a su genero. Ingresando a cualquiera de los botones disponibles podremos acceder a la seccion de su genero correspondiente, por ejemplo "Suspenso". Una vez ubicados ahi en el mismo apartado se nos agrega la opcion de hacer nuestro aporte con alguna pelicula, pudiendo agregar la informacion necesaria. Clickeando en este apartado nos llevara a otra seccion donde podremos cargar la informacion solicitada a la base de datos, una vez enviada la informacion nos redirecciona nuevamente a la seccion donde nos encontrabamos (Suspenso). Llegado a este punto, si deseamos buscar alguna pelicula de dicho genero sera posible hacerlo desde el buscador que se observa, donde buscara en la base de datos si existe la pelicula y de no ser asi nos redireccionara a otra pagina aclarandonos que no se ha encontrado la pelicula que se busca.

A simples rasgos, las funcionalidades de esta primer entrega consisten en lo anteriormente mencionado.

## Herramientas usadas

🛠️ Python

🛠️ Django

🛠️ HTML

🛠️ CSS


## Backend

Cada Modelo (Genero) será creado de la siguiente manera: 

 Peliculas(objects): Cada pelicula independientemente del genero tendran el mismo formato, lo que las diferenciara sera su clase. El modelo general es el siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   direccion   |   CharField   |   subtitulo   |
|     estreno   |   DateField   |    fecha      |
|   duracion    | IntegerField  |   texto       |
|   epigrafe    |   CharField   |   texto       |

Modelos(class): Las clases creadas son las siguientes:

|   Nombre     |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|   Drama    |   CharField   |   titulo      |
|   Terror  |   CharField   |   subtitulo   |
|      Aventura   |   DateField   |    fecha      |
|   Ciencia Ficcion      |   CharField   |   texto       |
|   Thriller      |   CharField   |   texto       |
|   Suspenso      |   CharField   |   texto       |


