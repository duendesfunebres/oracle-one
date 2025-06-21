
import sqlite3
import csv
import os

def Tiendas(tiend):
    cantidad_filas=0
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    local = f"tienda{tiend}"
    cursor.execute(f"SELECT COUNT(*) FROM {local}")  
    cantidad_filas = cursor.fetchone()[0]
    conn.close
    if cantidad_filas == 0:
        conn = sqlite3.connect('challengue.db')
        cursor = conn.cursor()
        tiendas = {
            "01": ("db/tienda1.csv", "tienda01"),
            "02": ("db/tienda2.csv", "tienda02"),
            "03": ("db/tienda3.csv", "tienda03"),
            "04": ("db/tienda4.csv", "tienda04")
        }
        if tiend not in tiendas:
            print("Código de tienda no válido.")
            return
        tienda, tien = tiendas[tiend]
        with open(tienda, 'r', encoding="utf-8") as nuevos:
            insertar = csv.reader(nuevos, delimiter=',')
            filas = list(insertar)
        datos = [tuple(fila) for fila in filas if len(fila) == 12]

        if datos:
            print(f"Datos procesados: {datos}")
        try:
            cursor.executemany(f"INSERT INTO {tien} (Producto, Categoria, Precio, Costo_envio, Fecha_compra, Vendedor, Lugar_compra, Calificacion, Metodo_pago, Cuotas,Lat,Lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
            conn.commit()
            cursor.execute(f"SELECT COUNT(*) FROM {tien}")
            print(f"Total de filas en {tien} después de la inserción: {cursor.fetchone()[0]}")
        except sqlite3.Error as e:
            print(f"Error en la inserción: {e}")
        finally:
            conn.close()
            print("BASE DE DATOS MIGRADA CON ÉXITO")

def sumatoria(local):
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    instruccion = f"SELECT SUM(precio) FROM {local}"; #f"INSERT INTO rubrodb VALUES (Null,'{nombre}', '{activo}')"
    cursor.execute (instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close
    return datos

def categoria_mas_popular(local):
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    instruccion ="SELECT categoria, SUM(precio) AS total_ingresos FROM {} GROUP BY categoria ORDER BY total_ingresos DESC LIMIT 5".format(local)
    cursor.execute (instruccion)
    datos = cursor.fetchall()
    conn.close()
    return datos

def promedios (local):
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    instruccion = f"select AVG(calificacion) FROM {local}";
    cursor.execute (instruccion)
    datos = cursor.fetchone()
    conn.close()
    return datos

def productos (local):
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    instruccion = "SELECT producto, SUM(precio) AS total_ingresos FROM {} GROUP BY producto ORDER BY total_ingresos DESC LIMIT 5".format(local)
    cursor.execute (instruccion)
    datos = cursor.fetchall()
    conn.close()
    return datos

def envio(local):
    conn = sqlite3.connect('challengue.db')
    cursor = conn.cursor()
    instruccion = f"select AVG(costo_envio) FROM {local}";
    cursor.execute (instruccion)
    datos = cursor.fetchone()
    conn.close()
    return datos