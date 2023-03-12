from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_file):
        if path_file.endswith(".xml"):
            with open(path_file) as file:
                products_list = xmltodict.parse(file.read())
                return products_list["dataset"]["record"]
        raise ValueError("Arquivo inválido")
