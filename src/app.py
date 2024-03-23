import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

terr2 = pd.read_csv('https://raw.githubusercontent.com/tahmimh/MM-804-GRAPHICS-AND-ANIMATION/main/Dataset/modified_globalterrorismdatabase.csv')

location1 = terr2[['country_txt', 'latitude', 'longitude']]
list_locations = location1.set_index('country_txt')[['latitude', 'longitude']].T.to_dict('dict')

region = terr2['region_txt'].unique()

app = dash.Dash(__name__, )
server = app.server
app.layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.H1('Global Terrorism Database Visualization', style = {"margin-top": "50px", "margin-bottom": "10px", 'color': '#3d5a80', 'font-family': 'Times New Roman', 'font-weight': 'bold'}),
                html.H5('From Year 1970 to Year 2021', style = {"margin-top": "0px", 'color': '#3d5a80'}),

            ]),
        ], className = "six column", id = "title")

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),


    html.Div([
        html.Div([
            html.P('Select Region:', className='fix_label', style={'color': '#242a5e'}),
            dcc.Dropdown(
                id='w_countries',
                multi=False,
                clearable=True,
                disabled=False,
                style={'display': True},
                value='South Asia',
                placeholder='Select Countries',
                options=[{'label': c, 'value': c} for c in region],
                className='dcc_compon'
            ),
        ], className="create_container five columns"),

        html.Div([
            html.P('Select Country:', className='fix_label', style={'color': '#242a5e'}),
            dcc.Dropdown(
                id='w_countries1',
                multi=False,
                clearable=True,
                disabled=False,
                style={'display': True},
                placeholder='Select Countries',
                options=[],
                className='dcc_compon'
            ),
        ], className="create_container five columns"),


        html.Div([
            html.P('Select Year:', className='fix_label', style={'color': '#242a5e', 'margin-left': '0%'}),
            dcc.RangeSlider(
                id='select_years',
                min=1970,
                max=2021,
                marks={year: str(year) for year in range(1970, 2022, 10)},  # Add marks every 10 years
                step=1,  # Allow to select each individual year
                dots=False,  # Show dots on slider
                value=[2010, 2021],  # Initial range
                tooltip={'always_visible': True, 'placement': 'bottom'},  # Show selected year on tooltip
            ),
        ], className="create_container five columns"),
    ], className="row flex-display", style={'position': 'sticky', 'top': '0', 'z-index': '999', 'background-color': 'rgba(255, 255, 255, 0.1)'}),

    
    html.Div([
        html.Div([
            dcc.Graph(
                id='map_1',
                config={'displayModeBar': 'hover', 'responsive': True, 'displaylogo': False, 'scrollZoom': True, 'displayModeBar': True, 'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'resetScale2d', 'toggleSpikelines', 'hoverClosestPie', 'toggleHover', 'sendDataToCloud', 'zoomInGeo', 'zoomOutGeo', 'resetGeo', 'hoverClosestGeo', 'hoverClosestGl2d', 'toggleHover', 'toggleSpikelines', 'resetViewMapbox'], 'toImageButtonOptions': {'format': 'png', 'filename': 'custom_image', 'height': 1080, 'width': 1920}},
                style={'width': '100%', 'height': '100vh'}  # Set graph size to fullscreen
            )
        ], className="create_container full columns"),
    ], className="row flex-display"),
    
    
    
    html.Div([
        html.Div([
                dcc.Graph(id = 'bar1',
                        config = {'displayModeBar': 'hover'}),

        ], className = "create_container nine columns"),


        html.Div([
                dcc.Graph(id = 'pie1',
                        config = {'displayModeBar': 'hover'}),

            ], className = "create_container four columns"), 

    ], className = "row flex-display"),

    

    html.Div([
        html.Div([
                dcc.Graph(id = 'pie2',
                        config = {'displayModeBar': 'hover'}),

            ], className = "create_container four columns"), 


        html.Div([
                dcc.Graph(id = 'bar2',
                        config = {'displayModeBar': 'hover'}),

        ], className = "create_container nine columns"),

    ], className = "row flex-display"),


    html.Div([
        html.Div([
                dcc.Graph(id = 'bar3',
                        config = {'displayModeBar': 'hover'}),

        ], className = "create_container nine columns"),


        html.Div([
                dcc.Graph(id = 'pie3',
                        config = {'displayModeBar': 'hover'}),

            ], className = "create_container four columns"), 

    ], className = "row flex-display"),


    html.Div([
        html.Div([
                dcc.Graph(id = 'pie4',
                        config = {'displayModeBar': 'hover'}),

            ], className = "create_container four columns"), 


        html.Div([
                dcc.Graph(id = 'bar4',
                        config = {'displayModeBar': 'hover'}),

        ], className = "create_container nine columns"),

    ], className = "row flex-display"),


    html.Div([
         
        html.Div([
                dcc.Graph(id = 'bar5',
                        config = {'displayModeBar': 'hover'}),

        ], className = "create_container nine columns"),
        
        html.Div([
                dcc.Graph(id = 'pie5',
                        config = {'displayModeBar': 'hover'}),

            ], className = "create_container four columns"), 

    ], className = "row flex-display"),


], id = "mainContainer", style = {"display": "flex", "flex-direction": "column"})


@app.callback(
    Output('w_countries1', 'options'),
    Input('w_countries', 'value'))
def get_country_options(w_countries):
    terr3 = terr2[terr2['region_txt'] == w_countries]
    return [{'label': i, 'value': i} for i in terr3['country_txt'].unique()]


@app.callback(
    Output('w_countries1', 'value'),
    Input('w_countries1', 'options'))
def get_country_value(w_countries1):
    return [k['value'] for k in w_countries1][0]


# Create scattermapbox chart
@app.callback(Output('map_1', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def update_graph(w_countries, w_countries1, select_years):
    terr3 = terr2.groupby(['region_txt', 'country_txt', 'provstate', 'city', 'iyear', 'latitude', 'longitude'])[['nkill', 'nwound']].sum().reset_index()
    terr4 = terr3[(terr3['region_txt'] == w_countries) & (terr3['country_txt'] == w_countries1) & (terr3['iyear'] >= select_years[0]) & (terr3['iyear'] <= select_years[1])]

    if w_countries1:
        zoom = 4
        zoom_lat = list_locations[w_countries1]['latitude']
        zoom_lon = list_locations[w_countries1]['longitude']


    return {
        'data': [go.Scattermapbox(
            lon = terr4['longitude'],
            lat = terr4['latitude'],
            mode = 'markers',
            marker = go.scattermapbox.Marker(
                size = terr4['nwound'],
                color = terr4['nwound'],
                colorscale = 'picnic',
                showscale = True,
                sizemode = 'area'),

            hoverinfo = 'text',
            hovertext =
            '<b>Region</b>: ' + terr4['region_txt'].astype(str) + '<br>' +
            '<b>Country</b>: ' + terr4['country_txt'].astype(str) + '<br>' +
            '<b>Province/State</b>: ' + terr4['provstate'].astype(str) + '<br>' +
            '<b>City</b>: ' + terr4['city'].astype(str) + '<br>' +
            '<b>Longitude</b>: ' + terr4['longitude'].astype(str) + '<br>' +
            '<b>Latitude</b>: ' + terr4['latitude'].astype(str) + '<br>' +
            '<b>Killed</b>: ' + [f'{x:,.0f}' for x in terr4['nkill']] + '<br>' +
            '<b>Wounded</b>: ' + [f'{x:,.0f}' for x in terr4['nwound']] + '<br>' +
            '<b>Year</b>: ' + terr4['iyear'].astype(str) + '<br>'

        )],

        'layout': go.Layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            hovermode='closest',
            mapbox=dict(
                accesstoken='pk.eyJ1IjoidGFobWltMDAiLCJhIjoiY2x0ejJjcWRpMG4xdzJycnUxY3YwczNoOCJ9.5iS_Nui18oiJMo8XATKX0g',  # Use mapbox token here
                center=go.layout.mapbox.Center(lat=zoom_lat, lon=zoom_lon),
                style='light',
                zoom=5,
            ),
            autosize=True,
            updatemenus=[
                {   #"basic", "streets", "outdoors", "light", "dark", "satellite", or "satellite-streets" 
                    'buttons': [
                        {
                            'args': [{'mapbox.style': 'light'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Light',
                            'method': 'relayout'
                        },
                        {
                            'args': [{'mapbox.style': 'basic'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Basic',
                            'method': 'relayout'
                        },
                        
                        {
                            'args': [{'mapbox.style': 'streets'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Streets',
                            'method': 'relayout'
                        },

                        {
                            'args': [{'mapbox.style': 'satellite-streets'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Satellite Streets',
                            'method': 'relayout'
                        },

                        {
                            'args': [{'mapbox.style': 'satellite'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Satellite',
                            'method': 'relayout'
                        },

                        {
                            'args': [{'mapbox.style': 'dark'}, {'frame': {'duration': 500, 'redraw': True}}],
                            'label': 'Dark',
                            'method': 'relayout'
                        }
                    ],
                    'direction': 'down',
                    'showactive': True,
                    'x': 0.01,
                    'xanchor': 'left',
                    'y': 0.99,
                    'yanchor': 'top'
                }
            ]
        )

    }

# Create combination of bar  (show number of Wounded and death)
@app.callback(Output('bar1', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def update_graph(w_countries, w_countries1, select_years):
    # Data for bar
    terr7 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nkill', 'nwound']].sum().reset_index()
    terr8 = terr7[(terr7['region_txt'] == w_countries) & (terr7['country_txt'] == w_countries1) & (terr7['iyear'] >= select_years[0]) & (terr7['iyear'] <= select_years[1])]

    return {
        'data': [
                 go.Bar(
                     x = terr8['iyear'],
                     y = terr8['nkill'],
                     text = terr8['nkill'],
                     texttemplate = '%{text:.2s}',
                     textposition = 'auto',
                     name = 'Killed',

                     marker = dict(color = '#F5f8fa'),

                     hoverinfo = 'text',
                     hovertext =
                     '<b>Region</b>: ' + terr8['region_txt'].astype(str) + '<br>' +
                     '<b>Country</b>: ' + terr8['country_txt'].astype(str) + '<br>' +
                     '<b>Year</b>: ' + terr8['iyear'].astype(str) + '<br>' +
                     '<b>Killed</b>: ' + [f'{x:,.0f}' for x in terr8['nkill']] + '<br>'
                 ),

                 go.Bar(x = terr8['iyear'],
                        y = terr8['nwound'],
                        text = terr8['nwound'],
                        texttemplate = '%{text:.2s}',
                        textposition = 'auto',
                        textfont = dict(
                            color = 'white'
                        ),
                        name = 'Wounded',

                        marker = dict(color = '#219ebc'),

                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr8['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr8['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr8['iyear'].astype(str) + '<br>' +
                        '<b>Wounded</b>: ' + [f'{x:,.0f}' for x in terr8['nwound']] + '<br>'
                        )],

        'layout': go.Layout(
            barmode = 'stack',
            plot_bgcolor = '#afdefd',
            paper_bgcolor = '#afdefd',
            title = {
                'text': 'Wounded and Death in ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#242a5e',
                'size': 20},

            hovermode = 'x',

            xaxis = dict(title = '<b>Year</b>',
                         tick0 = 0,
                         dtick = 1,
                         color = '#242a5e',
                         showline = True,
                         showgrid = True,
                         showticklabels = True,
                         linecolor = '#242a5e',
                         linewidth = 2,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#242a5e'
                         )

                         ),

            yaxis = dict(title = '<b>Attack and Death</b>',
                         color = '#242a5e',
                         showline = True,
                         showgrid = True,
                         showticklabels = True,
                         linecolor = '#242a5e',
                         linewidth = 2,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#242a5e'
                         )

                         ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.3},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = '#242a5e'),

        )

    }


# Create pie chart (total casualties)
@app.callback(Output('pie1', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])
def display_content(w_countries, w_countries1, select_years):
    terr9 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[
        ['nkill', 'nwound']].sum().reset_index()
    death = terr9[(terr9['region_txt'] == w_countries) & (terr9['country_txt'] == w_countries1) & (terr9['iyear'] >= select_years[0]) & (terr9['iyear'] <= select_years[1])]['nkill'].sum()
    wound = terr9[(terr9['region_txt'] == w_countries) & (terr9['country_txt'] == w_countries1) & (terr9['iyear'] >= select_years[0]) & (terr9['iyear'] <= select_years[1])]['nwound'].sum()
    colors = ['#242a5e', '#219ebc', '#F5f8fa']

    return {
        'data': [go.Pie(labels = ['Total Death', 'Total Wounded'],
                        values = [death, wound],
                        marker = dict(colors = colors),
                        pull=[0.1, 0.1],
                        hoverinfo = 'label+value+percent',
                        textinfo = 'label+value',
                        textfont = dict(size = 13)
                        # hole=.7,
                        # rotation=45
                        # insidetextorientation='radial',

                        )],

        'layout': go.Layout(
            plot_bgcolor = '#afdefd',
            paper_bgcolor = '#afdefd',
            hovermode = 'closest',
            title = {
                'text': 'Total Casualties : ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#242a5e',
                'size': 20},
            legend = {
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = '#242a5e')
        ),

    }



# Create donut chart 2 (total casualties)
@app.callback(Output('pie2', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def display_content(w_countries, w_countries1, select_years):
    terr10 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nkillus', 'nwoundus']].sum().reset_index()
    death = terr10[(terr10['region_txt'] == w_countries) & (terr10['country_txt'] == w_countries1) & (terr10['iyear'] >= select_years[0]) & (terr10['iyear'] <= select_years[1])]['nkillus'].sum()
    wound = terr10[(terr10['region_txt'] == w_countries) & (terr10['country_txt'] == w_countries1) & (terr10['iyear'] >= select_years[0]) & (terr10['iyear'] <= select_years[1])]['nwoundus'].sum()
    colors = ['#242a5e', '#219ebc', '#F5f8fa']

    return {
        'data': [go.Pie(labels=['Total Death of US Citizen', 'Total Wounded of US Citizen'],
                        values=[death, wound],
                        marker=dict(colors=colors),
                        hole=0.7,  # Setting the size of the hole to make it a donut chart
                        pull=[0.1, 0.1],
                        hoverinfo='label+value+percent',
                        textinfo='label+value',
                        textfont=dict(size=13)
                        )],

        'layout': go.Layout(
            plot_bgcolor='#afdefd',
            paper_bgcolor='#afdefd',
            hovermode='closest',
            title={
                'text': 'Total Casualties of US Citizen : ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': '#242a5e',
                'size': 20},
            legend={
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font=dict(
                family="sans-serif",
                size=12,
                color='#242a5e')
        ),

    }


@app.callback(Output('bar2', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])
def update_graph(w_countries, w_countries1, select_years):
    # Data for line chart
    terr11 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nkillus', 'nwoundus']].sum().reset_index()
    terr12 = terr11[(terr11['region_txt'] == w_countries) & (terr11['country_txt'] == w_countries1) & (terr11['iyear'] >= select_years[0]) & (terr11['iyear'] <= select_years[1])]

    return {
        'data': [
            go.Scatter(
                x=terr12['iyear'],
                y=terr12['nkillus'],
                mode='lines+markers',
                line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#F5f8fa'),
                name='Killed',
                marker=dict(color='#F5f8fa'),
                text=terr12['nkillus'],
                hoverinfo='text',
                hovertext='<b>Region</b>: ' + terr12['region_txt'].astype(str) + '<br>' +
                          '<b>Country</b>: ' + terr12['country_txt'].astype(str) + '<br>' +
                          '<b>Year</b>: ' + terr12['iyear'].astype(str) + '<br>' +
                          '<b>Killed</b>: ' + [f'{x:,.0f}' for x in terr12['nkillus']] + '<br>'
            ),

            go.Scatter(
                x=terr12['iyear'],
                y=terr12['nwoundus'],
                mode='lines+markers',
                line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#219ebc'),
                name='Wounded',
                marker=dict(color='#219ebc'),
                text=terr12['nwoundus'],
                hoverinfo='text',
                hovertext='<b>Region</b>: ' + terr12['region_txt'].astype(str) + '<br>' +
                          '<b>Country</b>: ' + terr12['country_txt'].astype(str) + '<br>' +
                          '<b>Year</b>: ' + terr12['iyear'].astype(str) + '<br>' +
                          '<b>Wounded</b>: ' + [f'{x:,.0f}' for x in terr12['nwoundus']] + '<br>'
            )
        ],
        'layout': go.Layout(
            plot_bgcolor='#afdefd',
            paper_bgcolor='#afdefd',
            title={
                'text': 'Death and Wounded of US Citizen in ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            titlefont={
                'color': '#242a5e',
                'size': 20
            },
            hovermode='x',
            xaxis=dict(
                title='<b>Year</b>',
                tick0=0,
                dtick=1,
                color='#242a5e',
                showline=True,
                showgrid=True,
                showticklabels=True,
                linecolor='#242a5e',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='#242a5e'
                )
            ),
            yaxis=dict(
                title='<b>Wounded and Death of US Citizen</b>',
                color='#242a5e',
                showline=True,
                showgrid=True,
                showticklabels=True,
                linecolor='#242a5e',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='#242a5e'
                )
            ),
            legend={
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center',
                'x': 0.5,
                'y': -0.3
            },
            font=dict(
                family="sans-serif",
                size=12,
                color='#242a5e'
            )
        )
    }

@app.callback(Output('bar3', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def update_graph(w_countries, w_countries1, select_years):
        # Data for bar
        terr13 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nperps', 'nperpcap']].sum().reset_index()
        terr14 = terr13[(terr13['region_txt'] == w_countries) & (terr13['country_txt'] == w_countries1) & (terr13['iyear'] >= select_years[0]) & (terr13['iyear'] <= select_years[1])]

        return {
            'data': [
                    go.Bar(
                        y = terr14['iyear'],
                        x = terr14['nperps'],
                        text = terr14['nperps'],
                        texttemplate = '%{text:.2s}',
                        textposition = 'auto',
                        name = 'Perpetrators Count',
                        orientation='h',
                        marker = dict(color = '#F5f8fa'),
                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr14['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr14['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr14['iyear'].astype(str) + '<br>' +
                        '<b>Perpetrators Count:</b>: ' + [f'{x:,.0f}' for x in terr14['nperps']] + '<br>'
                    ),

                    go.Bar(
                        y = terr14['iyear'],
                        x = terr14['nperpcap'],
                        text = terr14['nperpcap'],
                        texttemplate = '%{text:.2s}',
                        textposition = 'auto',
                        textfont = dict(
                            color = 'white'
                        ),
                        name = 'Perpetrators Captured Count',
                        orientation='h',
                        marker = dict(color = '#219ebc'),
                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr14['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr14['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr14['iyear'].astype(str) + '<br>' +
                        '<b>Perpetrators Captured Count</b>: ' + [f'{x:,.0f}' for x in terr14['nperpcap']] + '<br>'
                    )],

            'layout': go.Layout(
                barmode = 'stack',
                plot_bgcolor = '#afdefd',
                paper_bgcolor = '#afdefd',
                title = {
                    'text': 'Captured Perpetrators & Perpetrators Count: ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                        [str(y) for y in select_years]) + '</br>',
                    'y': 0.93,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': '#242a5e',
                    'size': 20},
                hovermode = 'y',

                xaxis = dict(title = '<b>Perpetrators & Captured Perpetrators Captured</b>',
                            color = '#242a5e',
                            showline = True,
                            showgrid = True,
                            showticklabels = True,
                            linecolor = '#242a5e',
                            linewidth = 2,
                            ticks = 'outside',
                            tickfont = dict(
                                family = 'Arial',
                                size = 12,
                                color = '#242a5e'
                            )

                            ),

                yaxis = dict(title = '<b>Year</b>',
                            tick0 = 0,
                            dtick = 1,
                            color = '#242a5e',
                            showline = True,
                            showgrid = True,
                            showticklabels = True,
                            linecolor = '#242a5e',
                            linewidth = 2,
                            ticks = 'outside',
                            tickfont = dict(
                                family = 'Arial',
                                size = 12,
                                color = '#242a5e'
                            )

                            ),

                legend = {
                    'orientation': 'h',
                    'bgcolor': '#afdefd',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.3},
                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = '#242a5e'),

            )

        }


# Create pie chart 3
@app.callback(Output('pie3', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])
def display_content(w_countries, w_countries1, select_years):
    terr15 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[
        ['nperps', 'nperpcap']].sum().reset_index()
    perpcount = terr15[(terr15['region_txt'] == w_countries) & (terr15['country_txt'] == w_countries1) & (terr15['iyear'] >= select_years[0]) & (terr15['iyear'] <= select_years[1])]['nperps'].sum()
    perpcap = terr15[(terr15['region_txt'] == w_countries) & (terr15['country_txt'] == w_countries1) & (terr15['iyear'] >= select_years[0]) & (terr15['iyear'] <= select_years[1])]['nperpcap'].sum()
    colors = ['#242a5e', '#219ebc', '#F5f8fa']

    return {
        'data': [go.Pie(labels = ['Perpetrators Count', 'Perpetrators Captured'],
                        values = [perpcount, perpcap],
                        marker = dict(colors = colors),
                        pull=[0.1, 0.1, 0.1],
                        hoverinfo = 'label+value+percent',
                        textinfo = 'label+value',
                        textfont = dict(size = 13)
                        # hole=.7,
                        # rotation=45
                        # insidetextorientation='radial',

                        )],

        'layout': go.Layout(
            plot_bgcolor = '#afdefd',
            paper_bgcolor = '#afdefd',
            hovermode = 'closest',
            title = {
                'text': 'Perpetrators in ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#242a5e',
                'size': 20},
            legend = {
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = '#242a5e')
        ),

    }



# Create donut chart 4 (per death and wounded)
@app.callback(Output('pie4', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def display_content(w_countries, w_countries1, select_years):
    terr16 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nkillter', 'nwoundte']].sum().reset_index()
    perkill = terr16[(terr16['region_txt'] == w_countries) & (terr16['country_txt'] == w_countries1) & (terr16['iyear'] >= select_years[0]) & (terr16['iyear'] <= select_years[1])]['nkillter'].sum()
    perwound = terr16[(terr16['region_txt'] == w_countries) & (terr16['country_txt'] == w_countries1) & (terr16['iyear'] >= select_years[0]) & (terr16['iyear'] <= select_years[1])]['nwoundte'].sum()
    colors = ['#242a5e', '#219ebc', '#F5f8fa']

    return {
        'data': [go.Pie(labels=['Perpetrator Death Count', 'Wounded Perpetrator Count'],
                        values=[perkill, perwound],
                        marker=dict(colors=colors),
                        hole=0.5,  # Setting the size of the hole to make it a donut chart
                        pull=[0.1, 0.1],
                        hoverinfo='label+value+percent',
                        textinfo='label+value',
                        textfont=dict(size=13)
                        )],

        'layout': go.Layout(
            plot_bgcolor='#afdefd',
            paper_bgcolor='#afdefd',
            hovermode='closest',
            title={
                'text': 'Perpereator Death and Wounded in ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': '#242a5e',
                'size': 20},
            legend={
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font=dict(
                family="sans-serif",
                size=12,
                color='#242a5e')
        ),

    }


@app.callback(Output('bar4', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def update_graph(w_countries, w_countries1, select_years):
        # Data for line chart
        terr17 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nkillter', 'nwoundte']].sum().reset_index()
        terr18 = terr17[(terr17['region_txt'] == w_countries) & (terr17['country_txt'] == w_countries1) & (terr17['iyear'] >= select_years[0]) & (terr17['iyear'] <= select_years[1])]

        return {
            'data': [
                    go.Scatter(
                        x = terr18['iyear'],
                        y = terr18['nkillter'],
                        mode = 'lines+markers',
                        name = 'Perpetrators Death Count',
                        marker = dict(color = '#F5f8fa'),
                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr18['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr18['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr18['iyear'].astype(str) + '<br>' +
                        '<b>Perpetrators Death Count:</b>: ' + [f'{x:,.0f}' for x in terr18['nkillter']] + '<br>'
                    ),

                    go.Scatter(
                        x = terr18['iyear'],
                        y = terr18['nwoundte'],
                        mode = 'lines+markers',
                        name = 'Wounded Perpetrators Count',
                        marker = dict(color = '#219ebc'),
                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr18['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr18['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr18['iyear'].astype(str) + '<br>' +
                        '<b>Wounded Perpetrators Count</b>: ' + [f'{x:,.0f}' for x in terr18['nwoundte']] + '<br>'
                    )],

            'layout': go.Layout(
                plot_bgcolor = '#afdefd',
                paper_bgcolor = '#afdefd',
                title = {
                    'text': 'Wound and Dead Perpetrator Count: ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                        [str(y) for y in select_years]) + '</br>',
                    'y': 0.93,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont = {
                    'color': '#242a5e',
                    'size': 20},
                hovermode = 'x',

                xaxis = dict(title = '<b>Year</b>',
                            color = '#242a5e',
                            showline = True,
                            showgrid = True,
                            showticklabels = True,
                            linecolor = '#242a5e',
                            linewidth = 2,
                            ticks = 'outside',
                            tickfont = dict(
                                family = 'Arial',
                                size = 12,
                                color = '#242a5e'
                            )

                            ),

                yaxis = dict(title = '<b>Count</b>',
                            color = '#242a5e',
                            showline = True,
                            showgrid = True,
                            showticklabels = True,
                            linecolor = '#242a5e',
                            linewidth = 2,
                            ticks = 'outside',
                            tickfont = dict(
                                family = 'Arial',
                                size = 12,
                                color = '#242a5e'
                            )

                            ),

                legend = {
                    'orientation': 'h',
                    'bgcolor': '#afdefd',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.3},
                font = dict(
                    family = "sans-serif",
                    size = 12,
                    color = '#242a5e'),

            )

        }



# Create second combination of bar and line  chart
@app.callback(Output('bar5', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])

def update_graph(w_countries, w_countries1, select_years):
    # Data for line and bar
    terr19 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])['nreleased'].sum().reset_index()
    terr20 = terr19[(terr19['region_txt'] == w_countries) & (terr19['country_txt'] == w_countries1) & (terr19['iyear'] >= select_years[0]) & (terr19['iyear'] <= select_years[1])]
    terr21 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[['nhostkid', 'nhostkidus']].sum().reset_index()
    terr22 = terr21[(terr21['region_txt'] == w_countries) & (terr21['country_txt'] == w_countries1) & (terr21['iyear'] >= select_years[0]) & (terr21['iyear'] <= select_years[1])]

    return {
        'data': [go.Scatter(x = terr20['iyear'],
                            y = terr20['nreleased'],
                            mode = 'lines+markers',
                            name = 'Released Hostage Count',
                            line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#242a5e'),
                            marker = dict(size = 10, symbol = 'square', color = 'white',
                                          line = dict(color = '#242a5e', width = 2)
                                          ),
                            hoverinfo = 'text',
                            hovertext =
                            '<b>Region</b>: ' + terr20['region_txt'].astype(str) + '<br>' +
                            '<b>Country</b>: ' + terr20['country_txt'].astype(str) + '<br>' +
                            '<b>Year</b>: ' + terr20['iyear'].astype(str) + '<br>' +
                            '<b>Hostage Released</b>: ' + [f'{x:,.0f}' for x in terr20['nreleased']] + '<br>'

                            ),
                 go.Bar(
                     x = terr22['iyear'],
                     y = terr22['nhostkid'],
                     text = terr22['nhostkid'],
                     texttemplate = '%{text:.2s}',
                     textposition = 'auto',
                     name = 'Hostage Count',

                     marker = dict(color = '#F5f8fa'),

                     hoverinfo = 'text',
                     hovertext =
                     '<b>Region</b>: ' + terr22['region_txt'].astype(str) + '<br>' +
                     '<b>Country</b>: ' + terr22['country_txt'].astype(str) + '<br>' +
                     '<b>Year</b>: ' + terr22['iyear'].astype(str) + '<br>' +
                     '<b>Hostage Count</b>: ' + [f'{x:,.0f}' for x in terr22['nhostkid']] + '<br>'
                 ),

                 go.Bar(x = terr22['iyear'],
                        y = terr22['nhostkidus'],
                        text = terr22['nhostkidus'],
                        texttemplate = '%{text:.2s}',
                        textposition = 'auto',
                        textfont = dict(
                            color = 'white'
                        ),
                        name = 'Hostage (US Citizen) Count',

                        marker = dict(color = '#219ebc'),

                        hoverinfo = 'text',
                        hovertext =
                        '<b>Region</b>: ' + terr22['region_txt'].astype(str) + '<br>' +
                        '<b>Country</b>: ' + terr22['country_txt'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + terr22['iyear'].astype(str) + '<br>' +
                        '<b>Hostage (US Citizen) Count</b>: ' + [f'{x:,.0f}' for x in terr22['nhostkidus']] + '<br>'
                        )],

        'layout': go.Layout(
            barmode = 'stack',
            plot_bgcolor = '#afdefd',
            paper_bgcolor = '#afdefd',
            title = {
                'text': 'Hostage (US/Regular) and Released Hostage Count ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#242a5e',
                'size': 20},

            hovermode = 'x',

            xaxis = dict(title = '<b>Year</b>',
                         tick0 = 0,
                         dtick = 1,
                         color = '#242a5e',
                         showline = True,
                         showgrid = True,
                         showticklabels = True,
                         linecolor = '#242a5e',
                         linewidth = 2,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#242a5e'
                         )

                         ),

            yaxis = dict(title = '<b>Hostage Released and Count </b>',
                         color = '#242a5e',
                         showline = True,
                         showgrid = True,
                         showticklabels = True,
                         linecolor = '#242a5e',
                         linewidth = 2,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#242a5e'
                         )

                         ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.3},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = '#242a5e'),

        )

    }


# Create pie chart (total casualties)
@app.callback(Output('pie5', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_countries1', 'value')],
              [Input('select_years', 'value')])
def display_content(w_countries, w_countries1, select_years):
    terr23 = terr2.groupby(['region_txt', 'country_txt', 'iyear'])[
        ['nreleased', 'nhostkid', 'nhostkidus']].sum().reset_index()
    hosrel = terr23[(terr23['region_txt'] == w_countries) & (terr23['country_txt'] == w_countries1) & (terr23['iyear'] >= select_years[0]) & (terr23['iyear'] <= select_years[1])]['nreleased'].sum()
    hostkid = terr23[(terr23['region_txt'] == w_countries) & (terr23['country_txt'] == w_countries1) & (terr23['iyear'] >= select_years[0]) & (terr23['iyear'] <= select_years[1])]['nhostkid'].sum()
    hostkidus = terr23[(terr23['region_txt'] == w_countries) & (terr23['country_txt'] == w_countries1) & (terr23['iyear'] >= select_years[0]) & (terr23['iyear'] <= select_years[1])]['nhostkidus'].sum()
    colors = ['#242a5e', '#219ebc', '#F5f8fa']

    return {
        'data': [go.Pie(labels = ['Hostage Released', 'Hostage Count', 'Hostage (US) Count'],
                        values = [hosrel, hostkid, hostkidus],
                        marker = dict(colors = colors),
                        pull=[0.1, 0.1, 0.1],
                        hoverinfo = 'label+value+percent',
                        textinfo = 'label+value',
                        textfont = dict(size = 13)
                        # hole=.7,
                        # rotation=45
                        # insidetextorientation='radial',

                        )],

        'layout': go.Layout(
            plot_bgcolor = '#afdefd',
            paper_bgcolor = '#afdefd',
            hovermode = 'closest',
            title = {
                'text': 'Hostage Situation in ' + (w_countries1) + '  ' + '<br>' + ' - '.join(
                    [str(y) for y in select_years]) + '</br>',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#242a5e',
                'size': 20},
            legend = {
                'orientation': 'h',
                'bgcolor': '#afdefd',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = '#242a5e')
        ),

    }







if __name__ == '__main__':
    app.run_server(debug = True)
