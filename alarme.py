from  datetime import datetime
import time
import random

agora =  datetime.now()
agora = str(agora)
horario_atual = agora[10:16].strip()
alarmes = []
acabou =  False
posicao_alarme = 0

while acabou is False:
    resposta = str(input('Deseja adicionar algum alarme (S/N)? ')).upper().strip()

    if resposta == 'S':

        horario_alarme  = str(input('Qual horário você deseja que o alarme toque? (hh:mm) '))

        if horario_alarme[0:2].isnumeric() and horario_alarme[3:].isnumeric() and horario_alarme[2] == ':':
            hora = int(horario_alarme[0:2])
            minuto  = int(horario_alarme[3:])

            if hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59:
                alarmes.append(horario_alarme)
            else:
                print('Alarme inválido! Tente novamente!')
        else:
            print('Alarme inválido! Tente novamente!')

    elif resposta == 'N':
        acabou = True

    else:
        print('Resposta inválida! Tente novamente!')
acabou = True

if alarmes == []:
    print('Nenhum alarme programado!')
else:
    print(f'Seus alarmes são: {alarmes}')
print(horario_atual)

while True: 
    for i in range(len(alarmes)):
        if horario_atual in alarmes[i]:            
            print('HORA DE ACORDAR!')
            continue
        elif horario_atual not in alarmes[i]:
            print(f'AINDA NÃO ESTÁ NA HORA! O alarme é {alarmes[i]}hrs e a hora atual é {horario_atual}hrs!')