# Metodos Dunder o Metodos magicos

Estos metodos permiten sobrecargar operadores que vienen construidos por defecto en Python, un ejemplo de esto es el 
siguiente codigo de un método que corresponde a la clase Gaussian:
```
def __repr__(self):
    
        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Return a string in the following format - 
        # "mean mean_value, standard deviation standard_deviation_value"
        # where mean_value is the mean of the Gaussian distribution
        # and standard_deviation_value is the standard deviation of
        # the Gaussian.
        # For example "mean 3.5, standard deviation 1.3"
        return f"mean {self.mean}, standard deviation {round(self.stdev,1)}"
```
En este caso se sobrecarga le metodo PRINT de python para que imprima una linea con las caracteriscas del Gaussian Object.
 De esta manera cuando se invoque la función PRINT se obtendra el siguiente resultado:
 Aqui se instancia un objeto Gaussiano con Promedio 5 y una desviación estandar de 2
 ```
 gaussian_one = Gaussian(5, 2) 
 ```
 Luego el ejecutar el PRINT se obtiene el siguiente  resultado:
  ```
 Línea de codigo:
 
	print(gaussian_sum)
	
 Resultado
 
	"mean 15, standar deviation 2.23606797749979"
  ```