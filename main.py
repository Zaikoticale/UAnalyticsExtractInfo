from src.domain.models import AnalyticsReport
from src.usecases.analytics_usecase import AnalyticsUsecase
from src.controller.analytics_controller import AnalyticsController
from src.infrastructure.google_analytics_client import GoogleAnalyticsClient
from src.view.console_view import ConsoleView
from datetime import datetime

credentials_path = 'src/controller/credentials.json'
analytics_client = GoogleAnalyticsClient(credentials_path)

# Crear el caso de uso y pasar el cliente de Google Analytics

analytics_usecase = AnalyticsUsecase(analytics_client)
analytics_controller = AnalyticsController(analytics_usecase)
backup_folder = 'backup/Hora'

group = 'mes'  
type = 'Usuario'
report = AnalyticsReport(
    group=group,
    type=type,
    name=f'{type} por {group}',
    view_id='77379827',
    start_date='2018-01-01',
    end_date='2023-06-30',
    pageSize=1000000000,
    metrics=[
        # <--------- Comportamiento ----------->
        # {'expression': 'ga:timeOnPage'},
        # {'expression': 'ga:totalEvents'},
        # {'expression': 'ga:uniqueEvents'},
        # {'expression': 'ga:sessionsWithEvent'}

        # <------------ Usuarios ---------------->
        {'expression': 'ga:sessionDuration'},
        {'expression': 'ga:avgSessionDuration'},
        {'expression': 'ga:sessionsPerUser'},
        {'expression': 'ga:pageviewsPerSession'},
        {'expression': 'ga:bounceRate'},
        {'expression': 'ga:avgTimeOnPage'},
        {'expression': 'ga:sessions'},
        {'expression': 'ga:users'},
        {'expression': 'ga:newUsers'},
        {'expression': 'ga:pageviews'}
        ],
    dimensions=[
    #{'name': 'ga:date'}
    {'name': 'ga:yearMonth'},
    ]
)


report_data = analytics_controller.fetch_report(report)
analytics_controller.save_report_to_csv(report_data, report, backup_folder)

console_view = ConsoleView()
if analytics_controller:
    console_view.display_succes()
else:
    console_view.display_error('error')
