# Entrega 1 - PeliBlog

*Por Delgado Alejo*👋

> Este es un proyecto que se realizó para el curso de Python en CoderHouse, el mismo consiste en un Blog de peliculas, donde se podrán agregar peliculas con su correspondiente informacion y una reseña para poder dar espacio al debate u opiniones en una seccion de comentarios. Al ser la primer entrega, solo se encuentran disponibles las funciones de agregar y buscar peliculas. Posteriormente se desea implementar la seccion de comentarios junto a la posibilidad de poder logearse en dicho blog para poder ser identificada las personas que interactuen. 
> Como se menciono anteriormente, en esta primer entrega, simplemente se puso en practica el uso de Herencias de HTML, el uso de POO con Clases, formularios para insertar datos a todas las Clases que fueron creadas y formulario para la busqueda de datos en la Base de Datos correspondiente. Se pretende hacer funcionales todas las cosas que ahora no lo son para la entrega final del proyecto. 

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



## Herramientas usadas

🛠️ Python

🛠️ Django

🛠️ HTML

🛠️ CSS


## Backend

Cada Modelo será creado de la siguiente manera: 

🌱 Post: Cada post será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |

🌱 PostNoticias: Cada Post de noticias será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostReviews: Cada Post de reviews será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostGaming: Cada Post de gaming será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |

🌱 PostSoftware: Cada Post de software será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostHardware: Cada Post de hardware será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 Contacto: Cada contacto será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    nombre     |   CharField   |   nombre      |
|   email       |   EmailField  |   email       |
|   consulta    |   CharField   |    consulta   |

