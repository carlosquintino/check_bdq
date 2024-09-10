from datetime import datetime

class Output():

    def __init__(self,df_name) -> None:
        self.report = ''
        self.df_name = df_name
        self.now = datetime.now().strftime('%Y-%m-%d %H:%M%S')


    def generate_report(self,expectation) -> None:
        
        if self.report == '':
            self.report += f'Business data quality to dataframe {self.df_name}\n'
            self.report += f'Date and time start validation  {self.now}\n'
            self.report += f'-' * 40 + '\n\n'
        
        self.report += f'Valdation Type : {expectation['expectation_config']['expectation_type']}\n'
        keys = expectation['expectation_config']['kwargs'].keys()

        if 'column' in expectation['expectation_config']['kwargs'].keys():
            self.report += f'Validation column : {expectation['expectation_config']['kwargs']['column']}\n'
        else:
            self.report += f'Dataframe validation\n'

        for key in keys:
            self.report += f'{key} : {expectation['expectation_config']['kwargs'][key]}\n' 
        self.report += f'validation status : {expectation['success']}\n'
        
        keys_result = expectation['result'].keys()
        for key in keys_result:
            self.report += f"{key} : {expectation['result'][key]}\n"
        
        self.report += f'-' * 40 + '\n\n'
    
    def save_report_as_txt(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M%S')
        self.report += f'Date and time final validation {now}\n'
        self.report += f'-' * 40 
        with open(f'{self.df_name}.txt', 'a+') as file:
            file.write(self.report)

