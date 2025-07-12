from init.scripts.generate_mocks import createMocks,names,colors,doorNumbers,prices,driverNames,sizes,weights,wheelNumbers,years,brands
from services.service import Service
import subprocess
class Runner:
    def __init__(self):
        self.api = None
        self.service = Service()
        self.options = {
            "pesquisar":self.displaySearch,
            "gerar":createMocks,
            "api":self.runApi,
            "q":self.quit,
            "stop":self.stopApi
        }
        self.flag = False
        pass
    def quit(self)->bool:
        return True
    def displayPresentation(self):
        print('=== RODANDO PROGRAMA DE PESQUISA ===')
        print("Opções:")
        print("'q': para terminar o progrma.")
        print("'pesquisar': para pesquisar automóveis.")
        print("'gerar': para gerar automóveis.")
        print("'api': para rodar a api.")
        print("'stop': para parar a api.")

    def displaySearch(self)->bool:
        
        print('=== CONSULTA DE AUTOMÓVEIS ===')
        print('Para consultar um automóvel, digite sua busca com o valor após a variável.')
        print('Ex: Me mostre automóveis com marca Bugatti do ano 2020')
        print('Variáveis inclusas nos mocks:')
        print(f'Nomes: {','.join(names)}')
        print(f'Cores: {','.join(colors)}')
        print(f'Número de Portas: {','.join(map(str, doorNumbers))}')
        print(f'Preços: {','.join(map(str, prices))}')
        print(f'Nome do(a) Motorista: {','.join(driverNames)}')
        print(f'Tamanho: {','.join(map(str, sizes))}')
        print(f'Peso: {','.join(map(str, weights))}')
        print(f'Número de Rodas: {','.join(map(str, wheelNumbers))}')
        print(f'Anos: {','.join(map(str, years))}')
        print(f'Marcas: {','.join(brands)}')
        print('=== ===================== ===')
        search = input('Pesquisar: ').lower()
        if search == 'q':
            return False
        else:
            results = self.service.getResults(search)
            print('Resultados:')
            print(results)
        self.displaySearch()
    
    def runApi(self)->bool:
        self.process = subprocess.Popen(["uvicorn", "app_controller:app", "--reload"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True)
        print('Api aberta em http://127.0.0.1:8000')
        return False
        
    def stopApi(self)->bool:
        if self.process:
            self.process.terminate()
            self.process = None
            print('Api fechada')
        return False
    
    def mainLoop(self):
        self.displayPresentation()
        search = input('Enter: ').lower()
        if search in self.options.keys():
            try:
                self.flag = self.options[search]()
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
        if self.flag:
            return 
        
        self.mainLoop()
            
    def main(self):
        self.mainLoop()
        print('Finalizando programa.')
        
runner = Runner()
runner.main()
