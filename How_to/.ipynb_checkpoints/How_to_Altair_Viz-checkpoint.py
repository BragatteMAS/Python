import numpy as np
import pandas as pd
import altair as alt
cols = ['Type','Price','Distance','Date','Landsize','Regionname']
melb = pd.read_csv(
   "/content/melb_data.csv", usecols = cols, parse_dates = ['Date']
).sample(n=1000).reset_index(drop=True)
melb.head()
