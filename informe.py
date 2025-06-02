def resumen ():

    import matplotlib.pyplot as plt


    # Abrir el archivo en modo lectura
    with open("1-Facturacion total por tienda.txt", "r", encoding="utf-8") as archivo:
        # Leer todas las líneas y guardarlas en una lista
        ventas = ventas = [float(linea.replace("$", "").replace(".", "").replace(",", "").strip()) for linea in archivo]
        print(ventas)
    # Mostrar la lista
    
    tiendas = ["tienda01", "tienda02", "tienda03", "tienda04"]
    # Crear el gráfico de barras
    plt.figure(figsize=(10,6))
    plt.bar(tiendas, ventas, color=['blue', 'green', 'red', 'orange'])

    # Etiquetas y título
    plt.xlabel("Tiendas")
    plt.ylabel("Facturación Total ($)")
    plt.title("Facturación Total de Cada Tienda")
    plt.xticks(rotation=90)

    # Mostrar el gráfico
    plt.show()


git rm --cached Léame.md
git rm --cached Léame.txt  # Si hay otro README con extensión .txt
git em --cached readme.me
git commit -m "Eliminando archivos README"
git push origin main

