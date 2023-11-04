# analytics_controller.py 
import os
import openpyxl

from src.usecases.analytics_usecase import AnalyticsUsecase

class AnalyticsController:

  def __init__(self, usecase: AnalyticsUsecase):  
    self.usecase = usecase

  def fetch_report(self, report):
    data = self.usecase.fetch_report(report)
    return data
    
  def save_report_to_excel(self, report_df, report, backup_folder):
    workbook = openpyxl.Workbook()

    for dimension in report.dimensions[1:]:
        sheet_name = dimension['name'].replace('/', '_').replace(':', '_').replace('ga', '').replace('_','')
        workbook.create_sheet(sheet_name)

        metrics = report.metrics
        sheet = workbook[sheet_name]
        sheet.append(['Fecha', 'Dimensión'] + [metric['expression'] for metric in metrics])

        for _, row in report_df.iterrows():
            sheet.append([row['dimensions'][0]] + row['metrics'][0]['values'])

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    excel_file_path = os.path.join(backup_folder, 'Reporte.xlsx')
    workbook.save(excel_file_path)
    return
