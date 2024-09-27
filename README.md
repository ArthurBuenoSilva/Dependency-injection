# Injeção de dependência

Este projeto implementa um sistema de cálculo de preços de produtos que utiliza injeção de dependência para 
aplicar diferentes estratégias de desconto e imposto. Ele também inclui um carrinho de compras que pode 
calcular o preço final de múltiplos produtos, além de gerar uma nota fiscal com os detalhes das compras.

## Funcionalidades

- Injeção de dependência para aplicar diferentes estratégias de desconto e imposto.
- Carrinho de compras que permite adicionar múltiplos produtos e calcular o valor total.
- Nota fiscal mostrando o preço final de cada produto e o total do carrinho.
- Suporte a diferentes tipos de produtos, cada um com suas próprias características de desconto e imposto.

## Pré-requisitos

- [Python 3.12.1](https://www.python.org/downloads/release/python-3121/) ou superior

## Instalação
Faça o clone do repositório:

```bash
git clone https://github.com/ArthurBuenoSilva/Dependency-injection.git
```

Acesse a pasta onde você clonou o repositório:

```bash
cd caminho/para/o/projeto
```

Crie um ambiente virtual(venv):

```bash
python -m venv venv
```

Acesse o ambiente virtual criado:

```bash
venv/Scripts/activate
```

## Uso
Execute o script main.py:

```bash
python main.py
```

No terminal deve aparecer o seguinte resultado:
```bash
------------ Invoice ------------
apple: $0.90
fridge: $122.48
monster_energy: $6.72
frozen_pizza: $9.70
Total: $139.80
---------------------------------
```

## Contribuições

Solicitações de pull requests são bem-vindas. Para mudanças importantes, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)