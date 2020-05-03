from nettools import netfunctions
from nettools import regularfunciotns

while True:
    option = regularfunciotns.menu_principal()
    if option == 1:
        lista = []
        ipdigitado = regularfunciotns.digita_ip()
        print(f'Testando com rede {ipdigitado}')
        lista = netfunctions.ping_discovery(ipdigitado)
        for ip in lista:
            print(f'O IP {ip} está Online')
        print('Fim da Execução')
        print()

    elif option == 2:
        lista = []
        ipdigitado = regularfunciotns.digita_ip()
        lista = netfunctions.tcp_discovery(ipdigitado)
        for ip in lista:
            print(f'O host {ip} está Online')
        print('Fim da Execução')
        print()
    elif option == 3:
        print('Escolheu a opção 3')
    elif option == 4:
        print('Escolheu a opção 4')
    else:
        break

