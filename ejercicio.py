mi_diccionario = {}
import os
sw = True

def fnt_agregar(mi_diccionario, nombre, valor, horas,salario_mensual, salario_neto):
    if nombre == '' or valor == '' or horas == '':
        print('No se pueden dejar campos vacios')
    else:
        mi_diccionario[nombre]= {'valor de horas': valor, 'numero de horas': horas, 'salario basico': salario_mensual, 'salario neto': salario_neto}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')

        
        
def fnt_selector(opcion):
        if opcion == '1':
                nombre = input('Ingrese su nombre->')
                valor = int(input('Ingrese el valor de la hora->'))
                horas = int(input('Ingrese el número de horas trabajadas->'))
                if horas <= 120:
                    salario_mensual= horas *valor
                    if salario_mensual <=380000:
                        deduccion = salario_mensual * 0.10
                        salario_neto = salario_mensual - deduccion
                    elif salario_mensual > 380000 and salario_mensual <= 480000:
                        deduccion = salario_mensual * 0.20
                        salario_neto = salario_mensual - deduccion
                    elif salario_mensual > 480000:
                        deduccion = salario_mensual * 0.30
                        salario_neto = salario_mensual - deduccion
                elif horas >120:
                    horas_extras = input('¿Cuántas horas extras trabajaste este mes?')
                    salario_mensual = valor * horas +(horas_extras*(valor * 2))
                    if salario_mensual <=380000:
                                deduccion = salario_mensual * 0.10
                                salario_neto = salario_mensual - deduccion
                    elif salario_mensual > 380000 and salario_mensual <= 480000:
                                deduccion = salario_mensual * 0.20
                                salario_neto = salario_mensual - deduccion
                    elif salario_mensual > 480000:
                                deduccion = salario_mensual * 0.30
                                salario_neto = salario_mensual - deduccion
                
                fnt_agregar(mi_diccionario, nombre, horas, valor, salario_mensual, salario_neto)
        
        elif opcion == '2': 
            print("Registros:")
            for nombre, datos in mi_diccionario.items():
                print(f"Nombre: {nombre}")
                print(f"Valor de horas: {datos['valor de horas']}")
                print(f"Número de horas: {datos['numero de horas']}")
                print(f"Salario básico: {datos['salario basico']}")
                print(f"Salario neto: {datos['salario neto']}\n")
                enter = input ('Presione enter para continuar <ENTER>')

        elif opcion == '3':  
            global sw
            sw = False

sw = True

while sw:
    os.system('cls')
    opcion = input('1. Registrar \n2. Mostrar \n3. Salir\n-> ')
    fnt_selector(opcion)
        
        
