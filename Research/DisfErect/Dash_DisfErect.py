# [Ref](https://www.youtube.com/watch?v=fKgPXUUsg1M)actor by @bragatte 202104031234

#default
import dash
import dash_html_components as html 
import dash_core_components as dcc
##from pandas_datareader import data as web
##from datetime import datetime as dt

#Live de Python version
from dash import Dash
from dash.dependencies import Input, Output
from dash_core_components import Input as dcc_input 
from dash_html_components import Div, H1, H2, H3, P, Br

##CSS options link
external_stylesheets = [
    'https://unpkg.com/termina.css@0.7.2/dist/terminal.min.css'
]

#Call Dash
app = Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = Div(
    children=[ 
    #Intro
        H1('Tibial Nerve Stimulation add on Pelvic Muscle Training for Postprostatectomy Urinary Incontinence'),
        P('Example of Erectile Dysfunction Database    Data collection carried out by the researcher Fernandes, J.A.'),
        P('Created by Bragatte 202102061700'),
    #Plots
        H2('Plots'),
        #Graph( ),

    #Updates
        dcc_input(id='meu_input1', value='results'),
        dcc_input(id='meu_input2', value='Right-Again'),
        P(id='output1'),
        P(id='output2'),
        
     ]
 )

@app.callback(
    [
        Output('output1', 'children'),
        Output('output2', 'children')

    ],
    [
        Input('meu_input1','value'),
        Input('meu_input2','value'),

    ],
)

def meu_callback(meu_input1, meu_input2):
    return meu_input1, meu_input2

app.run_server(debug=True)