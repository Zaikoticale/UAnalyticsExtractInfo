# analytics_controller.py 

from src.usecases.analytics_usecase import AnalyticsUsecase

class AnalyticsController:

  def __init__(self, usecase: AnalyticsUsecase):  
    self.usecase = usecase

  def fetch_report(self, report, backup_folder):
    data = self.usecase.fetch_report(report)
    
def save_report_to_excel(self, report_df, report, backup_folder):
    workbook = openpyxl.Workbook()

    for dimension in report.dimensions[1:]:
        sheet_name = dimension['name'].replace('/', '_').replace(':', '_').replace('ga', '')
        workbook.create_sheet(sheet_name)

        metrics = report.metrics
        sheet = workbook[sheet_name]
        sheet.append(['Fecha'] + [metric['expression'] for metric in metrics])

        for index, row in report_df.iterrows():
            sheet.append([row['dimensions'][0]] + row['metrics'][0]['values'])

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    excel_file_path = os.path.join(backup_folder, 'Reporte.xlsx')
    workbook.save(excel_file_path)
    return data



