from expectations.expectations import Coluns_expectations

class Expectations_group(Coluns_expectations):
    def __init__(self,df,group):
        self.df = df
        self.group = group
        super().__init__(self.df)
    
    def completeness(self,col):
        super().not_null(col_name=col)
        response = self.response
        return response