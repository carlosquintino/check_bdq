import great_expectations as ge
import pandas as pd


class Coluns_expectations():
    def __init__(self,df):
        self.df = df
        pass

    def not_null(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_not_be_null(
                                col_name
                                )
    

    def unique_vals(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_be_unique(
                                col_name
                                )

    #Falta adicionar mascara
    def date_mask_equal(self,col_name):
        self.response = self. \
                         df. \
                            expect_column_values_to_match_strftime_format(
                                col_name
                                )


    def value_btw(self,col_name,min_value,max_value):
        self.response = self. \
                            df. \
                            expect_column_value_lengths_to_be_between(
                                column=col_name,
                                min_value=min_value,
                                max_value=max_value)
    

    def df_count_btw(self,min_value,max_value):
        self.response = self. \
                            df. \
                            expect_table_row_count_to_be_between(
                                min_value,
                                max_value
                            )

        