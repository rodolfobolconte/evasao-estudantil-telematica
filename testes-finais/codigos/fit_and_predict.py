import pandas as pd
import time as tm

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

def importancias(atributos, valores):
    for i in range(len(atributos)):
        print(atributos[i], valores[i])

def plotar_arvores(modelo_algoritmo, atributos):
    dot_data = StringIO()
    export_graphviz(modelo_algoritmo.estimators_[99], out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True, feature_names=atributos)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png()) ; exit()

#função para dividir o conjunto de dados com o método Bootstrap com reposição para treino e teste
def dividir_conjunto_bootstrap(dados, atributos):
    #calculando a quantidade de valores para 63,2% para treino e 36,8% para teste
    qtd_treino = round(len(dados) * 0.632)
    qtd_teste = round(len(dados) * 0.368)

    #dividindo o Conjunto de Dados com reposição
    treino = resample(dados, n_samples=qtd_treino, replace=True)
    teste = resample(dados, n_samples=qtd_teste, replace=True)

    #pegando somente os atributos utilizados na classificação, para treino
    treino_atributos = treino[atributos].values
    treino_marcacoes = treino['evadiu'].values

    #pegando somente os atributos utilizados na classificação, para teste
    teste_atributos = teste[atributos].values
    teste_marcacoes = teste['evadiu'].values

    return treino_atributos, treino_marcacoes, teste_atributos, teste_marcacoes


#função para treinar e testar os algoritmos com os dados de treino e teste
def treinar_e_testar(nome_algoritmo, balanceamento, modelo_algoritmo, dados, atributos):

    #criando arquivo dos resultados
    arquivo = open('../resultados/' + nome_algoritmo + '.csv', 'w')
    #escrevendo cabeçalho no arquivo
    arquivo.write('Nome Algoritmo;' + 'Execução;' + 'Acurácia;' + 'Precisão;' + 'Sensibilidade;' + 'Taxa de Falsa Previsão Positiva;' + 'Tempo de Processamento (s);' + 'VN;' + 'FP;' + 'FN;' + 'VP' + '\n')


    metricas = {}

    for n_teste in range(1, 11):

        treino_atributos, treino_marcacoes, teste_atributos, teste_marcacoes = dividir_conjunto_bootstrap(dados, atributos)

        #balanceamento dos dados
        if balanceamento == 1:
            treino_atributos, treino_marcacoes = RandomOverSampler().fit_sample(treino_atributos, treino_marcacoes)
        if balanceamento == 2:
            treino_atributos, treino_marcacoes = RandomUnderSampler().fit_sample(treino_atributos, treino_marcacoes)


        #treino do modelo com dados balanceados
        modelo_algoritmo.fit(treino_atributos, treino_marcacoes)

        #plotar o esquema das árvores criadas
        #plotar_arvores(modelo_algoritmo, atributos)
        
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

        #escrevendo os valores de cada métrica das execuções no arquivo
        arquivo.write(nome_algoritmo + ';' + str(n_teste) + ';' + str(metricas['acuracia'])[:5].replace('.', ',') + ';' + str(metricas['precisao'])[:5].replace('.', ',') + ';' + str(metricas['sensibilidade'])[:5].replace('.', ',') + ';' + str(metricas['taxafp'])[:5].replace('.', ',') + ';' + str(metricas['processamento'])[:10].replace('.', ',') + ';' + str(matriz_de_confusao[0][0]) + ';' + str(matriz_de_confusao[0][1]) + ';' + str(matriz_de_confusao[1][0]) + ';' + str(matriz_de_confusao[1][1]) + '\n')


    #escrevendo a média das métricas no arquivo
    arquivo.write("\nMédias;;" + "=MÉDIA(C2:C11);" + "=MÉDIA(D2:D11);" + "=MÉDIA(E2:E11);" + "=MÉDIA(F2:F11);" + "=MÉDIA(G2:G11);" + "=MÉDIA(H2:H11);" + "=MÉDIA(I2:I11);" + "=MÉDIA(J2:J11);" + "=MÉDIA(K2:K11);")

    print("Fim:", nome_algoritmo)


def executar_projeto_evasao_codigo_fonte(teste, atributos):

    #data frame com os dados de telemática
    dados = pd.read_csv('../dados/ifcg_telematica_07a151.csv', delimiter=';')

    print('\n%s -' %(teste))

    #criando os ensemble methods
    modelo_floresta_aleatoria = RandomForestClassifier(n_estimators=100, bootstrap=True, max_depth=3, max_features=9, max_leaf_nodes=8)
    modelo_aumento_gradiente = GradientBoostingClassifier(n_estimators=100, max_depth=3, max_features=9, max_leaf_nodes=8, loss='deviance', learning_rate=0.2, subsample=1)

    #executando os ensemble methods
    treinar_e_testar("Teste1-FlorestaAleatória-100", 0, modelo_floresta_aleatoria, dados, atributos)
    treinar_e_testar("Teste2-AumentoDeGradiente-100", 0, modelo_aumento_gradiente, dados, atributos)

    treinar_e_testar("Teste3-FlorestaAleatória-100-OverSampling", 1, modelo_floresta_aleatoria, dados, atributos)
    treinar_e_testar("Teste4-AumentoDeGradiente-100-OverSampling", 1, modelo_aumento_gradiente, dados, atributos)

    treinar_e_testar("Teste5-FlorestaAleatória-100-UnderSampling", 2, modelo_floresta_aleatoria, dados, atributos)
    treinar_e_testar("Teste6-AumentoDeGradiente-100-UnderSampling", 2, modelo_aumento_gradiente, dados, atributos)