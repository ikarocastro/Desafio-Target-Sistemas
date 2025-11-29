import json
import random
from datetime import datetime

#=============================================
# REGRAS PARA CADA VENDA:
 # Vendas abaixo de R$100,00 não gera comissão
 # Vendas abaixo de R$500,00 gera 1% de comissão
 # A partir de R$500,00 gera 5% de comissão
#=============================================


# ============================================
#  DESAFIO 1 – Cálculo de Comissão por Vendedor
# ============================================

vendas_json = {
    "vendas": [
        {"vendedor": "João Silva", "valor": 1200.50},
        {"vendedor": "João Silva", "valor": 950.75},
        {"vendedor": "João Silva", "valor": 1800.00},
        {"vendedor": "João Silva", "valor": 1400.30},
        {"vendedor": "João Silva", "valor": 1100.90},
        {"vendedor": "João Silva", "valor": 1550.00},
        {"vendedor": "João Silva", "valor": 1700.80},
        {"vendedor": "João Silva", "valor": 250.30},
        {"vendedor": "João Silva", "valor": 480.75},
        {"vendedor": "João Silva", "valor": 320.40},

        {"vendedor": "Maria Souza", "valor": 2100.40},
        {"vendedor": "Maria Souza", "valor": 1350.60},
        {"vendedor": "Maria Souza", "valor": 950.20},
        {"vendedor": "Maria Souza", "valor": 1600.75},
        {"vendedor": "Maria Souza", "valor": 1750.00},
        {"vendedor": "Maria Souza", "valor": 1450.90},
        {"vendedor": "Maria Souza", "valor": 400.50},
        {"vendedor": "Maria Souza", "valor": 180.20},
        {"vendedor": "Maria Souza", "valor": 90.75},

        {"vendedor": "Carlos Oliveira", "valor": 800.50},
        {"vendedor": "Carlos Oliveira", "valor": 1200.00},
        {"vendedor": "Carlos Oliveira", "valor": 1950.30},
        {"vendedor": "Carlos Oliveira", "valor": 1750.80},
        {"vendedor": "Carlos Oliveira", "valor": 1300.60},
        {"vendedor": "Carlos Oliveira", "valor": 300.40},
        {"vendedor": "Carlos Oliveira", "valor": 500.00},
        {"vendedor": "Carlos Oliveira", "valor": 125.75},

        {"vendedor": "Ana Lima", "valor": 1000.00},
        {"vendedor": "Ana Lima", "valor": 1100.50},
        {"vendedor": "Ana Lima", "valor": 1250.75},
        {"vendedor": "Ana Lima", "valor": 1400.20},
        {"vendedor": "Ana Lima", "valor": 1550.90},
        {"vendedor": "Ana Lima", "valor": 1650.00},
        {"vendedor": "Ana Lima", "valor": 75.30},
        {"vendedor": "Ana Lima", "valor": 420.90},
        {"vendedor": "Ana Lima", "valor": 315.40}
    ]
}

# Função para calcular a comissão 
def calcular_comissao(valor):
    """Calcula a comissão conforme as regras estabelecidas."""
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05

    # Função principal do DESAFIO 1 
def desafio1():
    """Calcula e exibe a comissão total de cada vendedor."""
    comissoes = {}

    for venda in vendas_json["vendas"]:
        vendedor = venda["vendedor"]
        valor = venda["valor"]
        comissao = calcular_comissao(valor)

        if vendedor not in comissoes:
            comissoes[vendedor] = 0

        comissoes[vendedor] += comissao

    print("\n===== COMISSÕES POR VENDEDOR =====")
    for vendedor, total in comissoes.items():
        print(f"{vendedor}: R${total:.2f}")


# ============================================
#  DESAFIO 2 – Movimentação de Estoque
# ============================================

estoque = [
    {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
    {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75},
    {"codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200},
    {"codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320},
    {"codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90}
]

    # Função para buscar produto pelo código
def buscar_produto(codigo):
    """Retorna o produto pelo código informado."""
    for p in estoque:
        if p["codigoProduto"] == codigo:
            return p
    return None


def movimentar_estoque():
    """Registra entradas e saídas de estoque com ID único."""
    try:
        codigo = int(input("Digite o código do produto: "))
        produto = buscar_produto(codigo)

        if not produto:
            print("Produto não encontrado!\n")
            return

        quantidade = int(input("Digite a quantidade (ex: 10 ou -5): "))
        descricao = input("Descrição da movimentação: ")

        # ID único da movimentação
        mov_id = random.randint(10000, 99999)

        # Atualiza estoque
        produto["estoque"] += quantidade

        print("\n==== MOVIMENTAÇÃO REGISTRADA ====")
        print(f"ID: {mov_id}")
        print(f"Produto: {produto['descricaoProduto']}")
        print(f"Movimentação: {descricao}")
        print(f"Quantidade: {quantidade}")
        print(f"Estoque final: {produto['estoque']}")
        print("================================\n")

    except ValueError:
        print("Erro: Digite valores válidos!\n")


# ============================================
#  DESAFIO 3 – Cálculo de Juros Diário
# ============================================

def calcular_juros():
    """Calcula o valor de juros por atraso."""
    try:
        valor = float(input("Digite o valor original: R$"))
        data_str = input("Digite a data de vencimento (dd/mm/aaaa): ")

        data_venc = datetime.strptime(data_str, "%d/%m/%Y")
        hoje = datetime.now()

        dias_atraso = (hoje - data_venc).days

        if dias_atraso <= 0:
            print("\nPagamento em dia! Sem juros.\n")
            return

        multa = valor * 0.025 * dias_atraso
        total = valor + multa

        print("\n===== CÁLCULO DE JUROS =====")
        print(f"Dias de atraso: {dias_atraso}")
        print(f"Multa acumulada: R${multa:.2f}")
        print(f"Total a pagar: R${total:.2f}")
        print("=============================\n")

    except ValueError:
        print("Data inválida!\n")


# ============================================
#  MENU PRINCIPAL
# ============================================

def menu():
    while True:
        print("=========== MENU PRINCIPAL ===========")
        print("1 - Cálculo de comissão (Desafio 1)")
        print("2 - Movimentação de estoque (Desafio 2)")
        print("3 - Cálculo de juros por atraso (Desafio 3)")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            desafio1()
        elif opcao == "2":
            movimentar_estoque()
        elif opcao == "3":
            calcular_juros()
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!\n")


# Início do programa
if __name__ == "__main__":
    menu()


"""
===========================================================
 TUTORIAL DE COMO UTILIZAR A FUNÇÃO DE MOVIMENTAÇÃO DE ESTOQUE
===========================================================

A função "movimentar_estoque()" que criei permite registrar entradas e 
saídas de produtos do depósito, atualizando automaticamente 
a quantidade armazenada.

Como isso irá funcionar na prática? 
Detalhei abaixo um passo a passo simples para você compreender o que fiz.

------------------------------------------
1) COMO ABRIR O MÓDULO DE MOVIMENTAÇÃO?
------------------------------------------

Ao executar o programa principal, escolha no menu:

    2 - Movimentação de estoque (Desafio 2)

Isso iniciará o processo de registrar uma movimentação.

------------------------------------------
2) PASSO A PASSO PARA REALIZAR A MOVIMENTAÇÃO
------------------------------------------

O sistema solicitará três informações:

------------------------------------------
PASSO 1) DIGITE O CÓDIGO DO PRODUTO
------------------------------------------

Os códigos disponíveis são:

    101 - Caneta Azul
    102 - Caderno Universitário
    103 - Borracha Branca
    104 - Lápis Preto HB
    105 - Marcador de Texto Amarelo

Exemplo:
    Digite o código do produto: 101

------------------------------------------
PASSO 2) INFORME A QUANTIDADE
------------------------------------------

Use números positivos para entradas (adicionar estoque)
Use números negativos para saídas (retirar estoque)

Exemplos:
    Digite a quantidade: 20      -> Entrada de 20 unidades
    Digite a quantidade: -5      -> Saída de 5 unidades

------------------------------------------
PASSO 3)  INFORME A DESCRIÇÃO DA MOVIMENTAÇÃO
------------------------------------------

Aqui você descreve o motivo da movimentação.

Exemplos:

    "Entrada de fornecedor"
    "Venda realizada"
    "Ajuste de inventário"

------------------------------------------
PASSO 4) O SISTEMA GERA AUTOMATICAMENTE:
------------------------------------------

Após confirmar os dados, o programa exibe:

    - ID único da movimentação
    - Nome do produto
    - Tipo de movimentação realizada
    - Quantidade movimentada
    - Estoque final atualizado do produto

Exemplo de saída:

    ==== MOVIMENTAÇÃO REGISTRADA ====
    ID: 48291
    Produto: Caneta Azul
    Movimentação: Venda realizada
    Quantidade: -10
    Estoque final: 140
    =================================


------------------------------------------
PASSO 5) OBSERVAÇÕES IMPORTANTES
------------------------------------------

✓ Entradas usam número POSITIVO  
✓ Saídas usam número NEGATIVO  
✓ Estoque é atualizado automaticamente  
✓ O ID da movimentação é gerado pelo sistema  
✓ Se o código informado não existir, o sistema avisa  

------------------------------------------
PASSO 6) FUNÇÃO UTILIZADA PARA A MOVIMENTAÇÃO
------------------------------------------

Abaixo está o trecho-chave do código que registra a operação:

    produto["estoque"] += quantidade

Isso significa que:
    - Se quantidade for positiva → soma ao estoque
    - Se quantidade for negativa → subtrai do estoque

===========================================================
 Fim do tutorial de uso da movimentação de estoque
===========================================================

Criei esse tutorial para facilitar o entendimento de como utilizar a função e para que o codigo seja mais acessível, facilitando futuras manutenções.

"""
