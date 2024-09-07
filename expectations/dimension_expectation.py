from expectations.expectations import Coluns_expectations

class Expectations_group(Coluns_expectations):
    def __init__(self,df):
        self.df = df
        
        super().__init__(self.df)
    
    def completeness(self,col,max_value_col,min_value_col,max_value_df,min_value_df):
        super().not_null(col_name=col)

        super().value_btw(
                col_name=col,
                max_value=max_value_col,
                min_value=min_value_col)
        
        super().df_count_btw(max_value=max_value_df,
                             min_value=min_value_df
                             )
        
        