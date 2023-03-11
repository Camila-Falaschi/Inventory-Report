from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, path_file, report_type):
        if path_file.endswith(".csv"):
            with open(path_file, mode="r") as file:
                csv_file = csv.DictReader(file)
                products_list = [product for product in csv_file]
                return cls.generate_report(report_type, products_list)
        if path_file.endswith(".json"):
            with open(path_file) as file:
                products_list = json.load(file)
                return cls.generate_report(report_type, products_list)

    def generate_report(report_type, products_list):
        if report_type == "simples":
            simple_report = SimpleReport()
            return simple_report.generate(products_list)
        if report_type == "completo":
            complete_report = CompleteReport()
            return complete_report.generate(products_list)
