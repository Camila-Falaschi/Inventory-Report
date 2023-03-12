from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, path_file):
        raise NotImplementedError("This method hasn't been implemented")
