from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path_file, report_type):
        if path_file.endswith(".csv"):
            with open(path_file, mode="r") as file:
                csv_file = csv.DictReader(file)
                products_list = [product for product in csv_file]
                if report_type == "simples":
                    simple_report = SimpleReport()
                    return simple_report.generate(products_list)
                if report_type == "completo":
                    complete_report = CompleteReport()
                    return complete_report.generate(products_list)

    # def generate_report(report_type, products_list):
    #     if report_type == "simples":
    #         simple_report = SimpleReport()
    #         return simple_report.generate(products_list)
    #     if report_type == "completo":
    #         complete_report = CompleteReport()
    #         return complete_report.generate(products_list)
