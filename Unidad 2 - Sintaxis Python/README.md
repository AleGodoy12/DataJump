# Bases de la Sintaxis Python 🚀️

Python posee una sintaxis clara y simple

**Duck Typing** -> Es el estilo de tipificacion de los datos, permite declarar implicitamente el tipo de dato de una variable al asignarla, permitiendo que esta sea capaz de cambiar de tipo de dato cuando sea.

## Reglas generales de la Sintaxis

### Lineas fisicas y lineas logicas

Las **lineas fisicas** son lineas que terminan con un caracter de fin de linea, \n en Unix o \r\n en Windows, por ejemplo:

> print('esto es una linea fisica')

Una linea fisica terminaria al apretar enter, una **linea logica** en cambio puede estar formada por muchas lineas fisicas. Se pueden unir lineas fisicas para formar una linea logica de la siguiente manera:

```
print('esto en cambio \
es una linea \
logica')
```

Otra manmera es encerrar lo necesario entre (), [] o {}, por ejemplo:

> print(
> 'hola',
> 'mundo'
> )

### Construccion de las sentencias

En Python cuando hablamos de lineas, hablamos de lineas logicas, y se podrá empezar a hablar de sentencias.
Una **sentencia** es una instruccion que el interprete Python puede ejecutar, se pueden construir a partir de una linea fisica o de una linea logica, dependiendo la complejidad de la instruccion.

### Sentencias simples y compuestas

Las sentencias Python se componen de varias lineas logicas. Las **sentencias simples** son las que deben completarse en una sola linea logica

> from sys import platform

Las **sentencias compuestas** son aquellas que deben empezar con una condicion de sentencia compuesta y deben contener sentencias simples y/o compuestas identadas.

```
if a > b:
    print('a es mayor que b')
```

Tambien podemos finalizar lineas fisicas con punto y coma en una misma linea fisica.

> var1= 0; var2 = 1;

Deteniéndonos un segundo en este último uso, no es muy difícil entender que el empleo de ‘;’ para separar varias sentencias en una misma línea física atenta contra la legibilidad del código desarrollado en Python, haciendo engorrosa su interpretación por cualquier otro programador, o por la propia persona que escribió dicho código luego de un tiempo de realizado. Por este motivo el empleo de ‘;’ de esta manera **se considera una mala práctica, y se recomienda evitarlo**.

### Buenas practicas

* Elegir nombres significativos para las variables
* Evitar la incorporacion de mas de una instruccion por linea
* Escribir los codigos de la forma mas sencilla posible
* Usar el estilo de codificacion estandar para que distintas personas puedan entenderlo

### Indentación

Python no usa () o `begin...end` para definir bloques de codigo, se basa en la **indentacion**, consiste en la inclusión de espacios o caracteres de tabulación al inicio de las lineas logicas.
Python usa la indentación de las lineas logicas para determinar la agrupacion de sentencias, por ejemplo:

```
def printer():
 #los espacios al inicio de estas lineas son la indentación
 print('hola')

printer() #llamado a la funcion printer() por fuera ya de la funcion
```

* Se recomiendan 4 espacios
* Con una mala implementacion de la indentacion el codigo no funcionará

### Comentarios

```
# Comentario

# Uniendo lineas fisicas de forma implicita se puede agregar comentarios en el medio 

month_names = ['January', 'February', 'March', # Primer trimestre               'April', 'May', 'June', # Segundo trimestre
'July', 'August', 'September', # Tercer trimestre
'October', 'November', 'December'] # Cuarto trimestre
```

### Tokens del lenguaje

Son componentes fundamentales del lenguaje que forman las lineas logicas.

* **NewLine** -> Determina el fin de una linea logica y el comienzo de otra
* **Indent** -> Indentacion de las sentencias dentro de una sentencia compuesta
* **Dedent** -> Fin de la indentacion que determina el fin de una sentencia compuesta

No son los unicos tokens del lenguaje, agunos facilitan la creacion de distintas estructuras, entre ellos podemos mencionar el uso de **identificadores**.

### Identificadores

Son aquellos nombres que identifican a variables, funciones, clases, metodos, constantes, modulos, paquetes, etc..
Dichos tokens se comienzan con letras que pueden ser mayúsculas o minúsculas o con guion bajo y luego pueden contener dígitos, letras o más guiones bajos. Es importante tener en cuenta que Python es un lenguaje Case Sensitive, lo que significa que las letras mayúsculas son distintas de las minúsculas. Por ejemplo:

```

```

