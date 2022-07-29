# Empezando con Codigo

## Numeros

Los operadores +, -, * y / funcionan como en todos los lenguajes. Y los parentesis se usan para agrupar.

```python
2+2 #4 
50-5*6 # 20 
(50 - 5 * 6) / 4 # 5.0
8 / 5 # 1.6 - La division siempre devuelve un float
17 // 3 # 3 - usamos // para quedarnos solo con la parte entera de la division
17 % 3 # 2 - El resto
5 ** 2 # 25 - 5 al cuadrado
```

Python es un lenguaje no tipado, pero eso no significa que no maneje tipos de datos. Python es de alto nivel, tiene muchas cosas que le facilitan la vida a los dev, y la eleccion del tipo de dato es una de ellas. Para declarar una variable en Python alcanza con escribir el nombre y darle un valor que definiria implicitamente el tipo de dato.

El signo '=' se usa para asignar una variable

```python
ancho = 20
largo = 5 * 9
ancho * largo # 900
```

Si intentamos acceder a una variable sin asignar..

```python
n # tratamos de acceder a una variable no definida

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

Si combino muchos numeros enteros con uno flotante, ya el resultado es flotante

```python
4 * 3.75 - 1 # 14.0
```

## Sentencia If

En Python el uso de else no es obligatorio

```Python
valor1 = 4
valor2 = 2
result = valor1-valor2 # 2
if result < 0:
... print('el resultado es negativo')
... else:
... print(result) # 2
```

Tambien podemos usar elif que equivale a un else if

```python
valor1 = 4
valor2 = 2
result = valor1 - valor2 # 2
if result<0:
... print('negativo')
... elif result>100:
... print('resultado fuera de rango')
... else:
... print(result)
```

## Sentencia While

Se usa para realizar una repeticion de una accion mientras se cumpla con una condicion explicitada.
Por ejemplo, si queremos sumar todos los valores entre 1 y 10:

```python
b = 1
while b<10:
... result = result + b
... b = b+1
print(result) # Ya no forma parte del while
```

## Cadenas de Caracteres Strings

```python
'huevos y pan' # huevos y pan
'doesn\'t' # doesn't
"doesn't" # doesn't
'"Si", le dijo.' # "Si", le dijo.
"\"Si, \" le dijo." # "Si", le dijo.
'"Isn\'t", she said' # "Isn't" she said
'"Isn\'t," she said.''"Isn\'t," she said.'
print('"Isn\'t," she said.')# "Isn't," she said.
 s = 'Primera línea.\nSegunda línea.' # \n significa nueva línea
s # sin print(), \n es incluído en la salida
'Primera línea.\nSegunda línea.'
print(s) # con print(), \n produce una nueva línea
```

Para hacer cadenas multilinea:

```python
print("""\Uso: algo [OPTIONS]

     -h Muestra el mensaje de uso

     -H nombrehost Nombre del host al cual conectarse

""")

# Salida

Uso: algo [OPTIONS]     
-h Muestra el mensaje de uso
-H nombrehost Nombre del host al cual conectarse
```

Otros ejemplos:

```python
# 3 veces 'un', seguido de 'ium'
 3 * 'un' + 'ium' # 'unununium'
```

```python
#Concatenar dos literales
'Py' 'thon' #'Python'
```

Y cuando queremos concatenar una variable y un literal (como en el anterior)

```python
prefix = 'Py'
 prefix 'thon' # no se puede concatenar una variable y una cadena literal SyntaxError: invalid syntax
 ('un' * 3) 'ium' # SyntaxError: invalid syntax
```

Para lograr esta concatenacion, debemos usar el operador +

```python
prefix + 'thon' #'Python'
```

No olvidemos que los Strings no dejan de ser arrays de caracteres, ergo, pueden ser indexados

```python
palabra = 'Python'
palabra[0] # caracter en la posición 0 -> 'P'
palabra[5] # caracter en la posición 5 -> 'n'
```

En Python podemos usar **indices negativos** para contar de atras para adelante.


```python
palabra[-1] # último caracter'n'
palabra[-2] # ante último caracter -> 'o'
palabra[-6] # 'P'
```

Obtener subcadenas

```python
palabra[0:2] # caracteres desde la posición 0 (incluída) hasta la 2 (excluída) -> 'Py'
 palabra[2:5] # caracteres desde la posición 2 (incluída) hasta la 5 (excluída) -> 'tho'
 palabra[:2] # caracteres desde el principio hasta la posición 2 (excluída) -> 'Py'
 palabra[4:] # caracteres desde la posición 4 (incluída) hasta el final -> 'on'
 palabra[-2:] # caracteres desde la ante-última (incluída) hasta el final -> 'on'
```

Y si queremos acceder a un index que no existe

```python
palabra[42] # la palabra solo tiene 6 caracteres

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

Si quiero saber el tamaño total del String

```python
s = 'supercalifrastilisticoespialidoso' 
len(s) # 33
```

## Sentencia For

```
# Midiendo cadenas de texto
 palabras = ['gato', 'ventana', 'defenestrado']
 for p in palabras:
... print(p, len(p))

#Salida

#gato 4
#ventana 7
# defenestrado 12
```

## Funcion Range()

Si necesitamos iterar sobre una secuencia de numeros, contamos con la funcion integrada `range()` que genera progresiones artimeticas. Podemos usarla junto con el for:

```python
for i in range(5):
... print(i) #01234
```

`range(5)` genera 5 valores de 0 a 4. Se pueden realizar especificaciones en la misma funcion

```python
range(5, 10) #5 a 9
range(0, 10, 3) #  0, 3, 6, 9
range(-10, -100, -30) #-10, -40, -70
```

Para iterar sobre los index de una secuencia podemos usar `range()` y `len()`

```python
a = ['Mary', 'tenia', 'un', 'corderito']
 for i in range(len(a)):
... print(i, a[i])

# Salida
0 Mary
1 tenia
2 un
3 corderito
```

Si quiero hacer un print de  `range()` no se puede

```python
print(range(10)) # range(0, 10)
```

`range()` no es una lista, es un objeto que devuelve los item sucesivos en la secuencia deseada. Es un objeto iterable

```python
list(range(5)) #[0, 1, 2, 3, 4]
```

## Sentencias break, continue y else

```python
for n in range(2, 10):
... for x in range(2, n):
... if n % x == 0:
... print(n, 'es igual a', x, '*', n/x)
... break
... else:
... # sigue el bucle sin encontrar un factor
... print(n, 'es un numero primo')

# Devuelve

2 es un numero primo
3 es un numero primo
4 es igual a 2 * 2
5 es un numero primo
6 es igual a 2 * 3
7 es un numero primo
8 es igual a 2 * 4
9 es igual a 3 * 3
```

Cuando comenzamos a escribir código somos más propensos a
cometer algunos errores de sintaxis, y considerando que cometer
errores es muy común en programación aún en los
programadores más experimentados, vale mencionar los dos
tipos más frecuentes de errores que nos encontraremos en la
programación.
Podemos dividir los errores en errores de sintaxis y excepciones.
Podemos identificar los errores de sintaxis por haber cometido
algún error al escribir una estructura, omitir algún signo de
puntuación, etc. Las excepciones en cambio son errores que se
producen en tiempo de ejecución, por ejemplo, si en mi código
intento acceder a un archivo de texto y el mismo no existe en la
ubicación especificada, se producirá una excepción.

## Sentencia pass

No hace nada, se puede usar cuando una sentencia es requerida por la sintaxis pero el programa no requiere ninguna accion, por ejemplo:

```python
while True:
... pass # Espera ocupada hasta una interrupción de teclado (Ctrl+C)

# Se usa normalmente para crear clases en su mínima expresión: 
class MyEmptyClass:
... pass

# Se puede usar tambien como marcador 
 def initlog(*args):
... pass # Acordate de implementar esto!
```

