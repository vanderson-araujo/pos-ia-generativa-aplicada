# Classificação com Árvore de Decisão

Este README descreve o fluxo do notebook `notebooks/arvore_decisao.ipynb`, explicando cada passo para treinar e avaliar um modelo de árvore de decisão usando o conjunto de dados balanceado.

## Estrutura do notebook

1. **Importação das bibliotecas**
   - `pandas` para manipulação de dados.
   - `matplotlib` para visualização.
   - `sklearn` para pré-processamento, modelagem e métricas.

2. **Leitura dos dados**
   - O arquivo `data/DS_BALANCEADO.CSV` é carregado em um DataFrame.
   - `df.head()` é exibido para inspecionar o layout dos dados.

3. **Análise da variável alvo**
   - `df["Cancelou"].value_counts()` mostra a distribuição da classe de cancelamento.

4. **Separação entre recursos e alvo**
   - `X` contém todas as colunas exceto `Cancelou`.
   - `y` contém a coluna `Cancelou`.

5. **Identificação de colunas categóricas e numéricas**
   - Colunas de texto são identificadas para serem codificadas.
   - Colunas numéricas são mantidas sem alteração.

6. **Construção do pré-processador**
   - `ColumnTransformer` transforma colunas categóricas com `OneHotEncoder`.
   - Colunas numéricas são passadas sem transformação (`passthrough`).

7. **Criação do pipeline**
   - O pipeline combina o pré-processamento e o classificador `DecisionTreeClassifier`.
   - Desta forma, todas as etapas são executadas juntas durante o treino e a validação.

8. **Validação cruzada estratificada**
   - `StratifiedKFold` com `n_splits=3` é usado para manter a proporção das classes em cada divisão.
   - `cross_val_predict` gera previsões de classes e probabilidades com validação cruzada.

9. **Treinamento final do modelo**
   - O pipeline é ajustado em todo o conjunto de dados com `modelo.fit(X, y)`.

10. **Cálculo das métricas**
    - `roc_auc_score` mede a capacidade de separação entre as classes.
    - `accuracy_score`, `precision_score`, `recall_score`, `f1_score` avaliam a qualidade das previsões.
    - `matthews_corrcoef` fornece uma métrica balanceada para classificação binária.

11. **Matriz de confusão**
    - `ConfusionMatrixDisplay` plota a matriz de confusão para inspecionar verdadeiros positivos/negativos e falsos positivos/negativos.

12. **Visualização da árvore de decisão**
    - `plot_tree` desenha a árvore treinada com nomes das características e classes.
    - Permite interpretar as regras aprendidas pelo modelo.

## Como usar

1. Abra o notebook `notebooks/arvore_decisao.ipynb` em Jupyter Notebook ou JupyterLab.
2. Certifique-se de que o ambiente Python instalado contenha as bibliotecas do `requirements.txt` deste diretório.
3. Execute as células uma a uma, seguindo a sequência:
   - leitura dos dados
   - pré-processamento
   - treinamento e validação
   - avaliação das métricas
   - visualização da árvore

## Dependências

- pandas
- matplotlib
- scikit-learn

> Se preferir, instale as dependências com:
> `pip install -r requirements.txt`

## Observações

- O dataset `DS_BALANCEADO.CSV` foi usado neste notebook para exemplificar um caso de classificação com classes balanceadas.
- Se quiser testar com outro arquivo, basta alterar o caminho em `pd.read_csv()`.
- A árvore de decisão mostra quais recursos são mais importantes para prever se o cliente cancelou ou não.
