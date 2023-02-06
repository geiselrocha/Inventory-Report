import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) <= 2:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        path = sys.argv[1]
        type = sys.argv[2]
    if path.endswith('.csv'):
        sys.stdout.write(
            InventoryRefactor(CsvImporter).import_data(path, type))
    elif path.endswith('.json'):
        sys.stdout.write(
            InventoryRefactor(JsonImporter).import_data(path, type))
    elif path.endswith('.xml'):
        sys.stdout.write(
            InventoryRefactor(XmlImporter).import_data(path, type))
