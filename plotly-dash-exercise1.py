import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('data/ecom_sales.csv')
#print(ecom_sales.head())
from PIL import Image; logo_link = Image.open('img/e_com_logo.png')
#logo_link = '../img/e_com_logo.png'
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)').sort_values(by='Total Sales ($)', ascending=False)
#print(ecom_bar)
top_country = ecom_bar.loc[0]['Country']   
#print(top_country)         
bar_fig_country = px.bar(ecom_bar, x='Total Sales ($)', y='Country', color='Country', color_discrete_map={'United Kingdom':'lightblue', 'Germany':'orange', 'France':'darkblue', 'Australia':'green', 'Hong Kong':'red'})         
    
app = dash.Dash(__name__)

app.layout = html.Div([
  # Add the company logo
  html.Img(src=logo_link),
  html.H1('Sales by Country',style={'color':'blue'}
  ),
  html.Div(dcc.Graph(figure=bar_fig_country), 
           style={'width':'750px', 'margin':'auto'}),
  # Add an overall text-containing component
  html.Span(children=[
    # Add the top country text
    'This year, the most sales came from: ', 
    html.B(top_country),
    # Italicize copyright notice
    html.I(' Copyright E-Com INC',style={'backgroundColor':'lightgray'})
    
    ],style={'border':'2px solid black','margin':'2px 0px','display':'inline-block','padding':'5px'})
    ], 
  style={'textAlign':'center', 'fontSize':22})

if __name__ == '__main__':
    app.run_server(debug=True) 