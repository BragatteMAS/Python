# -*- coding: utf-8 -*-
"""How_to_Altair_Viz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/BragatteMAS/Python/blob/master/How_to/How_to_Altair_Viz.ipynb

How to use [**Altair** for simple **Viz**](https://towardsdatascience.com/3-examples-to-show-python-altair-is-more-than-a-data-visualization-library-700e37cbf95b) like Pandas

    Datasets e.g from Kaggle:
* [Melb](https://www.kaggle.com/anthonypino/melbourne-housing-market)
* [Insurance](https://www.kaggle.com/mirichoi0218/insurance)
* [Marketing](https://www.kaggle.com/yoghurtpatil/direct-marketing)
* [Bank](https://www.kaggle.com/sakshigoyal7/credit-card-customers)

        create by @bragatte 202103151325
"""

import numpy as np
import pandas as pd
import altair as alt

cols = ['Type','Price','Distance','Date','Landsize','Regionname']
melb = pd.read_csv(
   "/content/melb_data.csv", usecols = cols, parse_dates = ['Date']
).sample(n=1000).reset_index(drop=True)
melb.head()

alt.Chart(melb).mark_bar().encode(
   x = 'Regionname', y = 'avg_price:Q'
).transform_aggregate(
   avg_price = 'mean(Price)', groupby = ['Regionname']
).properties(
   height = 300, width = 500
)

alt.Chart(
  melb, height=300, width=500
).mark_bar().encode(
  x = 'Regionname', y = 'avg_price:Q'
).transform_filter(
  alt.FieldGTPredicate(field='Distance', gt=3)
).transform_aggregate(
  avg_price = 'mean(Price)',groupby = ['Regionname']
)

melb['OwnerId'] = np.arange(1,1001)
df = pd.DataFrame({
  'OwnerId': melb['OwnerId'],
  'Age': np.random.randint(20, 40, size=1000),
  'Salary': np.random.randint(5000, 10000, size=1000)
})
df.head()

alt.Chart(
  df, height=300, width=500
).mark_bar().encode(
  x = 'mean(Salary):Q', y = 'Type:O'
).transform_lookup(
  lookup='OwnerId',
  from_=alt.LookupData(data=melb, key='OwnerId', fields=['Type'])
)

"""## [Altair: Statistical Visualization Library for Python](https://towardsdatascience.com/altair-statistical-visualization-library-for-python-cfb63847c0c0)"""

insurance = pd.read_csv("/content/insurance.csv")
insurance.head()

"""### Scatter plot"""

(alt.
  Chart(insurance).
  mark_circle(size=40).
  encode(x='charges', y='bmi').
  properties(height=400, width=500))

"""### Interactive option"""

(alt.
  Chart(insurance).
  mark_circle(size=50).
  encode(x='charges', y='bmi', color='smoker').
  properties(height=400, width=500).
  interactive())

"""### Interactive with Hover option """

(alt.
  Chart(insurance).
  mark_circle(size=50).
  encode(x='charges', y='bmi', color='smoker', tooltip=   
  ['age','sex']).
  properties(height=400, width=500).
  interactive())

"""### Bar plot

"""

(alt.
  Chart(insurance).
  mark_bar().
  encode(x='region', y='mean(charges):Q').
  properties(height=300, width=400))

y=alt.X(field='charges', aggregate='mean', type='quantitative')

insurance[['region','charges']].groupby('region').mean()

"""### Histogram"""

(alt.
  Chart(insurance).
  mark_bar().
  encode(alt.X('bmi:Q', bin=True), y='count()').
  properties(height=300, width=500))

"""### Grid of plots

"""

p1 = (alt.
        Chart(insurance).
        mark_bar().
        encode(x='region', y='mean(charges):Q').
        properties(height=200, width=300))
p2 = (alt.
        Chart(insurance).
        mark_bar().
        encode(alt.X('bmi:Q', bin=True), y='count()').
        properties(height=200, width=300))

p1 | p2

p1 & p2

"""## [Altair: Statistical Visualization Library for Python (Part 2)](https://towardsdatascience.com/altair-statistical-visualization-library-for-python-part-2-4c8ce134e743)"""

marketing = pd.read_csv("/content/DirectMarketing.csv")
marketing.head()

(alt.
  Chart(marketing).
  mark_circle(size=50).
  encode(x='Salary', y='AmountSpent', color='Age'))

"""Filter data

    It is possible to filter data while creating a visualization. For instance, we can only plot the data points for which the salary is less than 120000.
"""

(alt.
  Chart(marketing).
  mark_circle(size=50).
  encode(x='Salary', y='AmountSpent', color='Age').
  transform_filter(alt.FieldLTPredicate(field='Salary', lt=120000)).
  properties(height=400, width=500))

"""    The same filtering operation can also be done by using the datum module of Altair. It is simpler in terms of the syntax. The following code will create the same plot as above."""

from altair import datum
(alt.
  Chart(marketing).
  mark_circle(size=50).
  encode(x='Salary', y='AmountSpent', color='Age').
  transform_filter(datum.Salary < 120000).
  properties(height=400, width=500))

"""    Specify a condition for filtering based on a categorical column. For instance, the data points that belong to a set of discrete values can be filtered using the FieldOneOfPredicate method."""

(alt.
  Chart(marketing).
  mark_circle(size=50).
  encode(x='Salary', y='AmountSpent', color='Age').
  transform_filter(alt.FieldOneOfPredicate(field='Children', 
                   oneOf= [0,2,3])).
  properties(height=400, width=500))

"""Two plots:
        One will the a scatter plot that consists of the salary and amount spent columns. The other one will be a bar plot that shows the average salary for the categories in the age column. The second plot will also be used as a filter for the first plot.

Calculated the averages by applying the following transformation in the encode function
`y='mean(Salary):Q'`
"""

selection = alt.selection_multi(fields=['Age'])
first = (alt.
          Chart().
          mark_circle(size=50).
          encode(x='Salary', y='AmountSpent').
          transform_filter(selection).
          properties(height=300, width=500))
second = (alt.
           Chart().
           mark_bar().
           encode(
           x='Age:O',y='mean(Salary):Q',
           color=alt.condition(selection, alt.value('steelblue'),   
                 alt.value('lightgray'))
           ).
           properties(height=300, width=300).
           add_selection(selection))
alt.hconcat(first, second, data=marketing)

"""## [Altair: Statistical Visualization Library for Python (Part 3)](https://towardsdatascience.com/altair-statistical-visualization-library-for-python-part-3-c1e650a8411e)"""

cols = ['Attrition_Flag','Gender','Education_Level', 'Marital_Status','Credit_Limit','Total_Trans_Amt','Total_Trans_Ct']
churn = pd.read_csv("/content/BankChurners.csv", usecols=cols)\
.sample(n=1000)
churn.head()

selection = alt.selection(type='interval')

plt1 = (alt.
         Chart(churn).
         mark_circle(size=50).
         encode(
          x='Credit_Limit', y='Total_Trans_Amt',
          color = alt.condition(selection, 'Gender',  
          alt.value('lightgray'))
         ).
         add_selection(selection))
plt2 = (alt.
         Chart(churn).
         mark_bar().
         encode(y='Gender', x='count(Gender):Q',color = 'Gender').
         transform_filter(selection))

plt1 & plt2

"""`y='mean(Total_Trans_Amt):Q'`"""

selection = alt.selection(type='interval')
plt1 = (alt.
         Chart().
         mark_circle(size=50).
         encode(x='Credit_Limit', y='Total_Trans_Amt',
         color='Gender').
         transform_filter(selection))
plt2 = (alt.
         Chart().
         mark_bar().
         encode(
         x='Marital_Status', y='mean(Total_Trans_Amt):Q',
         color=alt.condition(selection, alt.value("lightblue"),   
         alt.value("lightgray"))
         ).
         properties(height=300, width=200).
         add_selection(selection))

alt.hconcat(plt1, plt2, data=churn)

selection = alt.selection_multi(fields=['Education_Level'], bind='legend')

(alt.
  Chart(churn).
  mark_circle(size=50).
  encode(
  x='Total_Trans_Ct', y='Total_Trans_Amt',
  color= alt.Color('Education_Level:N',
  scale=alt.Scale(scheme='category20b')),
  opacity=alt.condition(selection, alt.value(1), alt.value(0.1))
  ).
  properties(height=400, width=500).
  add_selection(selection))

"""## [Altair: Statistical Visualization Library for Python](https://towardsdatascience.com/altair-statistical-visualization-library-for-python-part-4-9ec970fb12e8) (Part 4)"""

insurance = pd.read_csv("/content/insurance.csv")
insurance.head()

(alt.
  Chart(insurance).
  mark_circle().
  encode(x='charges', y='bmi', color='smoker').
  properties(height=400, width=500))

(alt.
  Chart(insurance).
  mark_circle().
  encode(
    alt.X('charges'),
    alt.Y('bmi', scale=alt.Scale(zero=False)),
    alt.Color('smoker')).
properties(height=400, width=500))

(alt.
  Chart(insurance).
  mark_circle().
  encode(
    alt.X('charges'),
    alt.Y('bmi', scale=alt.Scale(domain=(10,60))),
    alt.Color('smoker')).
properties(height=300, width=400))

(alt.
  Chart(insurance).
  mark_circle(size=50, color='darkblue', opacity=0.6).
  encode(
    alt.X('charges'),
    alt.Y('bmi', scale=alt.Scale(domain=(15,55)))
  ).
  properties(height=400, width=500))

(alt.
  Chart(insurance).
  mark_circle().
  encode(
    alt.X('charges'),
    alt.Y('bmi', scale=alt.Scale(domain=(15,55))),
    size = alt.value(50),
    color = alt.value('darkblue'),
    opacity = alt.value(0.6)
  ).
  properties(height=400, width=500))

(alt.
  Chart(insurance).
  mark_circle(size=40).
  encode(
    alt.X('charges'),
    alt.Y('bmi', scale=alt.Scale(zero=False)),
    alt.Color('smoker', 
              legend=alt.Legend(
                 title='Do they smoke?',  
                 orient='left',
                 titleFontSize=13,
                 labelFontSize=13
                 )
              )
    ).
  properties(title="Bmi vs Insurance Cost")
)

(alt.
  Chart(insurance).
  mark_circle(size=40).
  encode(
    alt.X('charges', title="Insurance Cost"),
    alt.Y('bmi', scale=alt.Scale(zero=False), 
          title="Body Mass Index"),
    alt.Color('smoker', 
              legend=alt.Legend(
                 title='Do they smoke?',  
                 orient='left',
                 titleFontSize=13,
                 labelFontSize=13
                 )
              )
    ).
  properties(title="Bmi vs Insurance Cost",
             height=350, width=500)
)