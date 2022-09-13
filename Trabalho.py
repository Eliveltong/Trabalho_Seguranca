import sys


def enumerarSubdominios():
    pass


def enumerarEnderecosIp():
    pass


def enumerarSistemas():
    pass
    
    
def enumerarPortas():
    pass
    

def enumerarServicos():
    pass


# Usar conexao TOR

# Ferramentas a serem usadas:
# API a ser usada: 


def salvarDadosTxt(nome_arquivo, itens):
    if ".txt" not in nome_arquivo:
        nome_arquivo += ".txt"
    with open(nome_arquivo, 'w') as f:
        for i in itens:
            f.write(i + '\n')


def controlePrincipal():
    if "--help" in sys.argv or "-help" in sys.argv:
        print("\nDigite um endereço web para buscar as informações")
        print("Por exemplo teste.com.br\n")
        
    else:
        pass
        
        
controlePrincipal()
