from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: List[Dict]):
        result = SimpleReport.generate(data)

        companies = []

        for item in data:
            companies.append(item["nome_da_empresa"])
        companies_list = list(Counter(companies).items())
        result = f"""{result}Produtos estocados por empresa:"""

        for item in companies_list:
            result = f"""{result}- {item[0]}: {str(item[1])}"""
        return result
