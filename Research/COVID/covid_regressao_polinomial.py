import numpy as np
import pandas as pd

from numpy import polyfit
from sklearn.metrics import mean_squared_error as mse

import warnings
warnings.simplefilter("ignore")


def regressao_polinomial(path, date, regiao, estado, municipio, tempo=60):
    
    # função para obter os dados e realizar a predição
    
    # path: diretório onde estão os dados. OBS.: não digitar o nome do arquivo, mas incluir a pasta.
                                         # OBS.2: substituir '/' por '\'
                                         
    # date: data que se deseja obter os dados, seguindo o exemplo: 11jun2021
    
    # regiao: região que se deseja analisar: Brasil, Sul, Sudeste, Centro-Oeste, Norte, Nordeste. Se
            # deseja analisar uma cidade ou estado, deixar em branco
    
    # estado: estado que se deseja analisar. Se deseja analisar uma região ou cidade, deixar em branco
    
    # municipio: município que se deseja analisar. Se deseja analisar uma região ou estado, deixar em branco
    
    # tempo: número de dias que se deseja prever
    
    
    def dataframe(y):
        
        # função realizar a regressão a partir dos dados
        
        X = np.arange(1, len(y)+1, 1) # dias
    
        u = []
        mean_square = []
        y_fit = []
        
        
        for n in range(2, 4):
            
            y_pred = 0
            
            u.append(polyfit(X, y, deg=n))
            
            u_test = u[n-2]
            
            X_test = np.arange(1, len(y)+1, 1) # dias
            
            for i in range(0, n):
                
                y_pred += u_test[i]*X_test + u_test[-1]
                
            y_fit.append(y_pred)
                
                
            mean_square.append(mse(y, y_pred))
            
            
        index = np.where(mean_square == np.amin(mean_square))[0][0]
        degree = index + 2
        u_fit = u[index]
        y_fit = y_fit[index]

        
        return u, u_fit, y_fit
    
    
    
    
    path = path + '/HIST_PAINEL_COVIDBR_Parte3_' + date + '.csv'

    df = pd.read_csv(path, sep=';', usecols=['regiao', 'estado', 'codmun', 'municipio', 'data', 'populacaoTCU2019', 'casosAcumulado', 'casosNovos', 'obitosAcumulado',
                                             'obitosNovos', 'Recuperadosnovos'])
        
    
    if regiao == 'Brasil' and estado == '' and municipio == '':
        
        data = df.loc[df['regiao'] == regiao].sort_values(by='data')
        
        
    elif regiao != 'Brasil' and estado == '' and municipio == '':
        
        data = df.loc[df['regiao'] == regiao].sort_values(by='data')
        data = data[data['municipio'].isnull()]
        data = data[data['codmun'].isnull()]
        
        
        if regiao == 'Norte':
            
            data_N = []
            lista_estados = ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO']
            
            for estados in lista_estados:
                
                data_N.append(data.loc[data['estado'] == estados])
                
                        
            obitos = data_N[0]['obitosAcumulado'].values + data_N[1]['obitosAcumulado'].values + data_N[2]['obitosAcumulado'].values + \
                     data_N[3]['obitosAcumulado'].values + data_N[4]['obitosAcumulado'].values + data_N[5]['obitosAcumulado'].values + \
                     data_N[6]['obitosAcumulado'].values
                
            casos = data_N[0]['casosAcumulado'].values + data_N[1]['casosAcumulado'].values + data_N[2]['casosAcumulado'].values + \
                    data_N[3]['casosAcumulado'].values + data_N[4]['casosAcumulado'].values + data_N[5]['casosAcumulado'].values  + \
                    data_N[6]['casosAcumulado'].values
                     
        if regiao == 'Nordeste':
            
            data_NE = []
            lista_estados = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
            
            for estados in lista_estados:
                
                data_NE.append(data.loc[data['estado'] == estados])
                
                        
            obitos = data_NE[0]['obitosAcumulado'].values + data_NE[1]['obitosAcumulado'].values + data_NE[2]['obitosAcumulado'].values + \
                     data_NE[3]['obitosAcumulado'].values + data_NE[4]['obitosAcumulado'].values + data_NE[5]['obitosAcumulado'].values + \
                     data_NE[6]['obitosAcumulado'].values
                
            casos = data_NE[0]['casosAcumulado'].values + data_NE[1]['casosAcumulado'].values + data_NE[2]['casosAcumulado'].values + \
                    data_NE[3]['casosAcumulado'].values + data_NE[4]['casosAcumulado'].values + data_NE[5]['casosAcumulado'].values  + \
                    data_NE[6]['casosAcumulado'].values + data_NE[7]['casosAcumulado'].values + data_NE[8]['casosAcumulado'].values
                     
                     
        if regiao == 'Centro-Oeste':
            
            data_CO = []
            lista_estados = ['DF', 'GO', 'MS', 'MT']
            
            for estados in lista_estados:
                
                data_CO.append(data.loc[data['estado'] == estados])
                
                        
            obitos = data_CO[0]['obitosAcumulado'].values + data_CO[1]['obitosAcumulado'].values + data_CO[2]['obitosAcumulado'].values + \
                     data_CO[3]['obitosAcumulado'].values
                
            casos = data_CO[0]['casosAcumulado'].values + data_CO[1]['casosAcumulado'].values + data_CO[2]['casosAcumulado'].values + \
                     data_CO[3]['casosAcumulado'].values
                     
        if regiao == 'Sudeste':
            
            data_SE = []
            lista_estados = ['ES', 'MG', 'RJ', 'SP']
            
            for estados in lista_estados:
                
                data_SE.append(data.loc[data['estado'] == estados])
                
                        
            obitos = data_SE[0]['obitosAcumulado'].values + data_SE[1]['obitosAcumulado'].values + data_SE[2]['obitosAcumulado'].values + \
                     data_SE[3]['obitosAcumulado'].values
                
            casos = data_SE[0]['casosAcumulado'].values + data_SE[1]['casosAcumulado'].values + data_SE[2]['casosAcumulado'].values + \
                     data_SE[3]['casosAcumulado'].values
                     
        if regiao == 'Sul':
            
            data_S = []
            lista_estados = ['PR', 'RS', 'SC']
            
            for estados in lista_estados:
                
                data_S.append(data.loc[data['estado'] == estados])
                
                        
            obitos = data_S[0]['obitosAcumulado'].values + data_S[1]['obitosAcumulado'].values + data_S[2]['obitosAcumulado'].values
                
            casos = data_S[0]['casosAcumulado'].values + data_S[1]['casosAcumulado'].values + data_S[2]['casosAcumulado'].values
                
        
    elif regiao == '' and estado != '' and municipio == '':
        
        data = df.loc[df['estado'] == estado].sort_values(by='data')
        data = data[data['municipio'].isnull()]
        data = data[data['codmun'].isnull()]
        
        obitos = data['obitosAcumulado']
        casos = data['casosAcumulado']
                
        
    elif regiao == '' and estado == '' and municipio != '':
        
        data = df.loc[df['municipio'] == municipio].sort_values(by='data')
        
    else:
        
        print('Erro de digitação')

    
    u_obitos, u_obitos_fit, y_fit_obitos = dataframe(obitos) # matriz contendo os coeficientes dos polinômios de 2º e 3º grau para óbitos
    u_casos, u_casos_fit, y_fit_casos = dataframe(casos) # matriz contendo os coeficientes dos polinômios de 2º e 3º grau para casos
    
    t = np.arange(1, len(y_fit_casos)+1 + tempo, 1) # vetor tempo, igual ao número de dias da amostra
                                                    # acrescido do número de dias que se deseja prever
    
    obitos_pred_2 = u_obitos[0][0]*t**2 + u_obitos[0][1]*t + u_obitos[0][2] # vetor contendo o número de óbitos previstos pelo
                                                                            # polinômio de 2º grau
        
    obitos_pred_3 = u_obitos[1][0]*t**3 + u_obitos[1][1]*t**2 + u_obitos[1][2]*t + u_obitos[1][3] # vetor contendo o número de óbitos previstos pelo
                                                                            # polinômio de 3º grau
                            
    obitos_mean = (obitos_pred_2 + obitos_pred_3)/2 # media entre o polinômio de 2º e 3º grau para obitos
                                                                            
    
    casos_pred_2 = u_casos[0][0]*t**2 + u_casos[0][1]*t + u_casos[0][2] # vetor contendo o número de casos previstos pelo
                                                                            # polinômio de 2º grau
                                                                            
    casos_pred_3 = u_casos[1][0]*t**3 + u_casos[1][1]*t**2 + u_casos[1][2]*t + u_casos[1][3] # vetor contendo o número de casos previstos pelo
                                                                            # polinômio de 3º grau
                                                                            
    casos_mean = (casos_pred_2 + casos_pred_3)/2 # media entre o polinômio de 2º e 3º grau para casos
    
    
    return t, obitos_pred_2.astype(int), obitos_pred_3.astype(int), obitos_mean, casos_pred_2.astype(int), casos_pred_3.astype(int), casos_mean


# INÍCIO DO PROGRAMA

path = 'D:/COVID-19'
date = '11jun2021'

t, obitos_pred_2, obitos_pred_3, obitos_mean, casos_pred_2, casos_pred_3, casos_mean = regressao_polinomial(path, date, '', 'RS', '')