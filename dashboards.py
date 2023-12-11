import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Previsão de doenças do coração", page_icon=":bar_chart:",layout="wide")
st.sidebar.title("Menu")
opcao_selecionada = st.sidebar.radio("Selecione uma opção", ["Dashboard principal", "Previsão de doenças cardíacas"])

def dashboard_principal():
    st.title("Fatores de doenças cardíacas")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    df = pd.read_csv('heart_cleveland_upload.csv')

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    # Gráfico de dispersão interativo
    scatter_fig = px.scatter(df, x='age', y='thalach', color='condition', title='Relação entre Idade e Frequência Cardíaca Máxima',
                            labels={'age': 'Idade', 'condition': 'Frequência Cardíaca Máxima','thalach' : 'Frequencia cardiaca'},
                            hover_data=['chol', 'trestbps'])
    scatter_fig.update_layout(
        showlegend=True
    )

    # Histograma interativo
    histogram_fig = px.histogram(df, x='age', color='condition', title='Distribuição de Idade para Doença Cardíaca',
                                labels={'age': 'Idade', 'count': 'Contagem'}, marginal='rug')
    histogram_fig.update_layout(showlegend=True)

    # Boxplot interativo
    boxplot_fig = px.box(df, x='condition', y='thalach', color='condition', title='Distribuição de Frequência Cardíaca Máxima para Pacientes com/sem Doença Cardíaca',
                        labels={'target': 'Doença Cardíaca', 'thalach': 'Frequência Cardíaca Máxima'})
    boxplot_fig.update_layout(showlegend=True)

    # Gráfico de Barras Interativo para Sexo
    bar_fig_sex = px.histogram(df, x='sex', color='condition', title='Distribuição de Pacientes por Sexo',
                        labels={'sex': 'Sexo', 'condition': 'Doença Cardíaca'}, 
                        category_orders={'sex': [0, 1]}, 
                        height=400)
    bar_fig_sex.update_layout(showlegend=True)

    # Gráfico de Pizza Interativo para Doença Cardíaca
    pie_fig_target = px.pie(df, names='condition', title='Proporção de Pacientes com/sem Doença Cardíaca',
                            labels={'condition': 'Doença Cardíaca'},
                            color_discrete_map={0: 'lightblue', 1: 'salmon'})
    pie_fig_target.update_layout(showlegend=True)

    # Gráfico de Área Interativo para Idade e Colesterol
    area_fig = px.area(df, x='age', y='chol', color='condition', title='Relação entre Idade e Colesterol',
                    labels={'age': 'Idade', 'chol': 'Colesterol'},
                    line_shape='linear')
    area_fig.update_layout(showlegend=True)

    col1.plotly_chart(scatter_fig, use_container_width=True)
    col2.plotly_chart(histogram_fig, use_container_width=True)
    col3.plotly_chart(boxplot_fig, use_container_width=True)
    col4.plotly_chart(bar_fig_sex, use_container_width=True)
    col5.plotly_chart(pie_fig_target, use_container_width=True)
    col6.plotly_chart(area_fig, use_container_width=True)

def previsao():
    st.title("Previsão de doenças cardíacas")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    df = pd.read_csv('heart_cleveland_upload.csv')
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    import plotly.figure_factory as ff


    # Pré-processamento do conjunto de dados
    X = df.drop('condition', axis=1)
    y = df['condition']

    # Dividir o conjunto de dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Padronizar as features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Treinar o modelo de Regressão Logística
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avaliar o desempenho do modelo
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Exibir métricas de desempenho
    st.write(f'Acurácia do Modelo: {accuracy:.2%}')
    st.write('Matriz de Confusão:')
    st.write(conf_matrix)

    # Criar um DataFrame para análise preditiva
    analysis_df = pd.DataFrame({'Real': y_test, 'Previsto': y_pred})

        # Gráfico de Barras Empilhadas
    stacked_bar_fig = px.histogram(analysis_df, x='Real', color='Previsto', color_discrete_map={0: 'lightblue', 1: 'salmon'},
                                title='Comparação Real vs. Previsto - Gráfico de Barras Empilhadas',
                                labels={'Real': 'Real', 'Previsto': 'Previsto'},
                                category_orders={'Real': [0, 1], 'Previsto': [0, 1]},
                                marginal='rug', barmode='stack')
    stacked_bar_fig.update_layout(xaxis=dict(title='Doença Cardíaca', tickmode='array', tickvals=[0, 1], ticktext=['Sem', 'Com']),
                                yaxis=dict(title='Contagem'))

    # Gráfico de Matriz de Confusão
    matrix_fig = ff.create_annotated_heatmap(conf_matrix, x=['Sem Doença', 'Com Doença'], y=['Sem Doença', 'Com Doença'],
                                            colorscale='blues', showscale=True)
    matrix_fig.update_layout(title='Matriz de Confusão - Análise Preditiva',
                            xaxis=dict(title='Previsto'),
                            yaxis=dict(title='Real'))

    # Exibir gráficos no Streamlit
    st.plotly_chart(stacked_bar_fig, use_container_width=True)
    st.plotly_chart(matrix_fig, use_container_width=True)

# Lógica para alternar entre dashboards
if opcao_selecionada == "Dashboard principal":
    dashboard_principal()
elif opcao_selecionada == "Previsão de doenças cardíacas":
    previsao()