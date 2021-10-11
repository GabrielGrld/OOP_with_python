# OOP_with_python


Introducción a la programación orientada a objetos con Python

OOP tiene varios beneficios comparado con la programacion procedimental (procedural programming)

	- OOP permite crear programas grandes y modulares los cuales pueden ser 
	 facilmente expandibles en el tiempo.
	- OOP esconden la implementación del programa para que no sea visible por el usuario final.
	
Ejemplos de paquetes de Python construidos con programación orientada a objetos son Scikit-learn, 
pandas y NumPy. Scikit-learn es una paquete construido con OOP, este paquete se ha expandido a lo 
largo de años con nuevas funcionalidades y nuevos algoritmos.

Cuando se entrena una algoritmo de Machine Learning con Scikit-learn, no se necesita saber como los
algoritmos funcionan o como estan escritos, es solo necesario  concentrarse en el modelado.

# Objetos:

Los objetos estan definidos por caracteristicas y acciones. 

Ejemplo de caracteristicas y acciones para un vehiculo:

	- Caracteristicas:
		- Color
		- Tamaño
		- Puertas
		- Precio
	- Acciones 
		- Acelerar
		- Frenar
		

# Vocabulario de la Programación Orientada a Objetos (OOP)

	- **Clases**: A blueprint que consiste de Métodos y atributos
	- **Objetos**: Una instancia de una clase. Ejemplo en el mundo real sería un lapicero rojo, un pero 
	pequeño, o una camisa azul
	- **Atributos**: Un descriptor o caracteristica, ejemplo de esto sería color, longitud, tamaño, 
	entre otros. Estos atributos pueden tomar
	valores espcificos como azul, 3 centimetros, largo 
	- **Metódos**: Una acción que una clase u objeto puede hacer.
	- **OOP**: Una abreviación común usada para programación orientada a objetos.
	- **Encapsulación**: Una de las ideas fundamentales detrás de la programación orientada a objetos 
	es lamada encapsulación: se puede combinar funcines e informacion todo en una sola entidad. En la
	programación orientada a objetos,  esta entidad singular es llamada una clase. La encapsulación 
	permite esconder detalles de implementación, muy similar a como funcionan paquetes de Python como 
	NumPy y Scikit-learn.
	
	
# Notas sobre OOP

Set and Get methods

Acceder atributos en Python es ciertamente difirente a comparación de otros lenguajes de programación como Java
y C++. 
```
	class Shirt:

		def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
			self.color = shirt_color
			self.size = shirt_size
			self.style = shirt_style
			self.price = shirt_price
		
		def change_price(self, new_price):
		
			self.price = new_price
			
		def discount(self, discount):

			return self.price * (1 - discount)
```

La clase Shirt tiene un método para cambiar el precio de la camiseta: shirt_one.chane_price(25).
En python,  también se puede cambiar los valores del un atributo con la siguiente sintaxis:

	shirt_one.price = 15
	shirt_one.price = 25
	shirt_one.color = 'blue'
	shirt_one.size = 'L'
	shirt_one.style = 'short_sleeve'
	
Este código accede y cambia directamente los atributos de precio, color, tamaño y estilo.
 Acceder a los atributos directamente estaría mal visto en muchos otros lenguajes, pero no en Python.
En cambio, la convención general de programación orientada a objetos es utilizar métodos para acceder 
a los atributos o cambiar los valores de los atributos. Estos métodos se denominan métodos **set** y **get** 
o métodos **setter** y **getter**.

Un método **get** es para obtener un valor de atributo. Un método **set** es para cambiar el valor de un atributo.
 Si estuviera escribiendo una clase de camisa, podría usar el siguiente código:
 ```
	 class Shirt:

		def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
			self._price = shirt_price

		def get_price(self):
		  return self._price

		def set_price(self, new_price):
		  self._price = new_price
```
Cuando se instancia y usa un objeto se obtiene un codigo que podría ser el siguiente:
```
	shirt_one = Shirt('blue', 'S', 'short-sleeve', 20)
	print(shirt_one.get_price())
	shirt_one.set_price(12)
```

En la definición delas clases, al guión bajo al frente de **price** es de alguna manera controversial en Python, 
en otros lenguajes como Java y C++, **price** podría ser declarada como una variable privada.  Lo cúal prevendría
un objeto de acceder al atributo directamente como **shirt_one._price=15**. A diferencia de otros lenguajes, Python 
no distingue entre variables publicas y privadas. Por lo tanto existe cierta controversia acerca de usar la convención
de guión bajo como también los Métodos **get** y **set** en Python.

Siguiendo la convención de Python, el subrayado delante del precio es para que un programador sepa que solo se debe
 acceder al precio con los métodos **get** y **set** en lugar de acceder al precio directamente con **shirt_one._price**. Sin 
 embargo, un programador aún podría acceder a **_price** directamente porque no hay nada en el lenguaje Python que 
 impida el acceso directo.
 
 Mas información acerca de los metódos **get** and **set** puede ser consultada en esta pagina [OOP Python Tutorial](https://www.python-course.eu/python3_properties.php).

En términos de programación orientada a objetos, las reglas en Python son un poco más flexibles que en otros lenguajes de programación.
 Como se mencionó anteriormente, en algunos lenguajes, como Java, puede indicar explícitamente si se debe permitir o no que un objeto
 cambie o acceda a los valores de un atributo directamente. Python no tiene esta opción.

¿Por qué sería mejor cambiar un valor con un método en lugar de hacerlo directamente? Cambiar valores a través de un método le brinda más
 flexibilidad a largo plazo. ¿Qué pasa si las unidades de medida cambian, como si la función para calcular distancia esta en millas y se 
 necesita luego que todas las distancias se calculen en ilometros,ejemplo de esto sería:
 
 Medida tomada esta en millas
 ```
 distance_one.measure = 10
 ```
 Para cambiarlo a kilometros habría que hacerlo manualmente en cada distancia
 ```
 distance_une.measure = 16.09
 ```
 Si se hubiese usado un método, unicamente se tendría que cambiar el métodos para convertir de millas a kilometros
 
 
	def change_measure(self, new_measure):
		self.measure = new_measure * 1.61 # convertir millas a kilometros

	distance_one.change_measure(10)
 
 
Código modularizado

Si se estuviera desarrollando un programa de software, y se quisiera modularizar este código. Colocaría la clase 
**Shirt** en su propia secuencia de comandos de Python, que podría llamar **shirt.py**. En otro script de Python, 
importaría la clase **Shirt** con una línea:
```
 from shirt import Shirt.
 ```

# Commenting object-oriented code

Un **docstring** es un tipo de comentario que describe como un modulo, funcion, clase o metódo de Python funciona. 
**Docstring** no son propios unicamente de la programación orientada a objetos (**OOP**)

Es importante usar **docstrings** y comentar el codigo desarrollado. De esta manera sera entendible y mantenible
en el futuro. 

## Docstrings and object-oriented code

	* Se debe asegurar que el docstring este indentado correctamente, o el codigo no correra. Un docstring debería 
	ser indentado con una indentación debajo de la clase o métodos que esta siendo descrito.
	* No se debe definir **self** en el métodos de you docstrings. Se entiende que cualquier metódo tendrá **self**
	como el primer valor de ingreso (input).
```	
	class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
```
source: Introduction to Object-Oriented- Programming, Udacity

## Herencia en OOP Python

La  herencia consiste de una clase mas general la cual tiene definido unos Métodos y atributos que son comunes
entros las clases hijas. Un ejemplo de lo anterior sería una clase Padre **Prendas_Vestir** la cual contiene los siguientes 
atributos y Métodos:

	- **Prendas_Vestir**
		- *Atributos*
			-color
			-tamaño
			-estilo
			-precio
		- *Métodos*
			- cambiar_precio()
			- precio_descuento()
			
Todo los campos anteriores serian comunes a clases como *Camisas*, *Pantalon*, *Medias*, *Vestido*

Observando lo anterior se puede preguntar por que codificar cada Clase por si misma, cuando todas estas tienen tanto en común, 
de esta manera se llega a la conclusión de que es posible codificar o programar una clase superior **Prendas_Vestir**, de la cual heredaran
las clases *Camisas*, *Pantalon*, *Medias* y  *Vestido* sus atributos y Métodos. Esto se puede ver como la clase padre (**Parent Class**) tiene 
clases hijas (**Child Class**).

Un beneficio de lo anterior es que es posible crear otras clases hijas a partir de la clase padre. En ciertos ocasiones será necesario 
agregar atributos y Métodos propios de estás clases. 

## Métodos Magicos (Dunder or Magic Methods)

Esta funcionalidad permite  realizar sobrecarga de Métodos, lo que significa modificar las operadores con los que python   cuenta por defecto
Los Métodos magicos (también conocidos como Métodos Dunder) tienes dos guiones bajos al inicio y final del nombre del métodos.
Algunos ejemplos de Métodos magicos son:  \_\_init\_\_, \_\_add\_\_, \_\_len\_\_, \_\_repr\_\_ entre otros.
Esto es muy útil cuando se esta desarrollando una clase particular que requiere una operación particular. Por lo cual operadores que ya
vienen construidos no permitirian hacer las operaciones deseadas entre estás clases.