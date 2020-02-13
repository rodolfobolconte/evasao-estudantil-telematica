# Computando _Ensemble Methods_ para Predizer Evasões Estudantis

[![Python](https://img.shields.io/badge/Python-3.6.8-blue)](https://www.python.org) [![Sublime Text 3](https://img.shields.io/badge/Sublime%20Text%203-Build%203176-orange)](https://www.sublimetext.com/3)

## Trabalho de Conclusão de Curso realizado no Período 2019.1

Toda a pesquisa foi realizada do dia 21 de Dezembro de 2018 até 07 de Junho de 2019, contando com um levantamento de referências bibliográficas, seguido da organização dos dados de alunos para serem trabalhados pelos algoritmos e computados os resultados. Para o desenvolvimento da pesquisa foi utilizada a Linguagem de Programação Python, divida em duas partes para a obtenção de Resultados [Parciais](https://github.com/rodolfobolconte/evasao-estudantil-telematica/tree/master/testes-parciais) e [Finais](https://github.com/rodolfobolconte/evasao-estudantil-telematica/tree/master/testes-finais).

Seguem os arquivos da [Apresentação Final](https://github.com/rodolfobolconte/evasao-estudantil-telematica/blob/master/Apresenta%C3%A7%C3%A3o.pdf) e da [Monografia](https://github.com/rodolfobolconte/evasao-estudantil-telematica/blob/master/Monografia.pdf) escrita, ambos hospedados aqui no GitHub.

## Resumo da Pesquisa

Meu Trabalho de Conclusão do Curso Superior de Tecnologia em Telemática pelo IFPB Campus Campina Grande teve o título "Computando Ensemble Methods para Predizer Evasões Estudantis", sendo orientado pela professora Samara Martins e coorientado pelo professor Gustavo Wagner. A seguir um breve resumo sobre o projeto:

A evasão estudantil ocorre em todas as esferas da educação, por diferentes fatores. Há estudos que apontam como causa fatores inerentes ao ensino, dentro da instituição, e outros apontam fatores sociais extra instituição, tais como condição financeira e distância da casa do estudante à instituição, causando problemas tanto sociais quanto econômicos. Do ponto de vista social, as expectativas dos alunos, são diminuídas quando os mesmos desistem dos estudos. Do ponto de vista econômico as instituições sofrem com a baixa expectativa criada pelos altos investimentos por parte dos governos e empresas.

Tendo em vista os danos anteriores apresentados, este trabalho buscou analisar dois Ensemble Methods – técnicas computacionais de Aprendizado de Máquina – para obter e comparar resultados de predição. As estratégias computaram o mesmo algoritmo de classificação, como forma de encontrar aquele que obtenha o melhor desempenho na identificação de possíveis alunos evasores, do Curso Superior de Tecnologia em Telemática do Instituto Federal da Paraíba campus Campina Grande.

Tal trabalho foi realizado a partir dos dados acadêmicos dos alunos utilizando atributos que sejam determinísticos para a previsão de evasão. O conjunto de dados totalizou 720 amostras de alunos, sendo 429 amostras evadidas e 291 amostras não evadidas. Os algoritmos foram testados de 3 formas distintas, com o conjunto de dados sem balanceamento, com balanceamento utilizando o método Oversampling e também com o método Undersampling, que correspondem a técnicas capazes de igualar a quantidade de amostras das classes utilizadas. Cada resultado dos testes foi comparado através dos valores de cinco métricas, sendo elas: Acurácia, Precisão, Sensibilidade, Taxa de Falsa Previsão Positiva e Tempo de Processamento. De forma geral, os testes experimentais mostraram maiores discrepâncias nos tempos de processamento dos algoritmos analisados.