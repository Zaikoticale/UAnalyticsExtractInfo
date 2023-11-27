import os
import openpyxl
import pandas as pd
from src.usecases.analytics_usecase import AnalyticsUsecase
import csv

class AnalyticsController:

    def __init__(self, usecase: AnalyticsUsecase):
        self.usecase = usecase

    def fetch_report(self, report):
        data = self.usecase.fetch_report(report)
        return data

    def save_report_to_csv(self, report_df, report, backup_folder: str):
        workbook = openpyxl.Workbook()
        default_sheet = workbook.active
        workbook.remove(default_sheet)

        if len(report.dimensions) > 1:
            second_dimension_name = report.dimensions[1]['name'].replace('/', '_').replace(':', '_').replace('ga', '').replace('_','')
        else:
            second_dimension_name = None

        sheet = workbook.create_sheet(second_dimension_name)

        metrics = report.metrics

        sheet.append(['pagina'] + [metric['expression'].replace('ga:', '') for metric in metrics])

        for i, row in report_df.iterrows():
            dimensions = row['dimensions']
            metrics_values = row['metrics'][0]['values']
            if second_dimension_name == 'date':
                if 'Unnamed: 11' in row['dimensions']:
                    row['dimensions'][row['dimensions'].index(' ')] = 'date'
                sheet.append([dimensions[0].replace('ga:', '')] + [value.replace('ga:', '') for value in metrics_values] + [dimensions[-1].replace('ga:', '')])
            else:
                sheet.append([dimensions[0].replace('ga:', '')] + [value.replace('ga:', '') for value in metrics_values])

        sheet.auto_filter.ref = sheet.dimensions

        group_folder = os.path.join(backup_folder, report.group)
        type_folder = os.path.join(group_folder, report.type)


        if not os.path.exists(group_folder):
            os.makedirs(group_folder)

        if not os.path.exists(type_folder):
            os.makedirs(type_folder)

        csv_file_path = os.path.join(type_folder, f"{report.name}.csv")

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['pagina'] + [metric['expression'].replace('ga:', '') for metric in metrics])

            for i, row in report_df.iterrows():
                dimensions = row['dimensions']
                metrics_values = row['metrics'][0]['values']
                if second_dimension_name == 'date':
                    if 'Unnamed: 11' in row['dimensions']:
                        row['dimensions'][row['dimensions'].index(' ')] = 'date'
                    writer.writerow([dimensions[0].replace('ga:', '')] + [value.replace('ga:', '') for value in metrics_values] + [dimensions[-1].replace('ga:', '')])
                else:
                    writer.writerow([dimensions[0].replace('ga:', '')] + [value.replace('ga:', '') for value in metrics_values])

        return

