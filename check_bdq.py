from expectations.dimension_expectation import Expectations_group
from exception.exceptions import *
import great_expectations as ge


class Check_bdq(Expectations_group):

    def __init__(self, df,parameters,report=False,df_name='',verbose=False):
        
        if report and df_name == '':
            raise InvalidPathException(df_name)
        self.df = df
        self.parameters = parameters
        self.keys = parameters.keys()
        self.type_df = parameters['type_df']
        self.verbose = verbose

    def convert_df(self):
        if self.type_df == 'pandas':
            self.df_ge = ge.from_pandas(self.df)
        if self.type_df == 'spark':
            self.df_ge = ge.from_pandas(self.df.to_pandas())
        
        super().__init__(self.df_ge)
    
    def kickOff(self):
        
        self.convert_df()

        for key in self.keys:

            if 'group' in key.keys():
                group = key['group']
                if group == 'completeness':

                    super().completeness(key,
                                        max_value=key['max_val'],
                                        min_value=key['min_val'])

            else:
                validations = key['validations']
                for validation in validations:
                    if validation not in 'value_btw,date_mask_equal,df_count_btw':
                        pass
                    else:
                        
                        expec = f"super().{validation}({key})"
                        eval(expec)
