def Fresumen (facturacion):
    from colorama import init, Fore, Style
    init(autoreset=True) 
    init()
    import matplotlib.pyplot as plt
    # Procesar los datos
    tiendas = list(facturacion.keys())
    valores = [v[0][0] for v in facturacion.values()]
    colores = ['red', 'blue', 'green', 'orange']
    # Crear gráfico
    fig = plt.figure(figsize=(8, 5))
    plt.bar(tiendas, valores, color=colores)
    plt.xlabel('Tiendas')
    plt.ylabel('Valor')
    plt.title('Valores por Tienda')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    tienda_min = min(facturacion.items(), key=lambda x: x[1][0][0])
    print ("")
    print (180*"-")
    print (" INFORME SOBRE FACTURACIÓN DE CADA TIENDA ".center(180))
    print (180*"-")
    print ("")
    print(f"El valor más bajo en facturación  corresponde a: {Fore.RED}{tienda_min[0]}{Style.RESET_ALL} con un valor de {Fore.RED}{tienda_min[1][0][0]:,.2f}".center(180))
    print (180*"-")
    print ("")
    plt.show(block=False)
    plt.pause(5) # Pausa por 5 segundos (ajusta el número según lo que necesites)
    plt.close(fig)



def FCategoria(datos):
    from colorama import init, Fore, Style
    init(autoreset=True) 
    init()
    import matplotlib.pyplot as plt
    import numpy as np

    # Extracción de nombres y ventas
    categorias = [cat for cat, _ in datos['tienda01']]
    tiendas = list(datos.keys())
    ventas = {tienda: [venta for _, venta in datos[tienda]] for tienda in tiendas}

    # Configuración del gráfico
    x = np.arange(len(categorias))  # Posiciones de las categorías
    width = 0.2  # Ancho de las barras

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, tienda in enumerate(tiendas):
        ax.bar(x + i * width, ventas[tienda], width, label=tienda)


    ventas_totales = {tienda: sum(venta for _, venta in productos) for tienda, productos in datos.items()}
    # Encontrar la tienda con menor venta
    tienda_menos_vendio = min(ventas_totales, key=ventas_totales.get)

    # Etiquetas y formato
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Ventas')
    ax.set_title('Comparación de ventas por tienda')
    ax.set_xticks(x + width * (len(tiendas) / 2 - 0.5))
    ax.set_xticklabels(categorias, rotation=45)
    ax.legend()
    print ("")
    print (Fore.LIGHTGREEN_EX + 180*"-")

    print (Fore.GREEN + "INFORME SOBRE FACTURACIÓN POR CATEGORÌA DE CADA TIENDA ".center(180))
    print (Fore.LIGHTGREEN_EX + 180*"-")

    print ("")
    print (Fore.LIGHTGREEN_EX + 180*"-")
    print(Fore.LIGHTGREEN_EX + f"Las totales por categoría muestran a: {Style.RESET_ALL} {Fore.RED} {tienda_menos_vendio}{Style.RESET_ALL} , {Fore.LIGHTGREEN_EX}como la de menor facturaciòn de las 4 sucursales con un total de: {Style.RESET_ALL}{Fore.RED}{ventas_totales[tienda_menos_vendio]:,.2f}".center(180))
    print ("")
    print (Fore.LIGHTGREEN_EX + 180*"-")
    # Mostrar gráfico
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(5)
    plt.close(fig)




def Fevaluacion (dato02):
    from colorama import init, Fore, Style
    init(autoreset=True) 
    init()
    import matplotlib.pyplot as plt
    # Procesar los datos
    tiendas = list(dato02.keys())
    valores = list(dato02.values())  # Extrae los valores sin intentar indexar
    #alores = [v[0][0] for v in dato02.values()]
    colores = ['red', 'blue', 'green', 'orange']
    # Crear gráfico
    fig= plt.figure(figsize=(8, 5))
    plt.bar(tiendas, valores, color=colores)
    plt.xlabel('Tiendas')
    plt.ylabel('Valor')
    plt.title('Valores por Tienda')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    tienda_min = min(dato02.items(), key=lambda x: x[1])
    print ("")
    print (Fore.LIGHTMAGENTA_EX + 180*"-")
    print (Fore.LIGHTMAGENTA_EX + "INFORME SOBRE CALIFICACIÒN POR CLIENTE DE CADA TIENDA ".center(180))
    print (Fore.LIGHTMAGENTA_EX + 180*"-")
    print ("")
    print(Fore.LIGHTMAGENTA_EX + f"El valor más bajo en evaluación facturación  corresponde a: {Style.RESET_ALL} {Fore.RED}{tienda_min[0]}{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX} con un valor de: {Style.RESET_ALL}{Fore.RED}{tienda_min[1]:,.2f}".center(180))
    print (Fore.LIGHTMAGENTA_EX + 180*"-")
    print ("")
    plt.show(block=False)
    plt.pause(5)
    plt.close(fig)


def Fenvio(envio):
    from colorama import init, Fore, Style
    init(autoreset=True) 
    init()
    import matplotlib.pyplot as plt
    # Procesar los datos
    tiendas = list(envio.keys())
    valores = [v[0] for v in envio.values()]
    colores = ['red', 'blue', 'green', 'orange']
    # Crear gráfico
    fig = plt.figure(figsize=(8, 5))
    plt.bar(tiendas, valores, color=colores)
    plt.xlabel('Tiendas')
    plt.ylabel('Valor')
    plt.title('Valores por Tienda')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    tienda_min = min(envio.items(), key=lambda x: x[1])
    print ("")
    print (Fore.LIGHTBLUE_EX + 180*"-")
    print (Fore.LIGHTBLUE_EX + "Costo promedio del envío por tienda".center(180))
    print (Fore.LIGHTBLUE_EX + 180*"-")
    print ("")
    print(Fore.LIGHTBLUE_EX + f"El valor más bajo en facturación corresponde a: {Fore.RED}{tienda_min[0]}{Style.RESET_ALL} con un valor de {Fore.RED}{tienda_min[1][0]:,.2f}".center(180))
    #print(f"El valor más bajo en facturación  corresponde a: {Fore.RED}{tienda_min[0]}{Style.RESET_ALL} con un valor de {Fore.RED}{tienda_min[1]:,.2f}".center(180))
    print (Fore.LIGHTBLUE_EX + 180*"-")
    print ("")
    plt.show(block=False)
    plt.pause(5) # Pausa por 5 segundos (ajusta el número según lo que necesites)
    plt.close(fig)