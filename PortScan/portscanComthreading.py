import socket
import threading
import optparse

def portscan(porta):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(0.5)
    if meusocket.connect_ex((ip, porta)) == 0:
        print("Porta: " + str(porta) + "[ABERTA]")
        meusocket.close()


# Portscan de rede com threading----<>
#vamos instânciar para receber argumentos

parser = optparse.OptionParser('Utilize o programa da seguinte forma:' ' -i < IP DO ALVO > ' ' -r < PORTA FIN >')
#Vamos adicionar as opções
parser.add_option('-i', dest='ip', type='string', help='Informe o IP que deseja fazer a varredura')
parser.add_option('-r', dest='port_ran', type='string', help="Informe até que porta vai ser realizado o Scan")
#vamos pegar os args
(options, args) = parser.parse_args()
#vamos validar
if options.ip == None or options.port_ran == None:
    print(parser.usage)
    exit(0)
else:
    print('''**************************\n>>>>> INICIO DE SCAN <<<<<\n[+]>>> Varrendo host <<<[+]\n**************************''')
    ip = options.ip
    port_range = int(options.port_ran) + 1
    print(f'[+] Varrendo o IP: >>>>>> {ip} <<<<<<[+]\r\n')
    for porta in range(1, port_range):
        t = threading.Thread(target=portscan,kwargs={'porta':porta})
        t.start()
    
    

