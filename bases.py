
def createdb ():
    import sqlite3 as sql
    conn= sql.connect ("challengue.db")
    conn.commit()
    conn.close()

def createtablas ():
    import sqlite3 as sql

    # Conectar a la base de datos
    conn = sql.connect('challengue.db')
    cursor = conn.cursor()

    # Lista de nombres de tablas que quieres crear
    tiendas = [f"tienda{str(i).zfill(2)}" for i in range(1, 5)]  # tienda01, tienda02, tienda03, tienda04

    # Crear tablas dinámicamente
    for tienda in tiendas:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {tienda} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Producto TEXT,
            Categoria TEXT,
            Precio REAL,
            Costo_envio REAL,
            Fecha_compra TEXT,
            Vendedor TEXT,
            Lugar_compra TEXT,
            Calificacion INTEGER,
            Metodo_pago TEXT,
            Cuotas INTEGER,
            Lat REAL,
            Lon REAL
        )
        """)

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()
