# rm557943 - Enzo Gaião Real
# definição de função
def verifica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        print('Insira apenas números')
        numero = input(msg)
    numero = int(numero)
    return numero


def forca_escolhe(msg, disponiveis, erro):
    escolha = input(msg)
    while escolha not in disponiveis:
        print(erro, disponiveis)
        escolha = input(msg)
        continue
    return escolha


def index(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i


def printa_essa_porra(vinhos, precos, quantidade):
    for i in range(len(vinhos)):
        print(f'{vinhos[i]}: R${precos[i]:.2f} -- {qtd[i]} Quantidade no Carrinho')


# Código pra valer

endereco = input('Qual o seu endereço? (Rua, N°)\n --> ')
idade = verifica_numero('Qual seu ano de nascimento?\n --> ')
ano_atual = 2024

if ano_atual - idade < 18:
    print('É proibida a venda de bebidas alcoólicas para menores de idade')
else:
    print('Seja bem vindo a Vinheria Agnello!')
    # listas
    vinhos = ['branco', 'tinto', 'rosé']
    precos = [59.9, 79.9, 63.9]
    qtd = [0, 0, 0]
    aux = 0
    preco = 0
    # Facilita caso o limite para frete gratis mude
    frete_gratis = 500
    frete = 30
    quer_ou_n_quer = ['sim', 'não']

    while True:
        aux += preco
        print('Nossa carta de vinhos:')
        printa_essa_porra(vinhos, precos)
        tipo_vinho = forca_escolhe('Qual o tipo de vinho de hoje? \n --> ', vinhos,
                                   'Inválido! Por favor, escolha entre')
        qtd_garrafa = verifica_numero('Quantas garrafas você quer? \n -->')
        i = index(tipo_vinho, vinhos)

        qtd[i] += qtd_garrafa
        preco = precos[i] * qtd[i]

        if forca_escolhe('Gostaria de mais algum vinho? \n', quer_ou_n_quer,
                         'Por favor digite sim ou não (em minúsculas)') == 'sim':
            continue
        else:
            print('------------------ CARRINHO ---------------------')
            printa_essa_porra(vinhos, precos, qtd)
            print(f'\n SUBTOTAL: R${preco + aux:.2f}\n\n')

            if preco + aux > frete_gratis:
                print('Parabéns! Você ganhou o frete gratis!\n'
                      f'PREÇO TOTAL DA COMPRA: {aux + preco:.2f}\n \n'
                      f'Obrigado pela compra! Conte sempre conosco!')
                break
            else:
                print(f'Frete para {endereco}: R${frete:.2f}\n'
                      f'PREÇO TOTAL DA COMPRA: {aux + preco + frete:.2f}\n'
                      f'Obrigado pela compra! Conte sempre conosco!')
                break
