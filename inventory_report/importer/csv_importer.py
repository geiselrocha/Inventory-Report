from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(f: str):
        if f.endswith('.csv'):
            return Inventory.verify(f)
        else:
            raise ValueError('Arquivo inválido')
