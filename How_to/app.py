##Varrer preços com código
#[Ref](https://www.youtube.com/watch?v=5M-kZf_s6a0)
#[Ref2](https://www.youtube.com/watch?v=ow8514gnajw)
#2. Pesquisar por produto
#3. Extrair o título e preço
#4. Navegar próxima página
#5. Agendar a execução
from selenium import webdriver
import os
#0. Abrir navegador
#ativar no chrome, OS para navegar pelo SO forma dinâmica
#getcwd(dir atual)+os.sep(/separador)+ 'chromedriver.exe'
#driver = webdriver.Chrome(executable_path=os.getcwd()+os.sep+ 'chromedriver')
driver = webdriver.Chrome(executable_path=r"/home/bragatte/Documentos/GitHub/Python_Learning/How_to")
#1. Navegar até o site (url)
#driver.get("https://www.mercadolivre.com")
driver.get("https://www.google.com")
