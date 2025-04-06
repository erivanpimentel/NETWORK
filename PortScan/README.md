# 🔍 SCAN_NETWORK

Este é um port scanner simples desenvolvido em Python, com suporte a **multithreading**, para realizar varreduras de portas TCP em um host alvo.

Foi feito como exercício de prática para relembrar conceitos de redes, `socket`, `threading` e leitura de argumentos via terminal com `optparse`.

---

## 🚀 Como usar

Execute o script com os parâmetros:

```bash
python3 portscanComthreading.py -i <IP_DO_ALVO> -r <PORTA_FINAL>

✅ Exemplo:
      python3 portscanComthreading.py -i 192.168.1.1 -r 8080

      Esse comando irá escanear todas as portas de 1 até 8080 no IP 192.168.1.1.

🛠️ Tecnologias usadas
  Python3
  socket
  threading
  optparse

⚠️ Aviso Legal
Este script foi criado apenas para fins educacionais.
Não use este código para escanear redes ou sistemas sem autorização.
O uso indevido pode violar leis locais ou diretrizes de segurança.
