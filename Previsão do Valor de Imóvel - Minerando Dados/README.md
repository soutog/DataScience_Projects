# Previsão do Valor do Imóvel

### Preços dos imóveis na cidade de Boston EUA
- Baseado nas características do imóvel o objetivo é estimar o preço do imóvel. 
- Entregar o melhor valor de venda baseado em seus atributos. 

### Conhecendo as colunas da base de dados:

**`CRIM`**: Taxa de criminalidade per capita por regiao.

**`ZN`**: Proporção de terrenos residenciais divididos por lotes com mais de 25.000 pés quadrados.

**`INDUS`**: Essa é a proporção de hectares de negócios não comerciais por regiao.

**`CHAS`**: variável fictícia Charles River (= 1 se o trecho limita o rio; 0 caso contrário)

**`NOX`**: concentração de óxido nítrico (partes por 10 milhões)

**`RM`**: Número médio de quartos entre as casas do bairro

**`Age`**: proporção de unidades ocupadas pelos proprietários construídas antes de 1940

**`DIS`**: distâncias ponderadas para cinco centros de emprego em Boston

**`RAD`**: Índice de acessibilidade às rodovias radiais

**`IMPOSTO`**: taxa do imposto sobre a propriedade de valor total por US $ 10.000

**`B`**: 1000 (Bk - 0,63) ², onde Bk é a proporção de pessoas de descendência afro-americana por regiao

**`PTRATIO`**: Bairros com maior proporção de alunos para professores (maior valor de 'PTRATIO')

**`LSTAT`**: porcentagem de status mais baixo da população

**`MEDV`**: valor médio de casas ocupadas pelos proprietários em US$ 1000

### Pandas Profilling 
- Essa ferramenta foi usada para análise dos dados. Alternativamente, também foi usada uma análise exploratória manual

### Arquitetura de Solução
- Usuários acessam a aplicação, que por sua vez acessa a um banco de dados e um modelo. 

### Ferramentas utilizadas para desenvolvimento do projeto.
- Python
- Pandas
- Numpy
- Scikit-learn
- Jupyter Notebook
- Matplotlib

### Criação do Data app

- Biblioteca Streamlit (https://www.streamlit.io/) para a construção de aplicações que trabalham com dados, de forma rápida e objetiva. Ferramenta para criação de aplicações web sem a utilização de APIs como Flask ou Django. 

**Para executar o app com o Streamlit**
-`na pasta data-app:` streamlit run app.py
