from src.domain.models import AnalyticsReport
from src.usecases.analytics_usecase import AnalyticsUsecase
from src.controller.analytics_controller import AnalyticsController
from src.infrastructure.google_analytics_client import GoogleAnalyticsClient
from src.view.console_view import ConsoleView
from datetime import datetime, timedelta
import os

current_directory = os.getcwd()
backup_folder_relative = 'backup/Usuarios'

credentials_path = os.path.join(current_directory, 'src/controller/credentials.json')
analytics_client = GoogleAnalyticsClient(credentials_path)
analytics_usecase = AnalyticsUsecase(analytics_client)
analytics_controller = AnalyticsController(analytics_usecase)
backup_folder = os.path.join(current_directory, backup_folder_relative)

start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 6, 30)

metrics = [
    # {'expression': 'ga:timeOnPage'},
    # {'expression': 'ga:totalEvents'},
    # {'expression': 'ga:uniqueEvents'},
    # {'expression': 'ga:sessionsWithEvent'}

    {'expression': 'ga:users'},
    {'expression': 'ga:newUsers'},
    {'expression': 'ga:sessions'},
    {'expression': 'ga:bounceRate'},
    {'expression': 'ga:sessionDuration'},
    {'expression': 'ga:avgSessionDuration'},
    {'expression': 'ga:pageviews'},
    {'expression': 'ga:pageviewsPerSession'},
    {'expression': 'ga:avgTimeOnPage'},
    {'expression': 'ga:sessionsPerUser'},
]
dimensions = [
    {'name': 'ga:City'},
    {'name': 'ga:date'},
]
current_date = start_date
num_reports = (end_date - start_date).days + 1
report_num = 0
# simulate_error_after_reports = 2
max_retries = 3
retry_count = 0

while current_date <= end_date:
    try:
        group = "RedSocial"
        report_type = 'usuarios'
        year = current_date.strftime('%Y')
        month = current_date.strftime('%B').capitalize()
        folder_path = os.path.join(backup_folder, group, report_type, year, month)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        date_str = current_date.strftime('%Y-%m-%d')  
    
        report = AnalyticsReport(
            group=group,
            type=report_type,
            name=f'{report_type} por {group} ({date_str})', 
            view_id='77379827',
            start_date=date_str,
            end_date=date_str,
            pageSize=1000000000,
            metrics=metrics,
            dimensions=dimensions,
            #orderBys=[{'fieldName': 'ga:pageviews', 'sortOrder': 'DESCENDING'}]
        )

        report_num += 1
        progress = report_num / num_reports * 100
        print(f"\033[1m\033[35mProgreso: {progress:.2f}% - Reporte {report_num} de {num_reports}\033[0m")

        report_data = analytics_controller.fetch_report(report)

        analytics_controller.save_report_to_csv(report_data, report, folder_path)
        print(report_data)

        current_date += timedelta(days=1)

        total_time = 0

        # Simular un error después de procesar 2 informes
        # if report_num == simulate_error_after_reports:
        #     raise RuntimeError("Este es un error simulado para propósitos de prueba.")

    except Exception as e:
        retry_count += 1
        if retry_count <= max_retries:
            print(f"Error: {e}. Retrying... ({retry_count}/{max_retries})")
            print(f"API Response: {report_num}")
            print(f"Exception details: {str(e)}")
            continue
        else:
            print(f"Max retries reached. Exiting loop.")
            break



console_view = ConsoleView()
if analytics_controller:
    console_view.display_succes()

else:
    console_view.display_error('error')
