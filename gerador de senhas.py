import string
import random
import os
from time import sleep

#mensagem inicial do programa
def disclaimer():
    #funcao para limpar a tela do console
    limpaTela = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    print('===============================================================================')
    print('Esse programa gera uma senha aleatoria de quantos digitos quiser.\n')
    print('A senha será salva em um arquivo chamado "SENHAS.txt" na sua área de trabalho(NAO MOVA O ARQUIVO PARA OUTRO LUGAR).\n')
    print('O codigo para este programa é aberto, sinta-se livre para edita-lo como desejar.\n')
    print('LEIA O ARQUIVO README.md')
    print('Código original por: https://github.com/Joaogmbd/ :)\n')
    print('===============================================================================')

    #timer para ler a mensagem inicial
    sleep(8)
    limpaTela()

def geraSenha(c, l):
	# randomiza caracteres da lista
	random.shuffle(c)
	
	#recebe caracteres aleatorios da lista e monta a nova senha
	password = []
	for i in range(l):
		password.append(random.choice(c))

    # randomiza senha
	random.shuffle(password)

    #a funcao retorna a senha
	return "".join(password)

disclaimer()

id = str(input("Digite um identificador para a senha: "))
l = int(input("Qual será o tamanho da senha?: "))
c = list(string.ascii_letters + string.digits + "!@#$%&*")
senha = geraSenha(c,l)

#gerando o caminho para o arquivo onde as senhas sao salvas
def path():
    user = os.getlogin()
    path = "C:/Users/"+ user + "/Desktop/Senhas.txt"
    return path

#salvando a senha no arquivo
def save():

    #abrindo arquivo no modo append
    f = open(path(), 'a')

    #adicionando senha ao arquivo + formatação
    f.write("\n\n"+ id + ":\n"+ senha)
    f.close()

print("A senha gerada foi: " + senha)
save()
