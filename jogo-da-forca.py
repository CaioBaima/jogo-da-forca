# Importar bibliotecas necessárias:
from random import choice
from time import sleep

# Funções úteis:
def abertura ():
    print('''    _                      _             ___                    
 _ | | ___  __ _  ___     __| | __ _    | __|___  _ _  __  __ _ 
| || |/ _ \/ _` |/ _ \   / _` |/ _` |   | _|/ _ \| `_|/ _|/ _` |
 \__/ \___/\__, |\___/   \__,_|\__,_|   |_| \___/|_|  \__|\__,_|
           |___/                                                ''')

def start():
    print(r''' __      __                              _                        
 \ \    / /                             | |                       
  \ \  / /_ _ _ __ ___   ___  ___       | | ___   __ _  __ _ _ __ 
   \ \/ / _` | `_ ` _ \ / _ \/ __|  _   | |/ _ \ / _` |/ _` | `_|
    \  / (_| | | | | | | (_) \__ \ | |__| | (_) | (_| | (_| | |   
     \/ \__,_|_| |_| |_|\___/|___/  \____/ \___/ \__, |\__,_|_|   
                                                  __/ |           
                                                 |___/ ''')

def ganhou():
    print(r''' __      __        //\                     _                 _ 
 \ \    / /       |/ \|                   | |               | |
  \ \  / /__   ___ ___    __ _  __ _ _ __ | |__   ___  _   _| |
   \ \/ / _ \ / __/ _ \  / _` |/ _` | '_ \| '_ \ / _ \| | | | |
    \  / (_) | (_|  __/ | (_| | (_| | | | | | | | (_) | |_| |_|
     \/ \___/ \___\___|  \__, |\__,_|_| |_|_| |_|\___/ \__,_(_)
                          __/ |                                
                         |___/                                 ''')


def perdeu():
    print(''' __      __        //\                      _            _ 
 \ \    / /       |/ \|                    | |          | |
  \ \  / /__   ___ ___   _ __   ___ _ __ __| | ___ _   _| |
   \ \/ / _ \ / __/ _ \ | `_ \ / _ \ `__/ _` |/ _ \ | | | |
    \  / (_) | (_|  __/ | |_) |  __/ | | (_| |  __/ |_| |_|
     \/ \___/ \___\___| | .__/ \___|_|  \__,_|\___|\__,_(_)''')

def linha_vazia(n):
    for n in range(0, n):
        print('')

def ensinar_regras():
    regras = ('''- Se você digitar uma letra da palavra secreta, te revelarei dicas que te ajudarão a ganhar.\n
- Caso a letra digitada não exista sua cabeça será pendurada na forca.\n
- Para cada letra inexistente na palavra, um membro de seu corpo será adicionado.\n
- Caso erre 6 vezes, seu corpo todo estará pendurado então GAME OVER!\n\n\n''')
    while True:
        ensinar = str(input('Se você já conhece as regras? [S/N]\n')).upper()
        if ensinar == 'S':
            sleep(1)
            break
        elif ensinar == 'N':
            print('Você me informou que não conhece as regras. Apresentarei as regras abaixo:\n')
            sleep(1)
            print(regras)
            sleep(2)
            break
        else:
            print('Digite S para SIM e N para NÃO!')

def boneco(n):
    if n == 0:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
   / /_\ \  
  / /_ _\ \ 
 /_/ | | \_\
    |___|   
   / / \ \  
  / /   \ \ 
 /_/     \_\
''')

    elif n == 1:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
''')

    elif n == 2:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
   / /      
  / /_      
 /_/ |      
    |___|   ''')

    elif n == 3:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
   / /_\ \  
  / /_ _\ \ 
 /_/ | | \_\
    |___|   ''')

    elif n == 4:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
   / /_\ \  
  / /_ _\ \ 
 /_/ | | \_\
    |___|   
   / /      
  / /       
 /_/        ''')

    elif n == 5:
        print(r'''     ___    
    / _ \   
   | (_) |  
    \___/   
   / /_\ \  
  / /_ _\ \ 
 /_/ | | \_\
    |___|   
   / / \ \  
  / /   \ \ 
 /_/     \_\ ''')



# Apresentação divertida:
abertura()
nome = str(input('Jogador(a), para colocar a sua cabeça na forca, digite seu nome:\n'))
print(end='\n'*3)
print(f'Seja muito bem vindo(a), {nome}. Abaixo verá seu avatar:')
sleep(1)

boneco(0)

linha_vazia(3)
ensinar_regras()
linha_vazia(3)

start(), sleep(2), linha_vazia(1)

import lista_de_palavras
while True:
    # Sorteando a palavra:
    
    itens = lista_de_palavras.palavras
    palavra_secreta = (choice(itens))

    # Dica de quantas letras:
    print('Abaixo está sua palavra secreta, digite uma letra para começar a tentar se salvar!')
    linha_vazia(1)

    quantidade_de_letras = len(palavra_secreta)

    for letra in range(quantidade_de_letras):
        print('_', end=' ')
    linha_vazia(1)

    # Código para as tentativas:
    letras_tentadas = []
    letras_corretas = '_'*len(palavra_secreta)

    while True:
        tentativa = (input('Digite uma letra:')).upper()
        letras_tentadas.append(tentativa)
        
        if len(tentativa) > 1 or tentativa.isalpha() == False:
            letras_tentadas.pop()
            print('Digite apenas um caractere. Também é necessário que seja uma letra e que não tenha!')
        
        elif letras_tentadas.count(tentativa) > 1:
            letras_tentadas.pop()
            print('Digite uma letra que ainda não tenha tentado!')
        
        elif tentativa in palavra_secreta:
            letras_tentadas.pop()
            localizar = []
            
            for posicao, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    localizar.append(posicao)
            
            for index in localizar:
                letras_corretas = letras_corretas[:index] + tentativa + letras_corretas[index+1:]
            
            print('Você achou algo! Veja abaixo o que descobriu:')
            linha_vazia(1)
            print(letras_corretas)
            
            if letras_corretas == palavra_secreta:
                ganhou()
                break

        elif tentativa not in palavra_secreta and len(letras_tentadas) == 1:
            boneco(1)
        
        elif tentativa not in palavra_secreta and len(letras_tentadas) == 2:
            boneco(2)
        
        elif tentativa not in palavra_secreta and len(letras_tentadas) == 3:
            boneco(3)
        
        elif tentativa not in palavra_secreta and len(letras_tentadas) == 4:
            boneco(4)
        
        elif tentativa not in palavra_secreta and len(letras_tentadas) == 5:
            boneco(5)
            linha_vazia(1)
            print('Vou te dar uma última chance!!!')
        
        elif len(letras_tentadas) == 6:
            perdeu()
            linha_vazia(3)
            print(f'A palavra que estava procurando era:\n {palavra_secreta}')
            break
    
    linha_vazia(2)

    encerrar = str(input('Você quer jogar novamente?\nDigite [ENTER] reiniciar o jogo.\nOu digite [N] Para encerrar o programa.\n')).upper().strip()
    if encerrar == 'N':
        break
    else:
        linha_vazia(10)
