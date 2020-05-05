import socket
import fcntl
import struct

def menu_principal():
    print('=*' * 40)
    print('Digite o número referente a opção desejada: ')
    print("[ 1 ] - Scan de Rede utilizando icmp")
    print('[ 2 ] - Scan de Rede utilizando tcp')
    print('[ 3 ] - Scan de Portas Abertas para 1 endereço')
    print('[ 4 ] - Scan de Portas Abertas para todos os endeços online')
    print('[ 0 ] Sair do programa')
    print('=*' * 40)
    try:
        escolhe = int(input('-> '))
    except:
        print('Digite uma opção válida!!!')
    else:
        return escolhe


def digita_ip():
    from socket import inet_aton
    while True:
        print('Digite o endereço da rede a ser verificada (Exemplo: 192.168.1.0)')
        ipuser = str(input('Ou digite 0 para escolher automaticamente a rede vinculada ao hostname do computador : '))
        if ipuser == '0':
            try:
                host_ip = escolhe_interface()
                inet_aton(host_ip)
                ipuser = host_ip[0:host_ip.rfind(".")] + '.0'
                ipverif01 = ipuser.split('.')
                if len(ipverif01) != 4:
                    print('Ocorreu um erro com o endereço digitado')
                else:
                    break
            except KeyboardInterrupt:
                print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
            except:
                print("Tente digitar a rede no formato 172.16.0.0/24")
        else:
            try:
                inet_aton(ipuser)
                ipverif01 = ipuser.split('.')
                if len(ipverif01) != 4:
                    print('Ocorreu um erro com o endereço digitado')
                else:
                    break
            except:
                print('Ocorreu um erro com o endereço digitado')
    while True:
        try:
            ipmask = int(input('Digite a Máscara de rede no formato CIDR (exemplos 8, 16, 24, ..., 32): '))
            if 1 <= ipmask <= 32:
                ipdigitado = ipuser + '/' + str(ipmask)
                return ipdigitado
        except:
            print('Digite um valo inteiro entre 1 e 32!')


def escolhe_interface():
    try:
        ifinfo = socket.if_nameindex()
        while True:
            for interf in range(0,len(ifinfo)):
                print(f"Digite {ifinfo[interf][0]} para escolher a interface {ifinfo[interf][1]}")
            ifoption = int(input('Qual sua escolha: '))
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ifname = ifinfo[ifoption -1][1]
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,
                struct.pack('256s', bytes(ifname[:15], 'utf-8'))
                )[20:24])
    except:
        return "Não foi possível determinar o endereço da interface"