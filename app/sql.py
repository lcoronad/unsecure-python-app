import sqlite3


def buscar_usuario(username: str) -> list:
    """CWE-89: SQL injection via f-string in execute()."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # Intentionally vulnerable
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()
