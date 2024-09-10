from expectations.expectations import Coluns_expectations

class Expectations_group(Coluns_expectations):
    def __init__(self,df):
        self.df = df
        
        super().__init__(self.df)
    
    def completeness(self,col,max_value,min_value):
        super().not_null(col_name=col)

        super().value_btw(
                col_name=col,
                max_value=max_value,
                min_value=min_value)
        
        # super().df_count_btw(max_value=max_value,
        #                      min_value=min_value
        #                      )
                
        