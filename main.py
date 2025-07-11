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
            "stop":self.stopApi
        }
        pass
    def displayPresentation(self):
        print('=== RODANDO PROGRAMA DE PESQUISA ===')
        print("Opções:")
        print("'q': para terminar o progrma.")
        print("'pesquisar': para pesquisar automóveis.")
        print("'gerar': para gerar automóveis.")
        if self.api is not None:
            print("'stop': para parar a api.")

    def displaySearch(self)->str:
        
        print('=== CONSULTA DE AUTOMÓVEIS ===')
        print('Para consultar um automóvel, digite sua busca com o valor após a variável.')
        print('Ex: Me mostre automóveis com nome Buggati do ano 2000')
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
            return 
        else:
            results = self.service.getResults(search)
            print('Resultados:')
            print(results)
        self.displaySearch()
    process = None
    def runApi(self):
        self.process = subprocess.Popen(["uvicorn", "app_controller:app", "--reload"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True)
        print('Api aberta em http://127.0.0.1:8000')
        
    def stopApi(self):
        self.process.terminate()
        self.process = None
        print('Api fechada')
    
    def mainLoop(self):
        self.displayPresentation()
        search = input('Enter: ').lower()
        if search not in self.options.keys():
            return
        else:
            self.options[search]()
        self.mainLoop()
            
    def main(self):
        self.mainLoop()
        print('Finalizando programa.')
runner = Runner()
runner.main()