import os
import matplotlib.pyplot as plt

#Limpia la terminal cada vez que se corra el programa
os.system('cls' if os.name == 'nt' else 'clear')

#Hacemos listas vacias de lo que necesitamos para agregar categorias y valores
total_gasto=0
categorias=[]
valores=[]
porcentaje=[]
print("---PROGRAMA DE REGISTRO DE GASTOS---")  #Iniciación del programa
for i in range (3):   #Nos aseguramos que solo existan 3 registros
    try:
        categorias_gasto=input('Ingrese 3 categorias de gasto: ').capitalize() #Ingreso de la categoria en mayúscula
        valor_gastado_str=input('Ingrese el valor gastado: ')
        valor_gastado=float(valor_gastado_str) #Convertimos el ingreso del valor a float 
        if valor_gastado <0:
            print(f'El valor {valor_gastado_str} no puede ser negativo') #Nos aseguramos que valor_gastado sea mayor a cero
            continue #Sigue a la siguiente entrada
        valores.append(valor_gastado)   #Añadimos el valor_gastado a nuestra lista vacia (valores)
        categorias.append(categorias_gasto) #Añadimos cada categoria a nuestra lista vacia (categorias)
        total_gasto+=valor_gastado  #Obtenemos el total del valor gastado proporcionado

    except ValueError:   #Si ingresan algo diferente a un numero les sale un mensaje de Error
        print(f'✘ Error: {valor_gastado_str} no es un número valido.')
        continue
    except Exception as e:  # Captura cualquier otro error inesperado durante la entrada de datos
        print(f"✘ Ocurrió un error inesperado al procesar la entrada: {e}. Esta entrada será ignorada.")
        continue # También continúa para pedir las 3 entradas

try:
    if total_gasto== 0:  #Si no hay valores en el total_gasto nos imprime un mensaje
        print('---No se registraron valores válidos---')
    else: 
        for valor in valores: #Iteramos cada valor en la lista (valores)
            porcentajes=valor/total_gasto #Calculamos el porcentaje de cada entrada
            porcentaje.append(porcentajes) #Añadimos cada porcentaje a nuestra lista vacia (porcentajes)

        #CREACIÓN DEL GRAFICO 
        plt.pie(porcentaje, labels=categorias, autopct='%1.1f%%', startangle=90, #autopct nos muestra los valores en formato porcentaje
                colors=['#2ecc71','#27ae60','#16a085'],
                textprops={'fontsize':8, 'color': 'black','fontweight':'bold'}) #Añadimos colores, modificamos las etiquetas, etc.
        plt.title('Distribución de Gastos Personales', fontsize=16,color='black',fontweight='bold') #Añadimos un titulo modificado a nuestro gusto
        plt.axis('equal') #Con esto nos aseguramos que sea un circulo

        #GUARDAR EL GRÁFICO
        nombre_archivo='gastos_personales.png'
        plt.savefig(nombre_archivo,bbox_inches='tight',dpi=300) #bbox recorta bordes y dpi establece una resolucion
        plt.show() #Mostramos el gráfico
except ZeroDivisionError: #Captura si esque total gasto = 0
    print('✘ Error de calculo, no se puede dividir para cero.')
except Exception as e:  #Captura cualquier otro error vario
    print('✘ Se ha producido un error')

print('---Programa finalizado---')