from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(f: str):
        if f.endswith('.xml'):
            return Inventory.verify(f)
        else:
            raise ValueError('Arquivo inválido')
