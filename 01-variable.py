#variables
#las variables son en minusculas
my_variable = "My String"
print(my_variable)

int_variable = 5

bool_variable = True

#concatenacion de variables
print(my_variable,"=",int_variable)

# cambiar el tipo de variable con una funcion resevada
int_to_str = str(int_variable)

# algunas funciones del sistema
print(len(my_variable)) #cuenta todos los caracteres al igual que los espacios

#variables en una sola linea
name, lastname, age = "jonathan","Sanchez",21
print(lastname,age,name)

#inputs
""""
firstname = input("introduce tu nombre: ")
edad = input("introduce tu edad: ")

print("nombre: ",firstname)
print("Edad: ",edad)
"""

#cambiando el tipo 
name = 35
age = "diesiocho"
print("nombre: ",name)
print("Edad: ",age)
