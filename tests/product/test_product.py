from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Product Name",
        "Company Name",
        "11/03/2023",
        "01/04/2024",
        "ANYTHING123",
        "Keep far from children and animals",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Product Name"
    assert product.nome_da_empresa == "Company Name"
    assert product.data_de_fabricacao == "11/03/2023"
    assert product.data_de_validade == "01/04/2024"
    assert product.numero_de_serie == "ANYTHING123"
    assert (
        product.instrucoes_de_armazenamento
        == "Keep far from children and animals"
    )
