import os
import pandas as pd
import re

nombre_archivo_salida = "/Users/r360sas/Sites/AnalyticsBackup/backup/Adquisicion/canalPredeterminado/usuarios/canalPredeterminado.csv"
carpeta_principal = "/Users/r360sas/Sites/AnalyticsBackup/backup/Adquisicion/canalPredeterminado/usuarios"

def combinar_csv(carpeta_principal, nombre_archivo_salida):
    dataframes = []

    for root, dirs, files in os.walk(carpeta_principal):
        for archivo in files:
            if archivo.endswith('.csv'):
                ruta_archivo = os.path.join(root, archivo)

                # Check if the file is empty
                if os.path.getsize(ruta_archivo) > 0:
                    mes_match = re.search(r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b)', archivo)
                    mes = mes_match.group(1) if mes_match else None

                    try:
                        # Leer el archivo CSV sin encabezado y con un nombre para la última columna
                        df = pd.read_csv(ruta_archivo, header=None, names=list(range(11))+['Unnamed'], dtype=str)

                        # Agregar el DataFrame al listado de DataFrames
                        dataframes.append(df)

                        # Imprimir información para la primera fila
                        for columna in df.columns:
                            print(f"{columna}: {df[columna].iloc[0]}")

                    except pd.errors.EmptyDataError:
                        print(f"Empty DataFrame: {ruta_archivo}")
                    except pd.errors.ParserError:
                        print(f"Error parsing file: {ruta_archivo}")

                else:
                    print(f"Skipping empty file: {ruta_archivo}")

    if dataframes:
        # Concatenar todos los DataFrames en uno solo
        df_final = pd.concat(dataframes, ignore_index=True)

        # Guardar el DataFrame combinado en un archivo CSV
        df_final.to_csv(nombre_archivo_salida, index=False)

        print(df_final.shape)
        print(f"Archivos CSV combinados y guardados en {nombre_archivo_salida}")
    else:
        print("No se encontraron archivos CSV no vacíos.")

# Verificar si el directorio de salida existe; si no, crearlo
if not os.path.exists(os.path.dirname(nombre_archivo_salida)):
    os.makedirs(os.path.dirname(nombre_archivo_salida))

# Llamar a la función para combinar archivos CSV
combinar_csv(carpeta_principal, nombre_archivo_salida)
