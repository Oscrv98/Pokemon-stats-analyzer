import sqlite3
import os

def create_database():
    #Crea la bd
    db_path = 'pokemon.db'  #Nobre de la Bd
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #SQL script
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemons (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type_1 TEXT,
            type_2 TEXT,
            image_url TEXT,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            special_attack INTEGER,
            special_defense INTEGER,
            speed INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f" Base de datos creada: {os.path.abspath(db_path)}")

def test_connection():
    #Test a la Bd
    db_path = 'pokemon.db'
    
    if os.path.exists(db_path):
        print(f"!! ARCHIVO ENCONTRADO: {db_path}")
        print(f"Tamaño: {os.path.getsize(db_path)} bytes")
        
        # Mostrar contenido
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pokemons")
        pokemons = cursor.fetchall()
        print(f" Pokémon en BD: {len(pokemons)}")
        conn.close()
    else:
        print(f" NO EXISTE: {db_path}")

if __name__ == "__main__":
    create_database()
    test_connection()