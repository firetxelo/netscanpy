import os
from ipaddress import ip_network
import socket
from icmplib import ping,multiping


def ping_discovery(net=0):
    """
    Função que realiza descoberta de hosts onlines na rede utilizando ping. Por padrão utiliza rede vinculada ao
    hostname da máquina onde o script está sendo rodado com a máscara /24. Por exemplo, se o seu ip é 192.168.10.10,
    a rede a ser utilizada no scan será 192.168.10.0/24
    :param net: Opcional, Rede a ser escaneada. Se não especificado será utilizada rede do gateway padrão
    :return: Lista com os endereços que responderam o ping.
    """
    # if __name__ == '__main__':
    target = net
    try:
        nethosts = ip_network(target).hosts()
        iponline = []
        for ip in nethosts:
            ipstr = str(ip)
            pingresult = ping(ipstr)
            if pingresult.is_alive:
                iponline.append(pingresult.address)
        return iponline
    except KeyboardInterrupt:
        print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
        return 0
    except:
        print("Tente digitar a rede no formato 172.16.0.0/24")


def tcp_discovery(net=0):
    """
    Função que busca hosts onlines através de scanner de portas abertas. É realizado um teste nas 20 portas mais comuns
    de estarem abertas. 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080
    :param net Formato CIDR - Exemplo 172.17.0.0/24:
    :return: Lista com o ip do hosts online.
    """

    target = net
    try:
        nethosts = ip_network(target).hosts()
        iponline = []
        portlist = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900,
                    8080]
        for ip in nethosts:
            for port in portlist:
                ipstr = str(ip)
                testportskt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                testportskt.settimeout(1)
                if testportskt.connect_ex((ipstr, port)) == 0 :
                    iponline.append(ipstr)
                    testportskt.close()
                    break
        return iponline
    except KeyboardInterrupt:
        print('\nO usuário preferiu interromper a execução, portanto o retorno será 0')
        return 0
    except:
        print("Tente digitar a rede no formato 172.16.0.0/24")