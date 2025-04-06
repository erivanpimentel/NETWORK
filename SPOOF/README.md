# 🎭 Programa Simples de ARP Spoofing

Este script foi criado como um **exercício prático** para entender o funcionamento de requisições ARP e como ocorre o **ARP Spoofing**, usando a biblioteca **Scapy**.

---

## 🚨 Aviso Importante

> ⚠️ **Este código é apenas para fins educacionais e de estudo.**
>  
> ⚠️ Nunca use este script em redes ou dispositivos sem a devida **autorização**, pois isso pode ser considerado **ilegal e antiético**.

---

## 🧠 O que o script faz?

O script envia repetidamente **requisições ARP falsas** para enganar o alvo, fazendo-o acreditar que o endereço IP do roteador está associado ao seu MAC.  
Essa técnica é usada em testes de segurança para simular ataques **Man-in-the-Middle (MITM)**.

---

## ⚙️ Tecnologias utilizadas

- Python3
- [Scapy](https://scapy.net/) — ferramenta poderosa para manipulação de pacotes
- `optparse` — para leitura de argumentos via linha de comando
- `time` — controle de envio


## 💻 Como usar
  python3 spoof.py -r <IP_DO_ROTEADOR> -d <IP_DA_VITIMA> -m <MAC_DA_VITIMA>

---
✅ Exemplo prático:
  python3 spoof.py -r 192.168.0.1 -d 192.168.0.50 -m 94:10:3E:AB:CD:EF
  Esse comando irá começar a enviar pacotes ARP spoofados para o IP 192.168.0.50, informando que o IP 192.168.0.1 (normalmente o roteador) está associado ao MAC 94:10:3E:AB:CD:EF.

---

📄 Explicações Técnicas
op = 1 → define a operação como ARP Request (pedido de resolução).

ARP(psrc=r, pdst=d, hwdst=m) → monta o pacote com:

IP de origem (psrc) = IP do roteador

IP de destino (pdst) = IP da vítima

MAC de destino (hwdst) = MAC da vítima

O script envia pacotes de forma contínua a cada segundo para manter o spoof ativo.

🛑 Reforço de Ética
Este script não deve ser usado em redes que não sejam de sua responsabilidade ou sem permissão explícita.
Sempre siga as boas práticas e diretrizes de segurança ofensiva ética (Ethical Hacking).


