from expectations.expectations import Coluns_expectations

class Expectations_group(Coluns_expectations):
    def __init__(self,df,df_name):
        self.df = df
        self.df_name = df_name
        
        super().__init__(self.df,df_name=self.df_name)
    
    def completeness(self,col,max_value,min_value):
        super().not_null(col_name=col)

        # super().value_btw(
        #         col_name=col,
        #         max_value=max_value,
        #         min_value=min_value)
        
        super().df_count_btw(max_value=max_value,
                             min_value=min_value
                             )
                
        