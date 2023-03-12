from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if path_file.endswith(".csv"):
            with open(path_file, mode="r") as file:
                csv_file = csv.DictReader(file)
                return [product for product in csv_file]
        raise ValueError("Arquivo inválido")
