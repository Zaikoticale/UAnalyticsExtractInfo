from src.domain.models import AnalyticsReport
from src.usecases.analytics_usecase import AnalyticsUsecase
from src.controller.analytics_controller import AnalyticsController
from src.infrastructure.google_analytics_client import GoogleAnalyticsClient
from src.view.console_view import ConsoleView


credentials_path = '/Users/r360sas/Sites/AnalyticsBackup/src/controller/credentials.json'
analytics_client = GoogleAnalyticsClient(credentials_path)
analytics_usecase = AnalyticsUsecase(analytics_client)

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
        {'name': 'ga:operatingSystem'},
        {'name': 'ga:year'},
    ]
)
backup_folder = '/Users/r360sas/Sites/AnalyticsBackup/backup'
report_df = analytics_usecase.fetch_report(report, backup_folder)

analytics_usecase.fetch_report(report, backup_folder)

console_view = ConsoleView()
console_view.display_succes()
