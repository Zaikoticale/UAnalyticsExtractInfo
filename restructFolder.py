import os
import shutil

def mover_contenido_y_eliminar(year_folder, target_folder):
    # Iterar sobre las carpetas de año
    for year in os.listdir(year_folder):
        year_path = os.path.join(year_folder, year)
        
        # Verificar si la carpeta de año es un directorio
        if os.path.isdir(year_path):
            print(f"Procesando año: {year}")
            # Iterar sobre las carpetas de mes dentro de la carpeta de año
            for month in os.listdir(year_path):
                month_path = os.path.join(year_path, month)
                
                # Verificar si la carpeta de mes es un directorio
                if os.path.isdir(month_path):
                    print(f"  Procesando mes: {month}")
                    Medio_path = os.path.join(month_path, "Medio")
                    usuarios_path = os.path.join(Medio_path, target_folder)
                    
                    # Verificar si la carpeta "usuarios" existe
                    if os.path.exists(usuarios_path):
                        try:
                            # Mover el contenido de "usuarios" a la carpeta de mes
                            for item in os.listdir(usuarios_path):
                                source_path = os.path.join(usuarios_path, item)
                                destination_path = os.path.join(month_path, item)
                                shutil.move(source_path, destination_path)
                                print(f"    Moviendo: {source_path} a {destination_path}")
                            
                            # Eliminar la carpeta "usuarios"
                            shutil.rmtree(usuarios_path)
                            print(f"    Carpeta 'usuarios' eliminada: {usuarios_path}")
                            
                            shutil.rmtree(Medio_path)
                            print(f"    Carpeta 'Medio' eliminada: {Medio_path}")
                        except OSError as e:
                            print(f"    Error al procesar 'usuarios' en {usuarios_path}: {e}")
                    else:
                        print(f"    Carpeta 'usuarios' no encontrada en {Medio_path}")

# Especifica la carpeta principal que contiene las carpetas de año
carpeta_principal = "/Users/r360sas/Sites/AnalyticsBackup/backup/Adquisicion/Medio/usuarios"
# Llama a la función para realizar la operación
mover_contenido_y_eliminar(carpeta_principal, "usuarios")
