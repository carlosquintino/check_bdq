from check_bdq import Check_bdq
import great_expectations as ge
import pandas as pd


data = {
    'Nome': ['Daniel', 'Maria', 'João', 'Ana'],
    'Idade': [29, 35, 22, 28],
    'Cidade': ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Salvador']
}

# Criando o DataFrame
df = pd.DataFrame(data)


parameters = {"df_type":"pandas","Nome":{"dimension":"completeness","max_val":5,"min_val":2}}

cck_bdq = Check_bdq(df,parameters,report=True,df_name='teste_1')
cck_bdq.kickOff()