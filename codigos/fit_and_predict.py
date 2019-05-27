import pandas as pd
#import numpy as np
import time as tm

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import train_test_split

def importancias(atributos, valores):
    for i in range(len(atributos)):
        print(atributos[i], valores[i])


def executar_projeto_evasao_codigo_fonte(teste, atributos):

    #data frame com os dados de telemática
    dados = pd.read_csv('../dados/ifcg_telematica_07a151.csv', delimiter=',')

    print('\n%s -' %(teste))

    dados_atributos = dados[atributos].values
    dados_marcacoes = dados['evadiu'].values


    #treino_atributos, teste_atributos, treino_marcacoes, teste_marcacoes = train_test_split(dados_atributos, dados_marcacoes, test_size=0.3, shuffle=False)
            

    #função para treinar e testar os algoritmos com os dados de treino e teste
    def treinar_e_testar(nome_algoritmo, balanceamento, modelo_algoritmo, dados_atributos, dados_marcacoes):

        arquivo = open('../analise/' + nome_algoritmo + '.csv', 'w')
        arquivo.write('Nome Algoritmo' + ';K-Fold;' + 'Acurácia;' + 'Precisão;' + 'Sensibilidade;' + 'Taxa de Falsos Positivos;' + 'Taxa de Processamento (s);' + 'VN;' + 'FP;' + 'FN;' + 'VP\n')


        metricas = {}

        for n_teste in range(1, 11):
            treino_atributos, teste_atributos, treino_marcacoes, teste_marcacoes = train_test_split(dados_atributos, dados_marcacoes, test_size=0.36, shuffle=True)


            #balanceamento dos dados
            if balanceamento == 1:
                treino_atributos, treino_marcacoes = RandomOverSampler().fit_sample(treino_atributos, treino_marcacoes)
            if balanceamento == 2:
                treino_atributos, treino_marcacoes = RandomUnderSampler().fit_sample(treino_atributos, treino_marcacoes)


            #treino do modelo com dados balanceados
            modelo_algoritmo.fit(treino_atributos, treino_marcacoes)

            #importancia de cada atributo para o modelo
            #importancias(atributos, modelo_algoritmo.feature_importances_)

            #previsão do modelo
            processamento_inicio = tm.time()
            previsoes = modelo_algoritmo.predict(teste_atributos)
            processamento_fim = tm.time()

            matriz_de_confusao = confusion_matrix(teste_marcacoes, previsoes)

            metricas['acuracia'] = accuracy_score(teste_marcacoes, previsoes)
            metricas['precisao'] = precision_score(teste_marcacoes, previsoes)
            metricas['sensibilidade'] = recall_score(teste_marcacoes, previsoes)
            metricas['taxafp'] = matriz_de_confusao[0][1] / (matriz_de_confusao[0][1] + matriz_de_confusao[1][0])
            metricas['processamento'] = processamento_fim - processamento_inicio

            arquivo.write(nome_algoritmo + ';' + str(n_teste) + ';' + str(metricas['acuracia'])[:5].replace('.', ',') + ';' + str(metricas['precisao'])[:5].replace('.', ',') + ';' + str(metricas['sensibilidade'])[:5].replace('.', ',') + ';' + str(metricas['taxafp'])[:5].replace('.', ',') + ';' + str(metricas['processamento'])[:10].replace('.', ',') + ';' + str(matriz_de_confusao[0][0]) + ';' + str(matriz_de_confusao[0][1]) + ';' + str(matriz_de_confusao[1][0]) + ';' + str(matriz_de_confusao[1][1]) + '\n')


        arquivo.write("\nMédias;;" + "=MÉDIA(C2:C11);" + "=MÉDIA(D2:D11);" + "=MÉDIA(E2:E11);" + "=MÉDIA(F2:F11);" + "=MÉDIA(G2:G11);" + "=MÉDIA(H2:H11);" + "=MÉDIA(I2:I11);" + "=MÉDIA(J2:J11);" + "=MÉDIA(K2:K11);")


        print("Fim Modelo")



    treinar_e_testar("RandomForest-100", 0, RandomForestClassifier(n_estimators=100), dados_atributos, dados_marcacoes)

    treinar_e_testar("RandomForest-100-OverSampling", 1, RandomForestClassifier(n_estimators=100), dados_atributos, dados_marcacoes)

    treinar_e_testar("RandomForest-100-UnderSampling", 2, RandomForestClassifier(n_estimators=100), dados_atributos, dados_marcacoes)



    treinar_e_testar("GradientBoosting-100", 0, GradientBoostingClassifier(n_estimators=100), dados_atributos, dados_marcacoes)

    treinar_e_testar("GradientBoosting-100-OverSampling", 1, GradientBoostingClassifier(n_estimators=100), dados_atributos, dados_marcacoes)

    treinar_e_testar("GradientBoosting-100-UnderSampling", 2, GradientBoostingClassifier(n_estimators=100), dados_atributos, dados_marcacoes)