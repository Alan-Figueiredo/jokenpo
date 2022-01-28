                                #input('sua vez de escolher: ')
import random
escolha = ('pedra','papel','tesoura')
maquina = ('pedra','papel','tesoura')
maquina = random.choice(maquina)
escolha = random.choice(escolha)

def pedra(e,m):
    if e == 'pedra' and m == 'tesoura':
        return 'Player1 venceu'
    if e == 'pedra' and m == 'papel':
        return 'Player2 venceu'    
    else:
        return 'empate'

def papel(e,m):
    if e == 'papel' and m == 'pedra':
        return 'Player1 venceu'
    if e == 'papel' and m == 'tesoura':
        return 'Player2 venceu'    
    else:
        return 'empate'

def tesoura(e,m):
    if e == 'tesoura' and m == 'papel':
        return 'Player1 venceu'
    if e == 'tesoura' and m == 'pedra':
        return 'Player2 venceu'    
    else:
        return 'empate'

if escolha == 'pedra':
    pedra
elif escolha == 'papel':
    papel
else:
    tesoura

if pedra(escolha,maquina) == 'Player1 venceu':
    teste = 'Player1 venceu'
elif pedra(escolha,maquina) =='Player2 venceu':
    teste = 'Player2 venceu'
elif tesoura(escolha,maquina) =='Player1 venceu':
    teste = 'Player1 venceu'
elif tesoura(escolha,maquina) =='Player2 venceu':
    teste = 'Player2 venceu'
elif papel(escolha,maquina) =='Player1 venceu':
    teste = 'Player1 venceu'
elif papel(escolha,maquina) =='Player2 venceu':
    teste = 'Player2 venceu'
else:
    teste = 'Empate'


print(f'(PLayer1 escolheu : {escolha.upper()}) VS (PLayer2 escolheu: {maquina.upper()})\n{teste}')