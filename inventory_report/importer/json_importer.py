from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(f: str):
        if f.endswith('.json'):
            return Inventory.verify(f)
        else:
            raise ValueError('Arquivo inválido')
