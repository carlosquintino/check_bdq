from expectations.dimension_expectation import Expectations_group
import great_expectations as ge
import pandas as pd


data = {
    'Nome': ['Daniel', 'Maria', 'João', 'Ana'],
    'Idade': [29, 35, 22, 28],
    'Cidade': ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Salvador']
}

# Criando o DataFrame
df = pd.DataFrame(data)

df_ge = ge.from_pandas(df)

response = df_ge.expect_column_values_to_not_be_null('Nome')
                                
print(type(response['success']))