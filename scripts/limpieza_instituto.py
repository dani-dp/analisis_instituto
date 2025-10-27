import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from db_extraccion import extraer_tablas_a_df
from dotenv import load_dotenv

load_dotenv()

# ========================  FUNCIONES ===================================
def mostrar_informacion(df, nombre_df):
    """
    Muestra información básica de un DataFrame.
    """
    print(f"\n# Información del DataFrame: {nombre_df}")
    print(df.info())
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

def comprobar_valores_unicos(df, columna):
    """
    Muestra los valores únicos y su conteo en una columna específica de un DataFrame.
    """
    print(f"\n# Valores únicos en la columna '{columna}':")
    print(df[columna].value_counts())

def convertir_fechas(df):
    """
    Convierte columnas de fecha.
    Devuelve una COPIA del DataFrame con las columnas convertidas.
    """
    df_copy = df.copy() # 1. CREAMOS UNA COPIA EXPLÍCITA
    for col in df_copy.columns:
        if any(keyword in col.lower() for keyword in ['fecha', 'date', 'nacimiento', 'registro']):

            df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce', dayfirst=True)
    return df_copy # 3. Devolvemos la COPIA

# ========================  FUNCIÓN PRINCIPAL ===================================
def main():
    """
    Función principal. 
    """

    # ========================  CONEXIÓN SERVIDOR SQL ===================================

    # Adjudicamos variables del servidor: MySQL
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')

    # Connection
    connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
    engine = create_engine(connection_string)

    # Mensaje de ayuda para ver si la conexión ha sido correcta
    try:
        connection = engine.connect()
        print("Intentando conectar a la base de datos...")
        print("¡Conexión exitosa!")
        connection.close()
    except Exception as e:
        print(f"Error al conectar: {e}")
        sys.exit(1)

    # Usamos la función importada para obtener los DataFrames
    print("\nIniciando extracción de tablas desde la base de datos...")
    dfs_instituto = extraer_tablas_a_df(engine)

    # ========================  INFORMACIÓN DE DATOS ===================================
    # Información de los Dataframes
    print("\n--- Información de los DataFrames ---")
    for nombre_tabla, df in dfs_instituto.items():
        mostrar_informacion(df, nombre_tabla)
        print(df.head(2))

    # ========================  lIMPIEZA DE DATOS ===================================
    # Comprobación de valores únicos en columnas clave
    print("\n--- Comprobación de valores únicos en columnas clave ---")
    comprobar_valores_unicos(dfs_instituto['asignaturas'], 'nombre')
    comprobar_valores_unicos(dfs_instituto['asignaturas'], 'rama')      # Nos damos cuenta que hay datos duplicados

    # Limpieza de datos: Eliminación de duplicados en 'asignaturas'
    mapping = {
        'Ciencias': 'Ciencias y Tecnología',
        'Technología': 'Ciencias y Tecnología',
        'Technologia': 'Ciencias y Tecnología', 
        'Tecnología': 'Ciencias y Tecnología'    
    }

    # Limpiar espacios y aplicar mapeo
    df_asig = dfs_instituto['asignaturas'].copy() 
    df_asig.loc[:, 'rama'] = df_asig['rama'].str.strip().replace(mapping)
    dfs_instituto['asignaturas'] = df_asig

    # Conversión de columnas de fecha
    for nombre_tabla, df in dfs_instituto.items():
        dfs_instituto[nombre_tabla] = convertir_fechas(df) 
        print(f"Fechas convertidas en la tabla: {nombre_tabla}")
        print(dfs_instituto[nombre_tabla].select_dtypes(include='datetime').columns.tolist())

    # ========================  EXPORTACIÓN DE DATOS LIMPIOS ===================================
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) 

    # Directorio de salida para CSVs
    out_dir = os.path.join(project_root, "data_clean")

    # Creamos la carpeta si no existe y guardamos los CSVs
    os.makedirs(out_dir, exist_ok=True)
    for name, df in dfs_instituto.items():
        df.to_csv(os.path.join(out_dir, f"clean_{name}.csv"), index=False)
    print("Exportados CSV en:", out_dir)

# ========================  PUNTO DE ENTRADA ===================================
if __name__ == "__main__":
    main()