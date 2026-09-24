from socket import *

config={ # Configuração de variáveis
    "porta":1203,
    "endereco":"127.0.0.1" # Endereço do servidor, loopback por padrão
}

erros={ # Dicionario para mensagens de erro
    -1:"Comando digitado incorretamente. Tente novamente...",
    1: "O endereço de IP fornecido nao e valido...",
    2: "A porta fornecida nao e valida..."
}

# Mensagem de inicialização
print("""
MODULO CLIENTE
=+=========+=
MODULO 3, TRABALHO 1
=+=========+=
12611CBS203
Gabriel R Silva
=+=========+=
Digite '!exit' ou '!sair' para fechar o cliente a qualquer momento...
Digite 'udp [XXX.XXX.XXX.XXX]:[PORTA]' para iniciar o cliente no modo UDP...
=+=========+=""")

# Confirmação de inicialização
print("Iniciado")

def validaIP(alvo): # Funcao para validação do endereço de IP do servidor
    try:
        alvo=alvo[4:] # Corta o comando da linha de texto
        x=alvo.split(":") # Separa porta e IP
        octetos=x[0].split(".") # Separa os octetos do IP
        for y in range(4):
            if int(octetos[y])>= 0 and int(octetos[y])<256: pass
            else: return 1 # Verfica se cada octeto está entre 0 e 255
        if int(octetos[0]) ==0: return 1
        if int(x[1]) >1000 and int(x[1]) <2000: pass
        else: return 2 # Verifica se o numero da porta está entre 1000 - 2000
        config.update({"porta":int(x[1]),"endereco":x[0]})
        return 0
    except Exception as erro:
        print(erro)
        return -1

resp="" # resp é a variável de input da linha de comando
try: # Estrutura do menu e do código, dentro de try/except para tratar erros
    while True:
        resp=input()
        if resp[:5].lower()=="!exit" or resp[:5].lower()=="!sair": break # encerra o programa
        elif resp[:3].lower()=="udp": ### Modo UDP
            x=validaIP(resp)
            if x==0: # IP:Port validado com sucesso
                try:
                    clientSocket=socket(AF_INET, SOCK_DGRAM)
                    print(f">>> Cliente UDP conectado ao servidor: {config['endereco']} porta: {config['porta']}")
                    msg=input("Comando > ")
                    clientSocket.sendto(msg.encode(),(config["endereco"],config["porta"]))
                    serv_resp, serv_end = clientSocket.recvfrom(2048)
                    raw_dados=serv_resp.decode()
                    dados=raw_dados.split("&")
                    for w in dados:
                        pass ######
                    clientSocket.close()
                except Exception as erroConn:
                    print(f""">>> ERRO: Nao foi possivel se conectar ao servidor...
>>> CAUSA: {erroConn}""")
            else: print(erros[x])
            
        elif resp[:3].lower()=="tcp": ### Modo TCP
            x=validaIP(resp)
            if x==0: # IP:Port validado com sucesso
                try:
                    print(f">>> Cliente TCP conectado ao servidor: {config['endereco']} porta: {config['porta']}")
                except Exception as erroConn:
                    print(f""">>> ERRO: Nao foi possivel se conectar ao servidor...
>>> CAUSA: {erroConn}""")
            else: print(erros[x])
        else: print(">>> Comando nao reconhecido. Tente novamente...")
except Exception as erro:
    print(f">>> ERRO: {erro}")
print("=+= CLIENTE ENCERRADO =+=") # mensagem de encerramento