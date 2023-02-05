from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


def test_decorar_relatorio():
    # data = [
    #     {
    #         "id": 9
    #         "nome_do_produto": "eucalyptus globulus",
    #         "nome_da_empresa": "Target Corporation",
    #         "data_de_fabricacao": "2020-09-06",
    #         "data_de_validade": "2024-05-21",
    #         "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
    #         "instrucoes_de_armazenamento": "instrucao 9",
    #     }
    # ]
    assert (
        ColoredReport(SimpleReport).generate(CsvImporter.import_data(
            "inventory_report/data/inventory.csv"))
        == "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2020-09-06\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-09-17\033[0m\n"
        + "\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mTarget Corporation\033[0m"
    )
