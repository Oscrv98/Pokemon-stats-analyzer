import requests
import sqlite3
import pandas as pd

def get_pokemon_data(pokemon_id: int):
    """Obtiene datos de un Pokémon de la API"""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f" Error al obtener Pokémon {pokemon_id}: {e}")
        return None

def extract_pokemon_info(api_data):
    """Extrae la información que necesitamos del JSON de la API"""
    if not api_data:
        return None
    
    # Stats que nos interesan
    stats = {stat['stat']['name']: stat['base_stat'] for stat in api_data['stats']}
    
    return {
        'id': api_data['id'],
        'name': api_data['name'],
        'type_1': api_data['types'][0]['type']['name'],
        'type_2': api_data['types'][1]['type']['name'] if len(api_data['types']) > 1 else None,
        'image_url': api_data['sprites']['front_default'],
        'hp': stats.get('hp', 0),
        'attack': stats.get('attack', 0),
        'defense': stats.get('defense', 0),
        'special_attack': stats.get('special-attack', 0),
        'special_defense': stats.get('special-defense', 0),
        'speed': stats.get('speed', 0)
    }

def main():
    print(" Iniciando extracción de los primeros 20 Pokémon...")
    
    conn = sqlite3.connect('pokemon.db')
    
    for pokemon_id in range(1, 21):
        print(f"📡 Obteniendo Pokémon {pokemon_id}...")
        raw_data = get_pokemon_data(pokemon_id)
        clean_data = extract_pokemon_info(raw_data)
        
        if clean_data:
            # Insertar en BD
            df = pd.DataFrame([clean_data])
            df.to_sql('pokemons', conn, if_exists='append', index=False)
            print(f" {clean_data['name'].capitalize()} guardado")
    
    conn.close()
    print("🎉 ¡Extracción completada!")

if __name__ == "__main__":
    main()