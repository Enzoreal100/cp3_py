#rm557943 - Enzo Gaião Real
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
        print(erro)
        escolha = input(msg)
        continue
    return escolha


endereco = input('Qual o seu endereço? (Rua, N°)\n --> ')
idade = verifica_numero('Qual seu ano de nascimento?\n --> ')
ano_atual = 2024

if ano_atual - idade < 18:
    print('É proibida a venda de bebidas alcoólicas para menores de idade')
else:
    print('Seja bem vindo a Vinheria Agnello!')
        #Facilita caso precise mudar os vinhos
    vinhos = ['branco', 'tinto', 'rosé']
        #Facilita caso precise mudar o preço
    precos = [59.9, 79.9, 63.9]
        #Soma de quantidade de garrafas
    qtd = [0,0,0]
    aux = 0
    preco = 0
        #Facilita caso o limite para frete gratis mude
    frete_gratis = 500
    frete = 30
    quer_ou_n_quer = ['sim', 'não']

    carta = (f'Nossa carta de vinhos: \n'
            f'{vinhos[0]}: R${precos[0]:.2f}\n'
            f'{vinhos[1]}: R${precos[1]:.2f}\n'
            f'{vinhos[2]}: R${precos[2]:.2f}\n')

    while True:
        aux += preco
        print(carta)
        tipo_vinho = forca_escolhe('Qual o tipo de vinho de hoje? \n --> ', vinhos, 'Inválido! Por favor, escolha entre')
        qtd_garrafa = verifica_numero('Quantas garrafas você quer? \n -->')
        qtd_garrafa = int(qtd_garrafa)

        if tipo_vinho == vinhos[0]:
            valor_vinho = precos[0]
            qtd[0] += qtd_garrafa
        elif tipo_vinho == vinhos[1]:
            valor_vinho = precos[1]
            qtd[1] += qtd_garrafa
        else:
            valor_vinho = precos[2]
            qtd[2] += qtd_garrafa

        preco = valor_vinho * qtd_garrafa

        if forca_escolhe('Gostaria de mais algum vinho? \n', quer_ou_n_quer,'Por favor digite sim ou não (em minúsculas)' ) == 'sim':
            continue
        else:
            print('------------------ CARRINHO ---------------------')
            print(f'{vinhos[0]}: {qtd[0]} Unidades \n'
                    f'{vinhos[1]}: {qtd[1]} Unidades\n '
                    f'{vinhos[2]}: {qtd[2]} Unidades \n')
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