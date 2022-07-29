# Buenas practicas y Errores comunes

### Error al querer ejecutar un Script en Python

* Omitir la extension del archivo `python3 holaMundo`
* Omitir mayusculas `python3 holamundo.py`
* Copiar y pegar un comando sin cambiar las comillas por unas que entienda Python

### Errores al escribir el codigo

* Declarar variables sin inicializarlas
* No cerrar las comillas `print(“la suma de la variable 1= , variable1, “ y la variable 2=”, variable2, “es igual a “, suma)`

### Excepciones

Algunos ejemplos de errores en tiempos de ejecucion pueden ser:

```python
>>> 10 * (1/0)Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ZeroDivisionError: division by zero

>>> 4 + spam*3

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

NameError: name 'spam' is not defined

>>> '2' + 2

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: Can't convert 'int' object to str implicitly
```

Como podemos suponer, las excepciones tienen diferente tipo y este se muestra como parte del mensaje de error (ZeroDivisionError, NameError, TypeError, etc). El nombre del tipo de excepción mostrada coincide con el nombre de la excepción predefinida que ocurrió, la coincidencia en la descripción y el nombre se utiliza por un tema de convención, no obstante nosotros podemos definir nuestras propias excepciones y en ese caso podríamos mostrar un texto diferente del nombre de la excepción por pantalla, aunque una buena práctica es mantener iguales el texto mostrado y el nombre para facilitar la tarea de depuración. Los nombres de las excepciones estándar son identificadores incorporados al intérprete (no son palabras clave reservadas).

El resto de la línea provee un detalle basado en el tipo de la excepción y qué la causó.

La parte anterior del mensaje de error muestra el contexto donde la excepción sucedió, en la forma de un trazado del error listando líneas fuente; sin embargo, no mostrará líneas leídas desde la entrada estándar.

### Manejo de Excepciones

```python
while True:    try:

      valor1 = int(input("Por favor ingrese el primer numero: "))

      break

  except ValueError:

      print("Oops! No era válido. Intente nuevamente...")
```

En el ejemplo anterior podemos ver que se introdujo una nueva declaración que encierra al bloque que podría tener el error en tiempo de ejecución, como habíamos visto en el ejemplo de Suma con Vitaminas, el error se producía al querer ingresar un dato no numérico por teclado, por lo tanto deberemos encerrar con ‘try’ esa porcion de codigo.

El bloque try lo que hace es intentar la ejecución del código que encierra, si no se produce ninguna excepción durante la ejecución, entonces el bloque except se saltea y se continúa con el flujo normal del programa.
Si en cambio se produce una excepción, entonces se interrumpirá el flujo del programa y se salteará el resto del código hasta pasar al bloque except, el cual se ejecutará en el caso de que la excepción ocurrida coincida con la manejada por este bloque, y luego es retornada nuevamente al comienzo del bloque try.

En el caso de que ocurriera una excepción diferente de la manejada por el bloque except, entonces se busca si hay alguna declaración try de orden superior (es decir algún try anidado por encima del bloque que produjo la excepción), si no se encuentra ningún bloque que la maneje, estamos frente a una excepción no manejada y la ejecución se frena con el mensaje de error.
Un except puede nombrar múltiples excepciones usando paréntesis, por ejemplo:

```python
... except (RuntimeError, TypeError, NameError):
... pass
```

Habiendo comprendido el uso de excepciones, manejaremos las mismas en el ejemplo de “Suma con Vitaminas”:

```python
while True: try:

          variable1=int(input("Ingrese el primer valor:"))

         break

 except ValueError:

         print("El valor debe ser numerico, por favor intente nuevamente")

while True:

 try:

         variable2=int(input("Ingrese el segundo valor:"))

         break

 except ValueError:

         print("El valor debe ser numerico, por favor intente nuevamente")

suma= variable1 + variable2

print("la suma de la variable 1=" , variable1, " y la variable 2=", variable2, "es igual a ", suma)
```

Realizamos un while True y un try por cada variable, seguramente se nos ocurriría pensar que podríamos simplificarlo utilizando un solo bucle, ya que al tratarse de la misma posible excepción para las dos variables, si el usuario se equivocarse al ingreso de cualquiera de las dos se manejaría la excepción de igual manera… veamos qué sucede si implementamos nuestro código con un solo while:

```python
while True: try:

          variable1=int(input("Ingrese el primer valor:"))

                 variable2=int(input("Ingrese el segundo valor:"))

         break

 except ValueError:

         print("El valor debe ser numerico, por favor intente nuevamente")

suma= variable1 + variable2

print("la suma de la variable 1=" , variable1, " y la variable 2=", variable2, "es igual a ", suma)
```

