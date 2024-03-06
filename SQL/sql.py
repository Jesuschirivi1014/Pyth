import sqlite3

# Crear conexión
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS productos
               (NUMEROS_EQUIPOS, JUGADORES, POSICION, EDAD)''')
conn.commit()

# Insertar datos
productos = [
    ('Colombia', 50.0, 100),
    ('Venezuela', 70.0, 80),
    ('Argentina', 60.0, 120),
    ('Paraguay', 90.0, 60),
    ('Brasil', 55.0, 150) 
    ('Bolivia', 55.0, 150)    
    ('Peru', 55.0, 150)    
    ('Canda', 55.0, 150)    
    ('Mexico', 55.0, 150)   
    ('Ecuador', 55.0, 150) 
    ('Costa rica', 55.0, 150)    
    ('Estados unidos', 55.0, 150)           
]
cursor.executemany('INSERT INTO productos (nombre, precio, stock) VALUES (?,?,?)', productos)
conn.commit()

# Consultar datos
cursor.execute('SELECT * FROM productos WHERE precio > 50')
resultados = cursor.fetchall()
print("Productos con precios superiores a $50:")
for producto in resultados:
    print(producto)

# Actualizar datos
cursor.execute('UPDATE productos SET precio = 80.0 WHERE id = 1')
conn.commit()
print("Precio actualizado para el producto A")

# Eliminar datos
cursor.execute('DELETE FROM productos WHERE id = 2')
conn.commit()
print("Producto B eliminado de la base de datos productos")

# Cerrar conexión
conn.close()