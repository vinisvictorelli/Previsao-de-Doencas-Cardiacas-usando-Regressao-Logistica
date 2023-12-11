# Previsao-de-Doencas-Cardiacas-usando-Regressao-Logistica
Este projeto visa explorar e prever doenças cardíacas com base em dados clínicos. A aplicação é construída usando o framework Streamlit para criar uma interface interativa que oferece visualizações detalhadas sobre fatores de risco e uma funcionalidade de previsão usando um modelo de Regressão Logística.

##Estrutura do Projeto
O projeto possui dois principais componentes:

###Dashboard Principal
O Dashboard Principal oferece uma visão geral dos fatores relacionados a doenças cardíacas. Ele inclui gráficos interativos que mostram a relação entre idade e frequência cardíaca máxima, a distribuição de idade para casos de doença cardíaca, a distribuição de frequência cardíaca máxima para pacientes com/sem doença cardíaca, a distribuição de pacientes por sexo, a proporção de pacientes com/sem doença cardíaca e a relação entre idade e colesterol.

##Previsão de Doenças Cardíacas
O Módulo de Previsão utiliza um modelo de Regressão Logística para prever a ocorrência de doenças cardíacas com base nos dados fornecidos. Após treinar o modelo, ele exibe métricas de desempenho, como acurácia e uma matriz de confusão. Além disso, são apresentados gráficos, incluindo uma comparação real vs. previsto em um gráfico de barras empilhadas e uma matriz de confusão para análise preditiva.

###Como Executar o Projeto
Para executar o projeto em sua máquina local, siga estas etapas:
Clone este repositório:
```python
# Seu código Python aqui
import streamlit as st
import pandas as pd
# ... resto do seu código ...
