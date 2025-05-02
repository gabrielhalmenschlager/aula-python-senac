import random

"""

opcoes = ['Pedra', 'Papel', 'Tesoura']
vitoriasUsuario = 0
vitoriasMaquina = 0

print('\n===========================================')
print('== Pedra, Papel ou Tesoura - Melhor de 3 ==')
print('===========================================')

while vitoriasUsuario < 2 and vitoriasMaquina < 2:
    escolhaUsuario = input('\nDigite sua escolha (Pedra, Papel ou Tesoura): ')
    escolhaDaMaquina = random.choice(opcoes)

    print(f"\nVocê escolheu: {escolhaUsuario}")
    print(f"A máquina escolheu: {escolhaDaMaquina}")

    if escolhaUsuario not in opcoes:
        print('\nVocê deve escolher (Pedra, Papel ou Tesoura)')
    elif escolhaUsuario == escolhaDaMaquina:
        print('Empate')
    elif escolhaUsuario == 'Pedra' and escolhaDaMaquina == 'Tesoura':
        print("\nVocê venceu esta rodada!")
        vitoriasUsuario += 1
    elif escolhaUsuario == 'Papel' and escolhaDaMaquina == 'Pedra':
        print("\nVocê venceu esta rodada!")
        vitoriasUsuario += 1
    elif escolhaUsuario == 'Tesoura' and escolhaDaMaquina == 'Papel':
        print("\nVocê venceu esta rodada!")
        vitoriasUsuario += 1
    else:
        print("\nVocê perdeu esta rodada!")
        vitoriasMaquina += 1

    print(f"\nPlacar: Você {vitoriasUsuario} x {vitoriasMaquina} Máquina")

if vitoriasUsuario == 2:
    print("\nParabéns! Você venceu o jogo melhor de 3.")
else:
    print("\nA máquina venceu o jogo melhor de 3.")

"""

print('Digite "Pedra", "Papel" ou "Tesoura"')

vitoriasJogador = 0
vitoriasPc = 0
rodadas = 0
escolhas = ['pedra', 'papel', 'tesoura']

while rodadas < 3 and vitoriasJogador < 2 and vitoriasPc < 2:
    try:
        escolhaJogador = input('\nJogue: ').lower().strip()
        if escolhaJogador == 'sair':
            print('Jogo encerrado!')
            break

        if escolhaJogador not in escolhas:
            print('Erro, escolha inválida!')
            continue

        escolhaPc = random.choice(escolhas)
        print(f'\nVocê escolheu: {escolhaJogador.capitalize()}')
        print(f'PC escolheu: {escolhaPc.capitalize()}')

        if escolhaPc == escolhaJogador:
            print('Empate!')

        elif (escolhaJogador == "pedra" and escolhaPc == "tesoura") or \
             (escolhaJogador == "papel" and escolhaPc == "pedra") or \
             (escolhaJogador == "tesoura" and escolhaPc == "papel"):
            vitoriasJogador += 1
            rodadas += 1
            print('Você venceu a rodada!')
        else:
            vitoriasPc += 1
            rodadas += 1
            print('PC venceu a rodada!')

        print(f'\nPlacar - Jogador: {vitoriasJogador}, PC: {vitoriasPc}')
    except KeyboardInterrupt:
        print('\nJogo interrompido!')
        break

print('\n--= Fim de Jogo =--')
if vitoriasJogador >= 2:
    print('Parabéns, você venceu!')
elif vitoriasPc >= 2:
    print('Você perdeu!')
else:
    print('Jogo incompleto.')
