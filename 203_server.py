from socket import *

config={ # Configuração de variáveis
    "porta":1203
}

dados={ # Armazenamento dos dados da resposta do servidor
     "teste1":"Uma Linha&Duas Linha&Tres Linha",
     "10linhas":".&.&.&.&.&.&.&.&.&.",
     "erro":"404 RECURSO NAO ENCONTRADO",
     "ping":"d8888b.  .d88b.  d8b   db  d888b &88  `8D .8P  Y8. 888o  88 88' Y8b&88oodD' 88    88 88V8o 88 88&88~~~   88    88 88 V8o88 88  ooo&88      `8b  d8' 88  V888 88. ~8~&88       `Y88P'  VP   V8P  Y888P ",
     "listar":"teste1&10linhas&ping&listar&tulipa&palmeira&mundi",
     "tulipa":"         ;M\";::;;&        ,\':;: \"\"\'.&       ,M;. ;MM;;M:&       ;MMM::MMMMM:&      ,MMMMM\'MMMMM:&      ;MMMMM MMMMMM&      MMMMM::MMMMMM:&      :MM:\',;MMMMMM\'&      \':: \'MMMMMMM:&        \'; :MMMMM\"&           \'\'\"\"\"\'&            .&            M&            M&.           M           .&\'M..        M        ,;M\'& \'MM;.      M       ;MM:&  :MMM.     M      ;MM:&  \'MMM;     M     :MMM:&   MMMM.    M     MMMM:&  :MMMM:    M     MMMM:&  :MMMM:    M    :MMMM:&  :MMMMM    M    ;MMMM:&  \'MMMMM;   M   ,MMMMM:&   :MMMMM.  M   ;MMMMM\'&    :MMMM;  M  :MMMMM\"&     \'MMMM  M  ;MMMM\"&-hrr- \':MM  M ,MMM:\'&        \"\": M :\"\"\'&This ASCII pic can be found at asciiart.website/art/3768",
     "palmeira":"###########################\'`################################&###########################  V##\'############################&#########################V\'  `V  ############################&########################V\'      ,############################&#########`#############V      ,A###########################V&########\' `###########V      ,###########################V\',#&######V\'   ###########l      ,####################V~~~~\'\',###&#####V\'    ###########l      ##P\' ###########V~~\'   ,A#######&#####l      d#########l      V\'  ,#######V~\'       A#########&#####l      ##########l         ,####V\'\'         ,###########&#####l        `V######l        ,###V\'   .....;A##############&#####A,         `######A,     ,##V\' ,A#######################&#######A,        `######A,    #V\'  A########\'\'\'\'\'##########\'\'&##########,,,       `####A,           `#\'\'           \'\'\'  ,,,&#############A,                               ,,,     ,######&######################oooo,                 ;####, ,#########&##################P\'                   A,   ;#####V##########&#####P\'    \'\'\'\'       ,###             `#,     `V############&##P\'                ,d###;              ##,       `V#########&##########A,,   #########A              )##,    ##A,..,ooA###&#############A, Y#########A,            )####, ,#############&###############A ############A,        ,###### ##############&###############################       ,#######V##############&###############################      ,#######################&##############################P    ,d########################&##############################\'    d#########################&##############################     ##########################&##############################     ##########################&#############################P     ##########################&#############################\'     ##########################&############################P      ##########################&###########################P\'     ;##########################&###########################\'     ,###########################&##########################       ############################&#########################       ,############################&########################        d###########P\'    `Y#########&#######################        ,############        #########&######################        ,#############        #########&#####################        ,##############b.    ,d#########&####################        ,################################&###################         #################################&##################          #######################P\'  `V##P\'&#######P\'     `V#           ###################P\'&#####P\'                    ,#################P\'&###P\'                      d##############P\'\'&##P\'                       V##############\'&#P\'                         `V###########\'&#\'                             `V##P\'&                                                        GNN94&This ASCII pic can be found at asciiart.website/art/3819",
     "mundi":":::::::::::''  ''::'      '::::::  `:::::::::::::'.:::::::::::::::&:::::::::' :. :  :         ::::::  :::::::::::.:::':::::::::::::::&::::::::::  :   :::.       :::::::::::::..::::'     :::: : :::::::&::::::::    :':  \"::'     '\"::::::::::::: :'           '' ':::::::&:'        : '   :  ::    .::::::::'    '                        .:&:               :  .:: .::. ::::'                              :::&:. .,.        :::  ':::::::::::.: '                      .:...::::&:::::::.      '     .::::::: '''                         :: :::::.&::::::::            ':::::::::  '',            '    '   .:::::::::&::::::::.        :::::::::::: '':,:   '    :         ''' :::::::::&::::::::::      ::::::::::::'                        :::::::::::::&: .::::::::.   .:''::::::::    '         ::   :   '::.::::::::::::&:::::::::::::::. '  '::::::.  '  '     :::::.:.:.:.:.:::::::::::::&:::::::::::::::: :     ':::::::::   ' ,:::::::::: : :.:'::::::::::&::::::::::::::::: '     :::::::::   . :'::::::::::::::' ':::::::::&::::::::::::::::::''   :::::::::: :' : ,:::::::::::'      ':::::::&:::::::::::::::::'   .::::::::::::  ::::::::::::::::       :::::::&:::::::::::::::::. .::::::::::::::::::::::::::::::::::::.'::::::::&:::::::::::::::::' :::::::::::::::::::::::::::::::::::::::::::::::&::::::::::::::::::.:::::::::::::::::::::::::::::::::::::::::::::::&This ASCII pic can be found at asciiart.website/art/2530"
}

# Mensagem de inicialização
print("""
.d8888. d88888b d8888b. db    db d888888b d8888b.  .d88b.  d8888b.
88'  YP 88'     88  `8D 88    88   `88'   88  `8D .8P  Y8. 88  `8D
`8bo.   88ooooo 88oobY' Y8    8P    88    88   88 88    88 88oobY'
  `Y8b. 88~~~~~ 88`8b   `8b  d8'    88    88   88 88    88 88`8b  
db   8D 88.     88 `88.  `8bd8'    .88.   88  .8D `8b  d8' 88 `88.
`8888Y' Y88888P 88   YD    YP    Y888888P Y8888D'  `Y88P'  88   YD
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
                serverSocket = socket(AF_INET, SOCK_DGRAM) # Abre o socket
                serverSocket.bind(('',config['porta'])) # Configura a porta
                print(f">>> SUCESSO: Servidor >>>UDP<<< ouvindo na porta {config['porta']}")
                print(f"Feche o Programa para encerrar...")
                while True: # Estrutura de funcionamento: escutar ad infinitum
                    msg, cliente_end = serverSocket.recvfrom(2048)
                    msg_cmd = msg.decode().lower()
                    if msg_cmd in list(dados.keys()):
                        serverSocket.sendto(dados[msg_cmd].encode(),cliente_end)
                    else: serverSocket.sendto(dados["erro"].encode(),cliente_end)
            except Exception as erroConn:
                    print(f""">>> ERRO: Nao foi possivel estabelecer um servidor...
>>> CAUSA: {erroConn}""")
        elif resp[:3].lower()=="tcp":
            try:
                serverSocket = socket(AF_INET, SOCK_STREAM) # Abre o socket
                serverSocket.bind(('',config["porta"])) # Configura a porta
                serverSocket.listen(10) # Escutar a conexão, com fila máxima de 10
                print(f">>> SUCESSO: Servidor >>>TCP<<< ouvindo na porta {config['porta']}")
                print(f"Feche o Programa para encerrar...")
                while True:
                    connSocket, endr = serverSocket.accept() # Recebe a requisição
                    msg = connSocket.recv(1024).decode().lower()
                    if msg in list(dados.keys()):
                        connSocket.send(dados[msg].encode())
                    else: connSocket.send(dados["erro"].encode())
                    connSocket.close() # Fecha a conexão
            except Exception as erroConn:
                print(f""">>> ERRO: Nao foi possivel estabelecer um servidor...
>>> CAUSA: {erroConn}""")
except Exception as erro:
    print(f">>> ERRO: {erro}")
print("=+= SERVIDOR ENCERRADO =+=") # mensagem de encerramento