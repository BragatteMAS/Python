'''
100daysofcode
"How to display all columns pandas"
create by  @bragatte ^202101051654 
Day 1
[Ref](https://towardsdatascience.com/10-python-skills-419e5e4c4d66)
'''
import pandas as pd
import requests

url="https://opendatasus.saude.gov.br/pt_BR/dataset/a2cfca72-d8e8-4878-b7f5-d97535a991d5/resource/77d8d14a-cf8c-4209-bed3-3b63ed63fd4f/download/arquivo_geral.csv"
s=requests.get(url).content
covid=pd.read_csv(io.StringIO(s.decode('utf-8')))
pd.set_option('max_colwidth', 1000) # Show up to 1000 characters within each cell
pd.set_option('max_rows', 20) # Show up to 20 dataframe rows
pd.set_option('max_columns', 1000) # Show up to 1000 columns

covid.head()
