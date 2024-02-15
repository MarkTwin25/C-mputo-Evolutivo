El archivo script.py consta de dos funcionalidades principales y a continuación se explica como funciona cada una:

1. evaluacion de las funciones

La manera de ejecutar esta funcionalidad es de la manera:

python .\script.py funcion dimension argumentos

Ejemplo:
python script.py rastringin 2 5 -5

Notemos que para todas las veces que se quiera usar se debe comenzar con "python script.py" ya que ese es el nombre del script.

rastringin es la función que queremos usar (se puede usar rosembrock y schwefel tambien), como tal el nombre de la funcion en minusculas.

2 es la dimension que queremos aplicar.

los n numeros que siguen son nuestros argumentos que estaran en la lista a evaluar (no usar comas, solo separarlos con espacios).

2. Busqueda binaria

Esta función se ejecuta y se ve de la manera:

python .\script.py busqueda_aleatoria funcion dimension argumentos

De la misma manera que el inciso anterior, debemos comenzar con "python \script.py".

busqueda_aleatoria es el comando que debemos usar y este es obligatorio ya que sino, ejecutara la funcion anterior.

funcion es la funcion que queremos ejecutar que de igual manera puede ser rastringin, rosembrock o schwefel todo en minusculas.

dimension es un numero entero arbitrario que indica la dimension que queremos ejecutar

argumentos son los intervalos en los que queremos ejecutar el programa.