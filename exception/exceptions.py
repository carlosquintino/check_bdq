class InvalidPathException(Exception):

    def __init__(self, df_name) -> None:
        self.df_name = df_name
        self.message = f'To generate a report you need pass a valid data frame name, the data frame name {self.df_name} is not valid'
        super().__init__(self.message)