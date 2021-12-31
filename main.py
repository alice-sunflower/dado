#Criar um programa que gire um dado de 6 lados quantas vezes o usuário desejar

#Importar a função giradado criado na pasta "módulos"
from modulos import giradado

#Começar o programa girando um dado
giradado()

#Loop que tem uma opção de rolar mais um dado ou não que pode ser quebrado pelo usuário
continuar = True

while continuar:
    opcao = str(input('Deseja rolar mais um dado? Digite [S] para SIM e [N] para NÃO ')).upper()
    if opcao not in 'SN':
        print('Ocorreu um erro. Digite S para SIM e N para NÃO.')
    if opcao in 'S':
        giradado()
        continue
    elif opcao in 'N':
        break

print('Volte sempre!')
