import pandas as pd
import datetime

def get_covid_data_jhu(dt_ini, dt_fim, us_columns = True, country = None):
    
    date_range = pd.date_range(start = dt_ini, end = dt_fim).to_list()
    string_range = [str(d.date().strftime("%m-%d-%Y")) for d in date_range]
    
    full_data_list = []
    for dat in string_range:
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{dat}.csv"
        current_data = pd.read_csv(url)
        full_data_list.append(current_data)
    
    full_df = pd.concat(full_data_list)
    
    if country:
        full_df = full_df[full_df['Country_Region'].isin(country)]
        
    if not us_columns:
        full_df.drop(full_df.columns[0:3], axis = 1, inplace = True)
        
    return full_df

# Examples
print(
        get_covid_data_jhu("2020-05-24", "2020-05-27", us_columns = True, country = ['Brazil'])
        )