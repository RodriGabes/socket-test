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
 .o88b. db      d888888b d88888b d8b   db d888888b d88888b
d8P  Y8 88        `88'   88'     888o  88 `~~88~~' 88'    
8P      88         88    88ooooo 88V8o 88    88    88ooooo
8b      88         88    88~~~~~ 88 V8o88    88    88~~~~~
Y8b  d8 88booo.   .88.   88.     88  V888    88    88.    
 `Y88P' Y88888P Y888888P Y88888P VP   V8P    YP    Y88888P
=+=========+=
MODULO 3, TRABALHO 1
=+=========+=
12611CBS203
Gabriel R Silva
=+=========+=
Digite '!exit' ou '!sair' para fechar o cliente a qualquer momento...
Digite 'udp [XXX.XXX.XXX.XXX]:[PORTA]' para iniciar o cliente no modo UDP...
Digite 'tcp [XXX.XXX.XXX.XXX]:[PORTA]' para iniciar o cliente no modo TCP...
=+=========+=""")

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
                while True: # Abre o loop para conexões
                    try:
                        clientSocket=socket(AF_INET, SOCK_DGRAM) # Abre o socket UDP
                        print(f">>> Cliente UDP conectado ao servidor: {config['endereco']} porta: {config['porta']}")
                        msg=input("Comando > ")
                        if msg.lower() in ["!exit","!sair"]: break
                        clientSocket.sendto(msg.encode(),(config["endereco"],config["porta"])) # Envia requisição
                        serv_resp, serv_end = clientSocket.recvfrom(4096) # Recebe a resposta
                        raw_dados=serv_resp.decode()
                        clientSocket.close() # Fecha a conexão
                        dados=raw_dados.split("&")
                        print("| # | CONTEUDO")
                        l=1
                        for w in dados: # Exibe o conteúdo
                            if l<10: print(f"| {l} | {w}")
                            elif l<100: print(f"| {l}| {w}")
                            else: print(f"|{l}| {w}")
                            l+=1
                    except Exception as erroConn:
                        print(f""">>> ERRO: Nao foi possivel se conectar ao servidor...
>>> CAUSA: {erroConn}""")
                        break #Sai do looping para pedir outra entrada
                print(">>> Conexao UDP com o servidor encerrada")
            else: print(erros[x])
            
        elif resp[:3].lower()=="tcp": ### Modo TCP
            x=validaIP(resp)
            if x==0: # IP:Port validado com sucesso
                while True:
                    try:
                        clientSocket=socket(AF_INET, SOCK_STREAM) # Abre o socket TCP
                        clientSocket.connect((config["endereco"],config["porta"]))
                        print(f">>> Cliente TCP conectado ao servidor: {config['endereco']} porta: {config['porta']}")
                        msg=input("Comando >")
                        if msg.lower() in ["!exit","!sair"]: break
                        clientSocket.send(msg.encode()) # Envia a requisição
                        serv_resp = clientSocket.recv(4096) # Recebe a resposta
                        raw_dados = serv_resp.decode()
                        clientSocket.close() # Fecha a conexão
                        dados=raw_dados.split("&")
                        print("| # | CONTEUDO")
                        l=1
                        for w in dados: # Exibe o conteúdo
                            if l<10: print(f"| {l} | {w}")
                            elif l<100: print(f"| {l}| {w}")
                            else: print(f"|{l}| {w}")
                            l+=1
                    except Exception as erroConn:
                        print(f""">>> ERRO: Nao foi possivel se conectar ao servidor...
>>> CAUSA: {erroConn}""")
                        break # Sai do looping para pedir outra entrada
            else: print(erros[x])
        else: print(">>> Comando nao reconhecido. Tente novamente...")
except Exception as erro:
    print(f">>> ERRO: {erro}")
print("=+= CLIENTE ENCERRADO =+=") # mensagem de encerramento