from src.domain.models import AnalyticsReport
from src.usecases.analytics_usecase import AnalyticsUsecase
from src.controller.analytics_controller import AnalyticsController
from src.infrastructure.google_analytics_client import GoogleAnalyticsClient
from src.view.console_view import ConsoleView

credentials_path = '/Users/r360sas/Sites/AnalyticsBackup/src/controller/credentials.json'
analytics_client = GoogleAnalyticsClient(credentials_path)

# Crear el caso de uso y pasar el cliente de Google Analytics
analytics_usecase = AnalyticsUsecase(analytics_client)
analytics_controller = AnalyticsController(analytics_usecase)

report = AnalyticsReport(
    group='analytics',
    type='report',
    name='reporte',
    view_id='216016069',
    start_date='2018-01-01',
    end_date='2023-07-31',
    metrics=[
        {'expression': 'ga:newUsers'},
        {'expression': 'ga:sessions'},
        {'expression': 'ga:sessionDuration'},
        {'expression': 'ga:avgSessionDuration'},
        {'expression': 'ga:sessionsPerUser'},
        {'expression': 'ga:bounceRate'},
        {'expression': 'ga:avgTimeOnPage'},
        {'expression': 'ga:sessions'},
        {'expression': 'ga:users'},
        {'expression': 'ga:pageviews'},
    ],
    dimensions=[
        {'name': 'ga:year'},
        {'name': 'ga:operatingSystem'},
        {'name': 'ga:yearMonth'},
        {'name': 'ga:date'},


    ]
)

# Obtener el informe y guardar los datos en una variable
report_data = analytics_controller.fetch_report(report)

# Definir la carpeta de respaldo
backup_folder = '/Users/r360sas/Sites/AnalyticsBackup/backup'

# Guardar los datos del informe en un archivo de Excel en la carpeta de respaldo
analytics_controller.save_report_to_excel(report_data, report, backup_folder)

console_view = ConsoleView()
if analytics_controller:
    console_view.display_succes()
else:
    console_view.display_error()
