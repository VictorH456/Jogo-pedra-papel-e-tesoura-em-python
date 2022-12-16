from random import choice
qt = {'qe':0,'qv':0,'qd':0}
lista = ['Pedra','Papel','Tesoura']
while True:
    res = input('Digite Pedra, Papel ou Tesoura ').title().strip()
    a = choice(lista)
    if res == a:
        qt['qe'] += 1
        print(f'Empate, nem vitória nem derrota \nO jogador escolheu: {res} e a maquina: {a}')
    elif (res == 'Pedra' and a == 'Tesoura') or (res == 'Tesoura' and a == 'Papel') or (res == 'Papel' and a == 'Pedra'):
        qt['qv'] += 1
        print(f'Parabéns, Você ganhou! \nO jogador escolheu: {res} e a maquina: {a}')
    else:
        qt['qd'] += 1
        print(f'Você perdeu, mais sorte da próxima! \nO jogador escolheu: {res} e a maquina: {a}')
    i=input('Quer continuar jogando? Sim ou Não ').title().strip()
    if i == 'Não': break
print(f'Quantidade de Vitórias: {qt["qv"]} \nQuantidade de Derrotas:{qt["qd"]} \nQuantidade de Empates:{qt["qe"]} \nTenha um ótimo dia!')
