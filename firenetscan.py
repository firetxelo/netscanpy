from nettools import netfunctions
from nettools import regularfunciotns

while True:
    option = regularfunciotns.menu_principal()
    if option == 1:
        lista = []
        listaonline = []
        ipdigitado = regularfunciotns.digita_ip()
        lista = netfunctions.ping_discovery(ipdigitado)
        for ip in lista:
            print(f'O IP {ip} está Online')
            listaonline.append(ip)
    elif option == 2:
        print('escolheu opção 2')
    elif option == 3:
        print('Escolheu a opção 3')
    else:
        break


