import pandas as pd

archivo_xlsx = '/Users/r360sas/Sites/AnalyticsBackup/backup/Comportamiento/pagina/Usuarios/2021/May/pagina/Usuarios/Usuarios por pagina (2021-05-04).xlsx'

# Lee todas las hojas del archivo Excel en un diccionario de DataFrames
dataframes = pd.read_excel(archivo_xlsx, sheet_name=None, engine='openpyxl')

# Itera sobre las hojas y muestra cada DataFrame
for sheet_name, df in dataframes.items():
    print(f"\nDataFrame de la hoja: {sheet_name}")
    print(df)
