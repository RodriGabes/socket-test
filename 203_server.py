from socket import *

config={ # Configuração de variáveis
    "porta":1203
}

dados={ # Armazenamento dos dados da resposta do servidor
     "1":"Uma Linha&Duas Linha&Tres Linha",
     "2":".&.&.&.&.&.&.&.&.&.",
     "erro":"404 RECURSO NAO ENCONTRADO",
     "ping":"pong"

}

# Mensagem de inicialização
print("""
MODULO SERVIDOR
=+=========+=
MODULO 3, TRABALHO 1
=+=========+=
12611CBS203
Gabriel R Silva
=+=========+=
Digite '!exit' ou '!sair' para fechar o servidor a qualquer momento...
Digite 'udp' ou 'tcp' para iniciar o servidor...
=+=========+=""")

resp="" # resp é a variável de input da linha de comando
try: # Estrutura do menu e do código, dentro de try/except para tratar erros
    while True:
        resp=input()
        if resp[:5].lower()=="!exit" or resp[:5].lower()=="!sair": break # encerra o programa
        elif resp[:3].lower()=="udp":
            try:
                serverSocket = socket(AF_INET, SOCK_DGRAM)
                serverSocket.bind(('',config['porta']))
                print(f">>> SUCESSO: Servidor >>>UDP<<< ouvindo na porta {config['porta']}")
                print(f"Pressione Ctrl + C para encerrar...")
                while True:
                    msg, cliente_end = serverSocket.recvfrom(2048)
                    msg_cmd = msg.decode().lower()
                    if msg_cmd in list(dados.keys()):
                        serverSocket.sendto(dados[msg_cmd].encode(),cliente_end)
                    else: serverSocket.sendto(dados["erro"].encode(),cliente_end)
            except Exception as erroConn:
                    print(f""">>> ERRO: Nao foi possivel estabelecer um servidor...
>>> CAUSA: {erroConn}""")
        elif resp[:3].lower()=="tcp":
            pass
except Exception as erro:
    print(f">>> ERRO: {erro}")
print("=+= SERVIDOR ENCERRADO =+=") # mensagem de encerramento