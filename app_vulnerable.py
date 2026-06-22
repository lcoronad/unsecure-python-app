import sqlite3
import hashlib

def buscar_usuario(username):
    # CRÍTICO (CWE-89 - Inyección SQL): Concatenación directa de entradas del usuario
    # OpenGrep/Semgrep detectará esto inmediatamente como un riesgo severo.
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def almacenar_password(password):
    # ADVERTENCIA (CWE-327 - Algoritmo criptográfico roto/débil): MD5 ya no es seguro
    # OpenGrep alertará que se debe usar bcrypt, Argon2 o al menos SHA-256.
    cipher = hashlib.md5()
    cipher.update(password.encode('utf-8'))
    return cipher.hexdigest()