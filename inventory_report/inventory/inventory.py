import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        inventory = Inventory.verify(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        return CompleteReport.generate(inventory)

    @staticmethod
    def verify(path: str):
        with open(path)as inventory:
            if path.endswith(".csv"):
                return list(csv.DictReader(inventory))
            if path.endswith(".json"):
                return json.load(inventory)
            xml = xmltodict.parse(inventory.read())
            data = xml["dataset"]["record"]
            return list(dict(i) for i in data)
