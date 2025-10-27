import pandas as pd

def extraer_tablas_a_df(engine):
    """
    Extrae todas las tablas de la base de datos conectada y las devuelve como un
    diccionario de DataFrames de pandas.
    """

    dataframes = {}
    try:
        with engine.connect() as connection:
            from sqlalchemy import inspect
            inspector = inspect(engine)
            lista_tablas = inspector.get_table_names()

        print(f"Tablas encontradaS: {lista_tablas}")

        for tabla in lista_tablas:
            query = f"SELECT * FROM {tabla}"
            df = pd.read_sql(query, engine)
            dataframes[tabla.lower()] = df     # Guardamos el DataFrame con el nombre de la tabla en minúsculas para evitar errores
            print(f"Extracción de la tabla '{tabla}' completada con éxito.")
        
        return dataframes
    
    except Exception as e:
        print(f"Ocurrió un error durante la extraccion de las tablas: {e}")
        return None