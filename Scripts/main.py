def mostrar_menu():
    print("\n" + "="*50)
    print("        POKEMON STATS ANALYZER")
    print("="*50)
    print("1. Extraer datos de la API (primeros 20 Pokémon)")
    print("2. Ver datos guardados en la base de datos")
    print("3. Generar análisis exploratorio (EDA)")
    print("4. Exportar datos a CSV")
    print("5. Salir")
    print("="*50)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n Ejecutando extracción de datos...")
            from poke_api import main as extraer_datos
            extraer_datos()
            
        elif opcion == "2":
            print("\n Creando/verificando base de datos...")
            from dbManager import create_database, test_connection
            create_database()
            test_connection()
            
        elif opcion == "3":
            print("\n Generando análisis exploratorio...")
            print("(Esta función se implementará después)")
            
        elif opcion == "4":
            print("\n Exportando datos a CSV...")
            print("(Esta función se implementará después)")
            
        elif opcion == "5":
            print("\n ¡Hasta luego!")
            break
            
        else:
            print("\n Opción inválida. Por favor elige 1-5.")

if __name__ == "__main__":
    main()