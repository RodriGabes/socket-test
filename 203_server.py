
config={ # Configuração de variáveis
    "porta":1203
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

# Confirmação de inicialização
print()

resp="" # resp é a variável de input da linha de comando
try: # Estrutura do menu e do código, dentro de try/except para tratar erros
    while True:
        resp=input()
        if resp[:5].lower()=="!exit" or resp[:5].lower()=="!sair": break # encerra o programa
        elif resp[:3].lower()=="udp":
            pass
        elif resp[:3].lower()=="tcp":
            pass
except:
    print("Erro Fatal")
print("=+= SERVIDOR ENCERRADO =+=") # mensagem de encerramento