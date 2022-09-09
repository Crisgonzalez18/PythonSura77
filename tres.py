#Crear un menu de 2 opciones

from msilib import PID_REVNUMBER


contador = 0
print("***MENU***")
print("1. Agregar pueblos")
print("2. Mostrar rutas")
print("3. Salir")
pueblos=[]

while(contador!=3):
    pueblo={}
    contador=int(input("Digite una opcion del menu"))
    if(contador==1):
        print("Agregando pueblo ")
        pueblo['nombre']= input("Ingrese el nombre del pueblo: ")
        pueblo['distancia']= int (input("Ingrese la distancia"))
        pueblo['poblacion']= int (input("Ingrese el numero de habitantes: "))
        pueblos.append(pueblo)
    elif(contador==2):
        print("Mostrando rutas ")
        print(pueblos)
    elif(contador==3):
        print("Saliendo")
        break
    else:
        print("Opcion invalida")