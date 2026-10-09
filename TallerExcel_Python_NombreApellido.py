from unittest import case

import openpyxl as op
from tabulate import tabulate

excel_dataframe = op.load_workbook("personas.xlsx")

dataframe = excel_dataframe.active
data =[]

for row in range(1, dataframe.max_row):
    _row =[row]
    for col in dataframe.iter_cols(1, dataframe.max_column):
        _row.append(col[row].value)
    data.append(_row)

headers = ["#", "Id", "Name", "Company", "Email", "MAC Address"]
headers_aling = ("center") * 6

#print(tabulate(data, headers=headers, tablefmt="fancy_grid", colalign=headers_aling))

## Reto 1: Mostrar únicamente Name y Email.  

def nombre_email(datos):
    nombre_email = [(row[2], row[4]) for row in datos] #es un for para recorrer la lista de datos y obtener el nombre y el correo electrónico de cada persona.
    print(tabulate(nombre_email, headers=["Name", "Email"], tablefmt="fancy_grid", colalign=("center"))) # este print tabulate es para mostrar la lista de nombre y correo electrónico en una tabla.

##Reto 2: Mostrar cuántos registros tiene el archivo.
def registro(datos):
    cantidad = []
    for row in datos:
        cantidad.append(row[0])
    print(f"numero de registros: {len(cantidad)}") # esto es para el total de usuarios
def registro_total(datos):
    cantidad = []
    columnas  = len(datos[0])
    for row in datos:
        cantidad.append(row[0])
    print(f"numero de registros totales: {len(cantidad * columnas)}") # esto es para el total de registros en la tabla osea cada celda que tiene un valor en la tabla.

## Reto 3: Filtrar personas cuya empresa contenga la palabra Group.
def filtrar_group(datos):
    group = [row for row in datos if "Group" in str(row[3])] # aca se filta y se guarda solo lo que tiene group en alguna parate
    print(tabulate(group, headers=headers, tablefmt="fancy_grid", colalign=("center",)))

##Reto 4: Pedir un ID con input() y mostrar solo esa persona

def filtrar_id(datos):
    id_persona = input("Ingrese el ID de la persona: ")
    resultado = [row for row in datos if str(row[1]) == id_persona] # aca se busca el id que se ingreso y se guarda en resultado    
    print(tabulate(resultado, headers=headers, tablefmt="fancy_grid", colalign=("center",) * 6))


def menu():
    while True:
        opcion = input("Ingrese una de las siguientes opciones: \n1. Mostrar toda la tabla \n2. Mostrar únicamente Name y Email \n3. Mostrar cuántos registros tiene el archivo \n4. Mostrar cuántos registros totales tiene el archivo \n5. Filtrar personas cuya empresa contenga la palabra Group \n6. Buscar persona por ID \n7. Salir \nOpción: ")
        match opcion:
            case "1":
                    print(tabulate(data, headers=headers, tablefmt="fancy_grid", colalign=headers_aling))
                
            case "2":
                    nombre_email(data)
                
            case "3":
                    registro(data)
                    
            case "4":
                    registro_total(data)
                    
            case "5":
                    filtrar_group(data)
                    
            case "6":
                    filtrar_id(data)
            
            case "7":
                    print("Saliendo del programa.")
                    break
            case _:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            
menu()