from typing import List, Dict
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data: List[Dict]):
        manufacturing_date = min(
            data, key=lambda item: item.get('data_de_fabricacao'))
        expiration_date = min(
            data, key=lambda item: item.get('data_de_validade'))

        companies = []

        for item in data:
            companies.append(item["nome_da_empresa"])
        companies_list = Counter(companies).most_common()[0][0]

        return (

            f"""Data de fabricação mais antiga: {manufacturing_date['data_de_fabricacao']}
Data de validade mais próxima: {expiration_date['data_de_validade']}
Empresa com mais produtos: {companies_list}""")
