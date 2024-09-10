import great_expectations as ge
from output.output import Output


class Coluns_expectations(Output):
    def __init__(self,df,df_name):
        self.df = df
        super().__init__(df_name)


    def not_null(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_not_be_null(
                                col_name
                                )
        super().generate_report(self.response)
    

    def unique_vals(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_be_unique(
                                col_name
                                )
        super().generate_report(self.response)

    #Falta adicionar mascara
    def date_mask_equal(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_match_strftime_format(
                                col_name
                                )
        super().generate_report(self.response)


    def value_btw(self,col_name,min_value,max_value):
        self.response = self. \
                            df. \
                            expect_column_value_lengths_to_be_between(
                                column=col_name,
                                min_value=min_value,
                                max_value=max_value)
        super().generate_report(self.response)
    

    def df_count_btw(self,min_value,max_value):
        self.response = self. \
                            df. \
                            expect_table_row_count_to_be_between(
                                min_value,
                                max_value
                            )
        super().generate_report(self.response)

        