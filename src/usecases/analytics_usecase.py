import os
import openpyxl

class AnalyticsUsecase:
    def __init__(self, analytics_client):
        self.analytics_client = analytics_client

    def fetch_report(self, report, backup_folder):
        report_df = self.analytics_client.fetch_report(report)
        