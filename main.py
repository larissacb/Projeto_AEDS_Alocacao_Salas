from Turma import Turma
menu=True
aux=list()
turmas=list()

def menu_inicial():
    print("==== Menu ====")
    print("1 - Imprimir turmas")
    print("2 - Ler um novo arquivo de demanda de salas")
    print("0 - Sair")
    op = int(input())
    return op

def abre_arq(arq):
    fhand = open(arq)
    for linha in fhand:
        linha = linha.rstrip()
        aux = linha.split()  # quebro a linha em varias strings
        curso = aux[0]
        disciplina = aux[1]
        professor = aux[2]
        num_alunos = int(aux[3])
        turno = aux[4]
        a = Turma(curso, disciplina, professor, num_alunos, turno)  # criando um objeto
        #return a
        turmas.append(a)  # salvando o objeto criado em uma lista

#ler arquivo inicial
fhand=open("EEL.txt") #abrindo um arquivo com as turmas reservadas para eng eletrica na funcao leitura
for linha in fhand:
    linha = linha.rstrip()
    aux = linha.split() #quebro a linha em varias strings
    curso = aux[0]
    disciplina = aux[1]
    professor = aux[2]
    num_alunos = int(aux[3])
    turno = aux[4]
    a = Turma(curso, disciplina, professor, num_alunos, turno) #criando um objeto
    turmas.append(a) #salvando o objeto criado em uma lista

while (menu==True):
    op=menu_inicial()
    if (op==1):
        for i in range(len(turmas)):  # percorrendo a lista com as turmas
            b = turmas[i]
            b.imprimir_inf()
    elif (op==0):
        break
    elif (op==2):
        arq=input("Informe o nome do arquivo:")
        abre_arq(arq)
        #turmas.append(a)
    else:
        print("Opcao invalida!")
#salvar na lista de classes
#imprimir os dados salvos
