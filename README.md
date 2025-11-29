📦 SISTEMA DE CONTROLE DE ESTOQUE
===========================================================================================================
Um sistema simples e eficiente de controle de estoque.
O sistema permite cadastrar produtos, listar, movimentar estoque (entrada e saída) e salvar os dados em arquivo.
===========================================================================================================
🧩 Funcionalidades
✔️ Cadastro de produtos

- Nome

- Código

- Quantidade

- Preço

- Categoria

✔️ Listagem dos produtos

- Ordenação e formatação organizada

- Exibição de todos os dados do produto

✔️ Movimentação de estoque

- Entrada: adiciona quantidade

- Saída: remove quantidade com bloqueio de valores inválidos

- Registro atualizado automaticamente

✔️ Armazenamento em arquivo

- Salva produtos em .txt (ou .csv, se você quiser adaptar)

- Lê ao iniciar o programa
================================================================================================
🛠️ Tecnologias Utilizadas

Python 3+

- Estrutura modular e organizada

- Leitura e escrita em arquivos

- Funções de manipulação de listas e dicionários

▶️ Como Usar o Sistema
🔹 1. Execute o arquivo principal
python estoque.py

📝 Exemplo de Movimentação de Estoque

O sistema permite:

Entrada de estoque:

- Você escolhe o produto

- Informa quantos itens estão chegando

- O sistema soma com o valor atual

Saída de estoque:

- O sistema impede saída maior que o estoque

- Atualiza e salva automaticamente

📦 Arquivo de Dados

Os produtos são salvos automaticamente no arquivo:

- produtos.txt

- Cada linha representa um produto com seus dados separados por ;.


🚀 Futuras Melhorias (opcional)

- Exportar dados para .csv

- Interface gráfica (Tkinter ou PyQt)

- API REST para controle remoto

- Dashboard com gráficos
