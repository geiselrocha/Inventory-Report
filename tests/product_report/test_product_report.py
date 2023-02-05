from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        'Chocolate',
        'Errepi Foods',
        '2023-01-01',
        '2023-12-12',
        '19101909',
        'em local arejado',
    )

    assert product.__repr__() == (
        'O produto Chocolate'
        ' fabricado em 2023-01-01'
        ' por Errepi Foods com validade'
        ' até 2023-12-12'
        ' precisa ser armazenado em local arejado.'
    )
