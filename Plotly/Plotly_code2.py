#Seetings codes of plotly for overview data bars.

##Imports
#all plotly
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go
import cufflinks as cf
init_notebook_mode(connected=True)
#others
import pandas as pd
import numpy as np

##Importing the dataset
df = pd.read_csv(filepath)

layout=go.Layout(updatemenus=list([dict(buttons= list_updatemenus)]))
##The Visible Parameter
data= [
go.Histogram(x=option1,name='option1'),
go.Histogram(x=option2,name='option2'),
go.Histogram(x=option3,name='option3')
]

#Show first graph object
{'visible':[True, False, False]}
#Show second graph object
{'visible':[False, True, False]}
#Show first and third graph object
{'visible':[True, False, True]}

list_updatemenus = 
[{'label': 'Option 1',
  'method': 'update',
  'args': [{'visible': [True, False, False]}, {'title': 'Title is Option 1'}]},
 {'label': 'Option 2',
  'method': 'update',
  'args': [{'visible': [False, True, False]}, {'title': 'Title is Option 2'}]},
 {'label': 'Option 3',
  'method': 'update',
  'args': [{'visible': [False, False, True]}, {'title': 'Title is Option 3'}]}]
layout=go.Layout(title = 'default title',
updatemenus=list([dict(buttons= list_updatemenus)]))

#defining list_updatemenus
list_updatemenus = [{'label': 'Survived',
  'method': 'update',
  'args': [{'visible': [False, False, False, True, True, True]}, {'title': 'Distribution of Age for Survived Passengers'}]},
 {'label': 'Non Survived',
  'method': 'update',
  'args': [{'visible': [True, True, True, False, False, False]}, {'title': 'Distribution of Age for Non-Survived Passengers'}]}]
#defining all graph objects
x_pclass3 = df[df['Pclass']==3]['Fare']
x_pclass1 = df[df['Pclass']==1]['Fare']
x_pclass2 = df[df['Pclass']==2]['Fare']
x_male = df[df['Sex']=='male']['Fare']
x_female = df[df['Sex']=='female']['Fare']
#defining data
data=[go.Histogram(x=x_pclass3,name='3rd Class'),go.Histogram(x=x_pclass1,name='1st Class',opacity = .5,nbinsx=60),go.Histogram(x=x_pclass2,name='2nd Class',opacity = .5),go.Histogram(x=x_male,name='Male',opacity = .5),go.Histogram(x=x_female,name='female',opacity = .5)]
#defining layout
layout=go.Layout(title='Distribution of Fares by Pclass and Gender',updatemenus=list([dict(buttons= list_updatemenus)]),barmode='overlay')
#defining figure and plotting
fig = go.Figure(data,layout)
iplot(fig)

##Custom buttons
layout=go.Layout(updatemenus=list([dict(buttons= list_updatemenus), type = buttons]))

#defining list_updatemenus
list_updatemenus = [{'label': 'Survived',
  'method': 'update',
  'args': [{'visible': [False, False, False, True, True, True]}, {'title': 'Distribution of Fares by Pclass'}]},
 {'label': 'Non Survived',
  'method': 'update',
  'args': [{'visible': [True, True, True, False, False, False]}, {'title': 'Distribution of Fares by Gender'}]}]
#defining graph objects
x_pclass3_nonsurvived = df[df['Pclass']==3][df['Survived']==0]['Age']
x_pclass1_nonsurvived = df[df['Pclass']==1][df['Survived']==0]['Age']
x_pclass2_nonsurvived = df[df['Pclass']==2][df['Survived']==0]['Age']
x_pclass3_survived = df[df['Pclass']==3][df['Survived']==1]['Age']
x_pclass1_survived = df[df['Pclass']==1][df['Survived']==1]['Age']
x_pclass2_survived = df[df['Pclass']==2][df['Survived']==1]['Age']
#defining data
data=[go.Histogram(x=x_pclass3_nonsurvived,name='Died 3rd Class',nbinsx=60),go.Histogram(x=x_pclass1_nonsurvived,name='Died 1st Class',opacity = .5,nbinsx=60),go.Histogram(x=x_pclass2_nonsurvived,name='Died 2nd Class',opacity = .5,nbinsx=60),go.Histogram(x=x_pclass3_survived,name='Survived 3rd Class',nbinsx=60),go.Histogram(x=x_pclass1_survived,name='Survived 1st Class',opacity = .5,nbinsx=60),go.Histogram(x=x_pclass2_survived,name='Survived 2nd Class',opacity = .5,nbinsx=60)]
#defining layout
layout=go.Layout(title='Distribution of Age by Pclass',updatemenus=list([dict(buttons= list_updatemenus,type = 'buttons')]),barmode='overlay')
#defining layout and plotting
fig = go.Figure(data,layout)
iplot(fig)

layout=go.Layout(
    sliders=sliders
)

# Create figure
fig = go.Figure()
# Create Graph Object for every increase of 2 years of Age
for step in np.arange(0, 80, 2):
    y=[]
    for i in list(df['Survived'].unique()):
        result = df[df['Age']<=step][df['Survived']==i]['Survived'].count()
        y.append(result)
    fig.add_trace(
        go.Bar(
            visible=False,
            x = list(df['Survived'].unique()),
            y= y,
            name="Age = " + str(step)))

##Sliders and steps
#defining sliders
sliders = [dict(
    currentvalue={"prefix": "Age less than "},
    active=1,
    steps=steps
)]
#defining steps 
steps = []
for i in range(len(fig.data)):
    step = dict(
        label = str([i for i in np.arange(0, 80, 2)][i]),
        method="restyle",
        args=["visible", [False] * len(fig.data)],
    )
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

#defining layout and plotting 
fig.update_layout(
    title = 'Change of Survivability with Age',
    yaxis=dict(title='Count of Survived'),
    sliders=sliders
)
fig.show()

'''
ref:
<<https://towardsdatascience.com/python-for-data-science-advance-guide-to-data-visualization-with-plotly-8dbeaedb9724>>
'''