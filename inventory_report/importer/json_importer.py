from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if path_file.endswith(".json"):
            with open(path_file) as file:
                return json.load(file)
        raise ValueError("Arquivo inválido")
