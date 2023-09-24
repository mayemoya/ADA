#Define una variable de cada tipo de primitivo
string = "Trabajo"
integer = 78
flotante = 3.1415
bole = True

#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
cadena = string + " " + str(integer) + " " + str(flotante) + " " + str(bole)

#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
#De acuerdo al docs de python, el número de enteros es ilimitado y el de flotantes lo determina la capacidad de la computadora y se puede averiguar utilizando sys.float_info.
#Otros autores afirman que el numero de enteros esta definido por la capacidad que tenga la computadora para almacenarlo y en cuanto a los flotantes tiene un valor minimo y maximo: La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
#Declaramos la variable n
n = integer
# Calculamos la suma de los primeros n números pares
suma = n * (n + 1)

#Imprimir los resultados de las tareas anteriores

print("Variable de tipo cadena:", string)
print("Variable de tipo entero:", integer)
print("Variable de tipo flotante:", flotante)
print("Variable de tipo booleano:", bole)
print("Cadena concatenada:", cadena)
print("Suma de los primeros n números pares:", suma)

