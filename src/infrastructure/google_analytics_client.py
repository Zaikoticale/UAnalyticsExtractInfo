import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleAnalyticsClient:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)

    def fetch_report(self, report):
        analytics = build('analyticsreporting', 'v4', credentials=self.credentials)

        response = analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': report.view_id,
                        'dateRanges': [{'startDate': report.start_date, 'endDate': report.end_date}],
                        'metrics': report.metrics,
                        'dimensions': report.dimensions
                    }
                ]
            }
        ).execute()

        return pd.json_normalize(response['reports'][0]['data']['rows'])
