#WebDashboard_python
# Web data dashboard Python

all_teams_df = pd.read_csv(‘srcdata/shot_dist_compiled_data_2019_20.csv’)
all_teams_df[all_teams_df.group == 'NOP']

import plotly.express as px
fig = px.scatter(all_teams_df[all_teams_df.group == 'NOP'], x='min_mid', y='player', size='shots_freq', color='pl_pps')
fig.show()

#Dashboard

def clean_chart_format(fig):
    import plotly.graph_objects as go
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        annotations=[
            go.layout.Annotation(
                x=0.9,
                y=1.02,
                showarrow=False,
                text="Twitter: @_jphwang",
                xref="paper",
                yref="paper",
                textangle=0
            ),
        ],
        font=dict(
            family="Arial, Tahoma, Helvetica",
            size=10,
            color="#404040"
        ),
        margin=dicdef clean_chart_format(fig):
    import plotly.graph_objects as go
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        annotations=[
            go.layout.Annotation(
                x=0.9,
                y=1.02,
                showarrow=False,
                text="Twitter: @_jphwang",
                xref="paper",
                yref="paper",
                textangle=0
            ),
        ],
        font=dict(
            family="Arial, Tahoma, Helvetica",
            size=10,
            color="#404040"
        ),
        margin=dict(
            t=20
        )
    )
    fig.update_traces(marker=dict(line=dict(width=1, color='Navy')),
                      selector=dict(mode='markers'))
    fig.update_coloraxes(
        colorbar=dict(
            thicknessmode="pixels", thickness=15,
            outlinewidth=1,
            outlinecolor='#909090',
            lenmode="pixels", len=300,
            yanchor="top",
            y=1,
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, tickson='boundaries', gridcolor='LightGray', fixedrange=True)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray', fixedrange=True)
    return True


def make_shot_dist_chart(input_df, color_continuous_scale=None, size_col='shots_count', col_col='pl_acc', range_color=None):

    max_bubble_size = 15
    if color_continuous_scale is None:
        color_continuous_scale = px.colors.diverging.RdYlBu_r
    if range_color is None:
        range_color = [min(input_df[col_col]), max(input_df[col_col])]

    fig = px.scatter(
        input_df, x='min_mid', y='player', size=size_col,
        color=col_col,
        color_continuous_scale=color_continuous_scale,
        range_color=range_color,
        range_x=[0, 49],
        range_y=[-1, len(input_df.player.unique())],
        hover_name='player', hover_data=['min_start', 'min_end', 'shots_count', 'shots_made', 'shots_freq', 'shots_acc', ],
        render_mode='svg'
    )
    fig.update_coloraxes(colorbar=dict(title='Points per<BR>100 shots'))
    fig.update_traces(marker=dict(sizeref=2. * 30 / (max_bubble_size ** 2)))
    fig.update_yaxes(title="Player")
    fig.update_xaxes(title='Minute', tickvals=list(range(0, 54, 6)))

    return fig


fig = make_shot_dist_chart(
    all_teams_df[all_teams_df.group == 'SAS'], col_col='pl_pps', range_color=[90, 120], size_col='shots_freq')
clean_chart_format(fig)
fig.update_layout(height=500, width=1250)
fig.show()t(
            t=20
        )
    )
    fig.update_traces(marker=dict(line=dict(width=1, color='Navy')),
                      selector=dict(mode='markers'))
    fig.update_coloraxes(
        colorbar=dict(
            thicknessmode="pixels", thickness=15,
            outlinewidth=1,
            outlinecolor='#909090',
            lenmode="pixels", len=300,
            yanchor="top",
            y=1,
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, tickson='boundaries', gridcolor='LightGray', fixedrange=True)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray', fixedrange=True)
    return True


def make_shot_dist_chart(input_df, color_continuous_scale=None, size_col='shots_count', col_col='pl_acc', range_color=None):

    max_bubble_size = 15
    if color_continuous_scale is None:
        color_continuous_scale = px.colors.diverging.RdYlBu_r
    if range_color is None:
        range_color = [min(input_df[col_col]), max(input_df[col_col])]

    fig = px.scatter(
        input_df, x='min_mid', y='player', size=size_col,
        color=col_col,
        color_continuous_scale=color_continuous_scale,
        range_color=range_color,
        range_x=[0, 49],
        range_y=[-1, len(input_df.player.unique())],
        hover_name='player', hover_data=['min_start', 'min_end', 'shots_count', 'shots_made', 'shots_freq', 'shots_acc', ],
        render_mode='svg'
    )
    fig.update_coloraxes(colorbar=dict(title='Points per<BR>100 shots'))
    fig.update_traces(marker=dict(sizeref=2. * 30 / (max_bubble_size ** 2)))
    fig.update_yaxes(title="Player")
    fig.update_xaxes(title='Minute', tickvals=list(range(0, 54, 6)))

    return fig


fig = make_shot_dist_chart(
    all_teams_df[all_teams_df.group == 'SAS'], col_col='pl_pps', range_color=[90, 120], size_col='shots_freq')
clean_chart_format(fig)
fig.update_layout(height=500, width=1250)
fig.show()

#Flask version of plotly
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

all_teams_df = pd.read_csv('srcdata/shot_dist_compiled_data_2019_20.csv')

app = dash.Dash(__name__)
server = app.server
team_names = all_teams_df.group.unique()
team_names.sort()
app.layout = html.Div([
    html.Div([dcc.Dropdown(id='group-select', options=[{'label': i, 'value': i} for i in team_names],
                           value='TOR', style={'width': '140px'})]),
    dcc.Graph('shot-dist-graph', config={'displayModeBar': False})])

@app.callback(
    Output('shot-dist-graph', 'figure'),
    [Input('group-select', 'value')]
)
def update_graph(grpname):
    import plotly.express as px
    return px.scatter(all_teams_df[all_teams_df.group == grpname], x='min_mid', y='player', size='shots_freq', color='pl_pps')

if __name__ == '__main__':
    app.run_server(debug=False)
view raw
dash_simple_nba_simple_app.py hosted with ❤ by GitHub

#Dash_version2

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

all_teams_df = pd.read_csv('srcdata/shot_dist_compiled_data_2019_20.csv')

app = dash.Dash(__name__)
server = app.server
team_names = all_teams_df.group.unique()
team_names.sort()
app.layout = html.Div([
    html.Div([dcc.Dropdown(id='group-select', options=[{'label': i, 'value': i} for i in team_names],
                           value='TOR', style={'width': '140px'})]),
    dcc.Graph('shot-dist-graph', config={'displayModeBar': False})])

@app.callback(
    Output('shot-dist-graph', 'figure'),
    [Input('group-select', 'value')]
)
def update_graph(grpname):
    import plotly.express as px
    return px.scatter(all_teams_df[all_teams_df.group == grpname], x='min_mid', y='player', size='shots_freq', color='pl_pps')

if __name__ == '__main__':
    app.run_server(debug=False)
view raw
dash_simple_nba_simple_app.py hosted with ❤ by GitHub

'''
ref:
<<
https://towardsdatascience.com/build-a-web-data-dashboard-in-just-minutes-with-python-d722076aee2b
>>
'''