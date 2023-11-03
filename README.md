Proyecto de Extracción de Datos de Google Analytics
Este proyecto tiene como objetivo la extracción de datos de Google Analytics utilizando Python y la biblioteca Google Analytics Client. Permite a los usuarios obtener informes personalizados y exportarlos para su análisis.

Requisitos
Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

Python 3.x
Credenciales de Google Analytics en un archivo JSON.
Paquetes de Python requeridos. Puedes instalarlos usando pip:
pip install pandas
pip install google-auth
pip install google-auth-oauthlib
pip install google-auth-httplib2
Configuración
Clona el repositorio de Git en tu máquina:

git clone https://github.com/tu-usuario/tu-proyecto.git
Coloca tus credenciales de Google Analytics en un archivo JSON y especifica la ruta en credentials_path en el archivo main.py.
python

credentials_path = '/ruta/a/tu/credentials.json'
Define las métricas y dimensiones que deseas extraer en un objeto AnalyticsReport. Personaliza este objeto según tus necesidades:
python
report = AnalyticsReport(
    group='analytics',
    type='report',
    name='reportexd',
    view_id='216016069',
    start_date='2022-01-01',
    end_date='2022-12-31',
    metrics=[
        {'expression': 'ga:newUsers'},
        {'expression': 'ga:sessions'},
        # ... Agrega más métricas aquí ...
    ],
    dimensions=[
        {'name': 'ga:operatingSystem'},
        {'name': 'ga:year'},
        # ... Agrega más dimensiones aquí ...
    ]
)
Especifica la carpeta de respaldo donde se guardarán los informes exportados:
python
backup_folder = '/ruta/a/tu/carpeta-de-respaldo'
Uso
Para ejecutar la extracción de datos desde Google Analytics, ejecuta el siguiente comando:

python main.py
Esto ejecutará el proyecto y guardará el informe en la carpeta de respaldo que especificaste.

Visualización de Datos
Este proyecto incluye una vista de consola para mostrar mensajes de éxito. Puedes personalizar y extender esta vista según tus necesidades en el archivo console_view.py.

python
console_view = ConsoleView()
console_view.display_success()
Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de crear un Pull Request. Asegúrate de seguir las pautas de contribución.

Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Esperamos que este proyecto sea útil para tus necesidades de extracción de datos de Google Analytics! Si tienes alguna pregunta o inquietud, no dudes en contactarnos.




