#Crear menu  empanada

contador = 0

print("***MENU***")
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")
empanadas=[]


while(contador!=3):
     ingredientes=[]
     empanada={}
     contador= int(input("Digite la opcion: "))
     if(contador==1):
        print("Agregando empanadas: ")
        empanada['Nombre']=input("Ingresar nombre empanada: ")
        for i in range (3):
            ingredientes.append(input(f'Digite el ingrediente {i+1}: '))
        
        empanada['ingredientes']=ingredientes
        empanada['Precio']=input("Ingresar precio: ")   
        empanadas.append(empanada)  
        
     elif(contador==2):
        print("Mostrando empanadas ")
        print(empanadas)
     elif(contador==3):
        print("Saliendo")
     elif(contador==3):
        print("Saliendo")
        break
    
     else:
        print("Opcion invalida")