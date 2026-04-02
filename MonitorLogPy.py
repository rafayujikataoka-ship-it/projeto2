import random 
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print('MENU\n')
        print('1 - Gerar logs')
        print('2 - Analisar logs')
        print('3 - Gerar e analisar logs')
        print('4 - Sair')
        opc = int(input('Digite a opção desejada: '))
        if opc == 1:
            try:
                qtd = int(input('Quantidade de logs(arquivos): '))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Entrada inválida. ')
        elif opc == 2:
            analisarLogs(nome_arq)
        elif opc == 3:
            try:
                qtd = int(input('Quantidade de logs(arquivos): '))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq)
            except:
                print('Entrada inválida. ')
            analisarLogs(nome_arq)
        elif opc == 4:
            print('Até mais.')
            break
    else:
        print('Opção inválida')
        
def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montaLog(i) + '\n')
    print('Log errado.')

def montarLog(i):
    data = gerarData(i)
    IP = gerarIp (i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    tamanho = gerarTamanho(i)
    return f'{data} {IP} - {metodo} - {status} - {recurso} - ´{tempo}ms - {tamanho} - {protocolo} - {agente} - /home'
    
def gerarData(i): 
    base = datatime.datatime.now()
    delta = datetime.timedelta(seconde= i * random.randint(5,20))
    return (base + delta).strftime('%d/%m/%y %H:%M:%S')
def gerarip(i):
    r = random.randint(1,6)
    if i >= 20 and i <= 50:
        return '203.120.45.7'
    
    if r == 1:
        return '192.168.1.100'
    elif r == 2:
        return '192.168.5.100'
    elif r == 3:
        return '192.168.77.100'
    elif r == 4:
        return '192.168.43.100'
    elif r == 5:
        return '192.168.13.100'
    elif r == 6:
        return '192.168.22.100'
    
    