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
                        'dimensions': report.dimensions,
                        'pageSize': report.pageSize,
                        'orderBys': report.orderBys
                    }
                ]
            }
        ).execute()

        try:
            return pd.json_normalize(response['reports'][0]['data']['rows'])
        except KeyError as e:
            print(f"KeyError: {e}. 'rows' not found in the API response.")
            # Puedes decidir cómo manejar esta situación, ya sea lanzando una excepción,
            # retornando un valor predeterminado, o tomando alguna otra acción.
            # Aquí, por ejemplo, podrías retornar un DataFrame vacío.
        return pd.DataFrame()
