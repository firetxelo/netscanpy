"""
"route -n | head -n3 | tail -n1 | awk '{print $2}'"
"""
import os
from ipaddress import ip_network
import socket


def ping_discovery(net=0):
    """
    Função que realiza descoberta de hosts onlines na rede utilizando ping. Por padrão utiliza rede vinculada ao
    hostname da máquina onde o script está sendo rodado com a máscara /24. Por exemplo, se o seu ip é 192.168.10.10,
    a rede a ser utilizada no scan será 192.168.10.0/24
    :param net: Opcional, Rede a ser escaneada. Se não especificado será utilizada rede do gateway padrão
    :return: Lista com os endereços que responderam o ping.
    """
    # if __name__ == '__main__':
    if net == '0':
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            if host_ip == '127.0.0.1':
                return "Não foi possível coletar seu IP - Por favor tente informar o mesmo"
            else:
                target = host_ip[0:host_ip.rfind(".")] + '.0/24'
                nethosts = ip_network(target).hosts()
                iponline = []
                for ip in nethosts:
                    pingresult = os.system(f"ping -q -c 1 {ip}")
                    if pingresult == 0:
                        iptemp = ip
                        iponline.append(iptemp)
                return iponline
        except KeyboardInterrupt:
            print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
            return 0
        except:
            print("Tente digitar a rede no formato 172.16.0.0/24")
    else:
        target = net
        try:
            nethosts = ip_network(target).hosts()
            iponline = []
            for ip in nethosts:
                pingresult = os.system(f"ping -c 1 {ip}")
                if pingresult == 0:
                    iptemp = ip
                    iponline.append(iptemp)
            return iponline
        except KeyboardInterrupt:
            print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
            return 0
        except:
            print("Tente digitar a rede no formato 172.16.0.0/24")


def tcp_discovery(net=0):
    """
    Função que realiza a descoberta de hosts online através de conexões em portas TCP. Por padrão são utilizadas
    as portas 21, 22, 23, 25, 80, 110, 139, 443 e 445.
    :param net:
    :return:
    """
    if net == '0':
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            if host_ip == '127.0.0.1':
                return "Não foi possível coletar seu IP - Por favor tente informar o mesmo"
            else:
                target = host_ip[0:host_ip.rfind(".")] + '.0/24'
                nethosts = ip_network(target).hosts()
                iponline = []
                portasalvo = [21, 22, 23, 25, 80, 110, 139, 443, 445]
                for ip in nethosts:
                    for portas in portasalvo:
                        testsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        respteste = testsocket.connect_ex(ip, portas)
                        if (respteste == 0):
                            print(f'A porta {portas} no endereço {ip} está aberta')
                            listaendport = [portas, ip]
                            iponline.append(listaendport)
                for ip in range(0, len(iponline)):
                    print(f'O endereço {iponline[ip][0]} tem as seguintes portas abertas: ')
                    for porta in range(1, len(iponline[ip][1])):
                        print(f'Porta: {porta}')
        except KeyboardInterrupt:
            print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
            return 0
        except:
            print("Tente digitar a rede no formato 172.16.0.0/24")

    else:
        target = net
        try:
            nethosts = ip_network(target).hosts()
            iponline = []
            portasalvo = [21, 22, 23, 25, 80, 110, 139, 443, 445]
            for ip in nethosts:
                for portas in portasalvo:
                    ipstr = str(ip)
                    testsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    if (testsocket.connect_ex((ipstr, portas)) == 0):
                        print(f'A porta {portas} no endereço {ipstr} está aberta')
                        listaendport = [portas, ipstr]
                        iponline.append(listaendport)
                    testsocket.close()
            for ip in range(0, len(iponline)):
                print(f'O endereço {iponline[ip][1]} tem as seguintes portas abertas: ')
                for porta in range(1, len(iponline[ip][0])):
                    print(f'Porta: {porta}')
        except KeyboardInterrupt:
            print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
            return 0


tcp_discovery("192.168.100.0/30")
