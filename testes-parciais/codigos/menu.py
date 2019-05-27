from fit_and_predict import *

#Todos os testes que podem ser feitos no momento
testes = ['1- Todos os Atributos',
          '2- porcentagem_curso, cre, qtd_periodos_cursados, qtd_disciplinas_curso',
          '3- qtd_disciplinas_curso, qtd_disciplinas_aprovadas, qtd_disciplinas_reprovadas_nota, qtd_disciplinas_reprovadas_falta, qtd_disciplinas_canceladas',
          '4- cre, qtd_disciplinas_aprovadas, qtd_disciplinas_reprovadas_nota, qtd_disciplinas_reprovadas_falta',
          '5- porcentagem_curso, cre, qtd_periodos_cursados, qtd_disciplinas_aprovadas, qtd_disciplinas_trancadas',
          '6- porcentagem_curso, cre, qtd_disciplinas_curso, qtd_disciplinas_aprovadas, qtd_disciplinas_trancadas',
          '7- cre, qtd_disciplinas_curso, qtd_disciplinas_aprovadas, qtd_disciplinas_canceladas, qtd_disciplinas_trancadas',
          '8- qtd_periodos_cursados, qtd_disciplinas_aprovadas, qtd_disciplinas_reprovadas_nota, qtd_disciplinas_reprovadas_falta, qtd_disciplinas_canceladas, qtd_disciplinas_trancadas',
          '9- cre, qtd_periodos_cursados, qtd_disciplinas_curso, qtd_disciplinas_aprovadas, qtd_disciplinas_canceladas, qtd_disciplinas_trancadas',
          '10- porcentagem_curso, qtd_periodos_cursados, qtd_disciplinas_aprovadas, qtd_disciplinas_reprovadas_nota, qtd_disciplinas_trancadas'
          ]

while True:
    print('Menu de Testes:\n\t0- Sair')
    for i in testes:
        print('\t' + i)

    teste = int(input('\nEscolha um Tipo de Teste de Acordo com Atributos para Executar: '))

    #If para mandar os atributos especificos de cada teste
    if not teste:
        break
    elif teste == 1:
        atributos = ['porcentagem_curso', 'cre', 'qtd_periodos_cursados', 'qtd_disciplinas_curso', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_reprovadas_nota', 'qtd_disciplinas_reprovadas_falta', 'qtd_disciplinas_canceladas', 'qtd_disciplinas_trancadas']
    elif teste == 2:
        atributos = ['porcentagem_curso', 'cre', 'qtd_periodos_cursados', 'qtd_disciplinas_curso']
    elif teste == 3:
        atributos = ['qtd_disciplinas_curso', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_reprovadas_nota', 'qtd_disciplinas_reprovadas_falta', 'qtd_disciplinas_canceladas']
    elif teste == 4:
        atributos = ['cre', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_reprovadas_nota', 'qtd_disciplinas_reprovadas_falta']
    elif teste == 5:
        atributos = ['porcentagem_curso', 'cre', 'qtd_periodos_cursados', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_trancadas']
    elif teste == 6:
        atributos = ['porcentagem_curso', 'cre', 'qtd_disciplinas_curso', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_trancadas']
    elif teste == 7:
        atributos = ['cre', 'qtd_disciplinas_curso', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_canceladas', 'qtd_disciplinas_trancadas']
    elif teste == 8:
        atributos = ['qtd_periodos_cursados', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_reprovadas_nota','qtd_disciplinas_reprovadas_falta', 'qtd_disciplinas_canceladas', 'qtd_disciplinas_trancadas']
    elif teste == 9:
        atributos = ['cre', 'qtd_periodos_cursados', 'qtd_disciplinas_curso', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_canceladas', 'qtd_disciplinas_trancadas']
    elif teste == 10:
        atributos = ['porcentagem_curso', 'qtd_periodos_cursados', 'qtd_disciplinas_aprovadas', 'qtd_disciplinas_reprovadas_nota', 'qtd_disciplinas_trancadas']

    executar_projeto_evasao_codigo_fonte(testes[teste - 1], atributos)
    pausar = input("\nDigite algo para continuar: ")

    print('\n\n')