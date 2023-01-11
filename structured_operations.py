#calculando payoffs e lucro atual em algumas estruturas de opcoes


def lucro_jade_lizard(preco_ativo, preco_opcao_compra, preco_opcao_venda1, preco_opcao_venda2, preco_opcao_compra_alto):
    lucro = preco_opcao_compra - preco_opcao_venda1 - preco_opcao_venda2 + preco_opcao_compra_alto - preco_ativo
    return lucro

def lucro_venda_coberta(preco_ativo, preco_opcao_compra, preco_opcao_venda):
    lucro = preco_opcao_venda - preco_opcao_compra - preco_ativo
    return lucro

def lucro_seagull(preco_ativo, preco_opcao_compra, preco_opcao_venda, preco_opcao_compra_alto):
    lucro = preco_opcao_compra - preco_opcao_venda - preco_opcao_compra_alto + 2*preco_ativo
    return lucro

def lucro_fence(preco_ativo, preco_opcao_compra_baixo, preco_opcao_venda_baixo, preco_opcao_compra_alto, preco_opcao_venda_alto):
    lucro = (preco_opcao_compra_alto + preco_opcao_venda_baixo) - (preco_opcao_compra_baixo + preco_opcao_venda_alto)
    return lucro

