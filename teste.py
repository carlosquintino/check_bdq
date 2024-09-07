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

ex_gp = Expectations_group(df_ge)

response = ex_gp.completeness('Nome',
                                min_value_col=1,
                                max_value_col=6,
                                max_value_df=10,
                                min_value_df=2)
                                
print(response)