from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Panetone',
        'Errepi Foods',
        '01-01-2023',
        '01-10-2023',
        '64433725',
        'armazenar em local arejado'
        )
    assert product.id == 1
    assert product.nome_do_produto == 'Panetone'
    assert product.nome_da_empresa == 'Errepi Foods'
    assert product.data_de_fabricacao == '01-01-2023'
    assert product.data_de_validade == '01-10-2023'
    assert product.numero_de_serie == '64433725'
    assert product.instrucoes_de_armazenamento == 'armazenar em local arejado'
