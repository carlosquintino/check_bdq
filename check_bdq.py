from expectations.dimension_expectation import Expectations_group
import great_expectations as ge
# from expectations.expectations import Coluns_expectations

class Check_bdq(Expectations_group):

    def __init__(self, df,parameters,verbose=False):
        
        self.df = df
        self.parameters = parameters
        self.keys = parameters.keys()
        self.type_df = parameters['type_df']
        self.verbose = verbose

    def conver_df(self):
        if self.type_df == 'pandas':
            self.df_ge = ge.from_pandas(self.df)
        
        super().__init__(self.df_ge)
    
    def kickOff(self):
        
        self.type_df()

        for key in self.keys:

            if 'group' in key.keys():
                group = key['group']
                if group == 'completeness':

                    super().completeness(key,
                                        max_value_col=key['max_val'],
                                        min_value_col=key['min_val'],
                                        max_value_df=key['max_val'],
                                        min_value_df=key['min_val'])

            else:
                validations = key['validations']
                for validation in validations:
                    if validation not in 'value_btw,date_mask_equal,df_count_btw':
                        pass
                    else:
                        
                        expec = f"super().not_null({key})"
                        eval(expec)
