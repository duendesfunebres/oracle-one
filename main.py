import matplotlib.pylab as plt
import Tablas

import pandas as pd
from colorama import init, Fore, Back
init(autoreset=True) 
init()

def limpiar ():
    from os import system
    system ("cls")

import bases
bases.createdb()
bases.createtablas()
Tablas.Tiendas("01")
Tablas.Tiendas("02")
Tablas.Tiendas("03")
Tablas.Tiendas("04")


from colorama import init, Fore
init(autoreset=True) 
init()
opcion = 0
while opcion >= 0 or opcion < 8:
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.BLUE + " MENÚ PRINCIPAL".center(100))
    print (Fore.BLUE + " -(Elija una opción)- ".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print ("")
    print (Fore.BLUE + "1- Facturación total de cada tienda")
    print (Fore.BLUE + "2- Categorias mas populares")
    print (Fore.BLUE + "3- Promedio de calificación de los clientes")
    print (Fore.BLUE + "4- Productos mas y menos vendidos")
    print (Fore.BLUE + "5- Costo promedio del envío")
    print (Fore.BLUE + "6- Informe General")
    print (Fore.BLUE + "7- Salir")
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")

    try:
        #input de elecciòn opciòn de demenù
        opcion = int(input("Seleccione una opción por su número: "))
        # captura de errores
    except ValueError:
        print (Fore.RED + "La opción que ingreso no es válida, vuelva a intentarlo")
        # tiempo para que se lea el enunciado del informe
        import time
        time.sleep (2)
    # llamado a limpiar la patalla para que se efectìe arrastre de menùes y se preste a confusióm
    limpiar()

    match  opcion: 
        # opciòn de selecciòn del primer item
        case 1:
            print ( Fore.BLUE + "__-** FACTURACION TOTAL DE CADA TIENDA **- ___".center(80))
            print ("")
            print (80*"-")
            #Generando una lsita para luego iterar sobre cada tienda
            total_tiendas= ("tienda01", "tienda02", "tienda03", "tienda04")
            # Apertura de archivo txt para guardar resultados
            with open("1-Facturacion total por tienda.txt", "w", encoding="utf-8") as archivo:
                archivo.write("") 
            # iteracción por la cantidad de elementos de "total_tiendas"
            for i  in total_tiendas:
                # Recepción de datos de lo que devuelve la funciòn de sumatoria de cada tienda 
                sumatoria = Tablas.sumatoria (i)
                print (sumatoria)
                # totales pasados a pesos
                sumatoria =  "${:,.2f}".format(sumatoria[0][0]).replace(",", "X").replace(".", ",").replace("X", ".")               
                # abertura de archivo txt para guardar resultados de cada tienda
                with open("1-Facturacion total por tienda.txt", "a", encoding="utf-8") as archivo:
                    archivo.write(sumatoria + "\n")
                print("")
                # Muestra en pantalla de Informe de los resultados por cara tienda 
                print (("LA SUMA TOTAL DE VENTAS EN " + Fore.GREEN + f" {i}" + Fore.RED + f"  {sumatoria}").center(80))
                print("")
                print (80*"-")


        case 2:
            total_locales = ("tienda01","tienda02","tienda03","tienda04")
            with open("2-Categorias mas populares.txt", "w", encoding="utf-8") as archivo:
                archivo.write("") 
            for i in range(len(total_locales)):
                valor=(total_locales[i])
                lista_resultados = Tablas.categoria_mas_popular(valor) # Ahora Python sabe qué es
                df_resultados = pd.DataFrame(lista_resultados, columns=['Categoría', 'Total Ingresos'])
                print(Fore.RED + f"--- Top 5 Categorías más populares para: {valor} ---")
                df_resultados.to_csv('2-Categorias mas populares.txt', sep='\t', index=False)
                print (df_resultados.to_string(index=False))
                print (50*"*")

        case 3:
            
            total_tiendas= ("tienda01", "tienda02", "tienda03", "tienda04")
            with open("3-Promedio de calificación de los clientes", "w", encoding="utf-8") as archivo:
                archivo.write("") 
            with open("3-Promedio de calificación de los clientes", "a") as archivo:  # Abre el archivo en modo escritura
                for i  in total_tiendas:
                    promedio = Tablas.promedios (i)
                    promedio = round(promedio [0],3)
                    print (("EL PROMEDIO DE CALIFICACIONES DE " + Fore.GREEN + f" {i}" + Fore.RED + f"  {promedio}").center(80))
                    print("")
                    print (80*"-")
                    info = (i) + (" ") + (str(promedio) + "\n")
                    archivo.write (info)
                    archivo.write("\n")


        
        case 4:

            from colorama import Fore
            total_locales = ("tienda01", "tienda02", "tienda03", "tienda04")
            for valor in total_locales:
                    lista_resultados = Tablas.productos(valor)
                    
                    # Convierto lista_resultados en DataFrame
                    df_resultados = pd.DataFrame(lista_resultados, columns=['producto', 'Total Ingresos'])
                    # Ordeno ascendentemente por ingresos
                    df_mas_vendidos = df_resultados.sort_values(by='Total Ingresos', ascending=False).head(5)
                    df_menos_vendidos = df_resultados.sort_values(by='Total Ingresos', ascending=True).head(5)
                    # Renombro columnas para diferenciarlas
                    df_mas_vendidos = df_mas_vendidos.rename(columns={'producto': 'Más Vendidos', 'Total Ingresos': 'Ingresos Más Vendidos'})
                    df_menos_vendidos = df_menos_vendidos.rename(columns={'producto': 'Menos Vendidos', 'Total Ingresos': 'Ingresos Menos Vendidos'})
                    # genera un espacio entre columnas para que visualmente se vea una sepacación
                    espacio = pd.DataFrame({" ": [""] * 5})  
                    # Se unen los DataFrames
                    df_final = pd.concat([df_mas_vendidos.reset_index(drop=True), espacio, df_menos_vendidos.reset_index(drop=True)], axis=1)
                    # cambiar formato int a pesos
                    columnas_ingresos = ['Ingresos Más Vendidos', 'Ingresos Menos Vendidos']
                    for col in columnas_ingresos:
                        df_final[col] = df_final[col].apply(lambda x: "${:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", "."))
                    # Se muestran resultados
                    print(Fore.RED + f"Productos MAS VENDIDOS en {valor}" + Fore.YELLOW + " Vs " + Fore.GREEN + f"Productos MENOS VENDIDOS en {valor}")
                    print(df_final.to_string(index=False))
                    print(82 * "*")

        case 5:
            # genero un separador de asteriscos como divisor de 80 espacios
            print (Fore.CYAN + 80*"-")
            # genero una lista de las distintas tiendas que voy a enviar a procesar
            total_tiendas= ("tienda01", "tienda02", "tienda03", "tienda04")
            # imprimo titulo en color Cyan
            print(Fore.CYAN + f"--- PROMEDIO DE ENVÌOS POR TIENDA ---".center(80))
            print (Fore.CYAN + 80*"-")
            # recorro toda la lista por cada item que la compone
            for i  in total_tiendas:
                # Obtengo en la variable "promedio" el resultado solicitado a la funciòn "tabla .envìo" segùn el item "i"
                promedio = Tablas.envio (i)
                # redondeo de decimales en soo 4 posiciones
                promedio = round(promedio [0],4)
                print("")
                # se imprime el romedio por cada tienda
                print (("EL PROMEDIO DE ENVÌO " + Fore.GREEN + f" {i}" + Fore.RED + f"  {promedio}").center(80))
                print("")
                print (80*"-")


        case 6:
            import informe
            informe.resumen()

        case 7:
            confirmar = 3
            while confirmar>= 0 or confirmar <=3:
                limpiar()
                print ("confirme que desea salir del programa".center (100))
                print ("")
                print ("0- Si desea volver... ")
                print ("")
                print ("1- Terminar el programa y salir definitivamente")
                print ("")
                try:
                    confirmar = int(input("Seleccione una opción por su número: "))
                except ValueError:
                    from colorama import init, Fore
                    init(autoreset=True) 
                    init()
                    print (Fore.RED + "La opción que ingreso no es válida, vuelva a intentarlo")
                    import time
                    time.sleep (3)    
                else:
                    if confirmar == 0:
                        limpiar()
                        break
                    elif confirmar == 1:
                        limpiar()
                        quit()

    print(Fore.CYAN + "\nPresiona Enter para volver al menú...")
    input()  # Espera a que el usuario presione Enter
    limpiar()            


