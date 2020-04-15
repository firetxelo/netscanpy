def menu_principal():
    print('=*' * 40)
    print('Digite o número referente a opção desejada: ')
    print('[ 1 ] - Scan de Rede')
    print('[ 2 ] - Scan de Portas Abertas para 1 endereço')
    print('[ 3 ] - Scan de Portas Abertas para todos os endeços online')
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
        print('Digite o endereço da rede a ser verificada (Exempplo: 192.168.1.0)')
        ipuser = str(input('Ou digite 0 para escolher automaticamente a rede vinculada ao hostname do computador : '))
        if ipuser == '0':
            return '0'
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
