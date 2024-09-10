from expectations.dimension_expectation import Expectations_group
from exception.exceptions import *
import great_expectations as ge


class Check_bdq(Expectations_group):

    def __init__(self, df,parameters,report=False,df_name='',verbose=False):
        
        self.df_name = df_name
        if report and self.df_name == '':
            raise InvalidPathException(df_name)
        self.df = df
        self.parameters = parameters
        
        self.type_df = parameters['df_type']
        self.parameters.pop('df_type')
        self.keys = self.parameters.keys()
        self.verbose = verbose

    def convert_df(self):
        if self.type_df == 'pandas':
            self.df_ge = ge.from_pandas(self.df)
        if self.type_df == 'spark':
            self.df_ge = ge.from_pandas(self.df.to_pandas())
        
        super().__init__(self.df_ge,self.df_name)
    
    def kickOff(self):
        
        self.convert_df()

        for key in self.keys:

            exp_col = self.parameters[key]
            if 'dimension' in exp_col:
                group = exp_col['dimension']
                if group == 'completeness':

                    super().completeness(key,
                                        max_value=exp_col['max_val'],
                                        min_value=exp_col['min_val'])
                    if self.report:
                        super().save_report_as_txt()

            else:
                validations = exp_col['validations']
                for validation in validations:
                    if validation not in 'value_btw,date_mask_equal,df_count_btw':
                        pass
                    else:
                        
                        expec = f"super().{validation}({key})"
                        eval(expec)
