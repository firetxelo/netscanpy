"""
"route -n | head -n3 | tail -n1 | awk '{print $2}'"
"""
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
    else:
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
    pass


