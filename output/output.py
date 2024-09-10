from datetime import datetime

class Output():

    def __init__(self,df_name) -> None:
        self.report = ''
        self.df_name = df_name
        self.now = datetime.now().strftime('%Y-%m-%d %H:%M%S')


    def generate_report(self,expectation) -> None:
        if self.report == '':
            self.report += f'Relátorio de qualidade de dados para o dataframe {self.df_name}\n'
            self.report += f'Data e horario da execução {self.now}\n'
            self.report += f'-' * 40 + '\n\n'
        
        self.report += f'Tipo da validação : {expectation['expectation_config']['expectation_type']}\n'
        self.report += f'Coluna usada para o teste : {expectation['expectation_config']['column']}\n'
        self.report += f'Status da validação : {expectation['success']}\n'
        if not expectation['success']:
            self.report += f'Exemplo de valores que falharam na validação : {expectation['result']['partial_unexpected_list']}\n'
            self.report += f'Quantidade de valores que falharam na validação : {expectation['result']['unexpected_count']}\n'
        
        self.report += f'-' * 40 + '\n\n'
    
    def save_report_as_txt(self):

        with open(f'{self.df_name}.txt', 'a+') as file:
            file.write(self.report)

