import sys
sys.path.insert(0,"Library/Frameworks/Python.Framework/Versions/3.8.6/lib/site-packages")
import pymysql as ps
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


# makes the layout
fig = make_subplots(
    rows=3, cols=2,
    column_widths=[7.0, 7.0],row_heights=[7.0, 7.0, 6.0],
    subplot_titles=("Number of Airbnbs per Neighbourhood",
    "Airbnb Room Types", "Last Airbnb Review",
    "Price per Airbnb Room Type",
    "Most Expensive Airbnb per Neighbourhood"))
conn=ps.connect(host='database-1.cspat74yfn24.us-east-1.rds.amazonaws.com',
                user='admin', passwd='Lalastacks',
                port=3306, db='NYCAirBnBs', autocommit=True);


#number of airbnbs per nieghbourhood
#query
perneighbourhood = pd.read_sql('SELECT NeighbourhoodGroup, Count(*) FROM NeighbourhoodLocation GROUP BY NeighbourhoodGroup ', conn)
#fig
fig.add_trace(
    go.Bar(
        x=perneighbourhood['NeighbourhoodGroup'],
        y=perneighbourhood['Count(*)'],
        name=('Number of AirBnb per Neighbourhood')
        ),
        row=1,col=1
        )

#airbnb roomtypes
#query
roomType = pd.read_sql('SELECT RoomType, Count(*) FROM AirBnB GROUP BY roomType', conn)
#fig
fig.add_trace(
    go.Bar(
        x=roomType['RoomType'],
        y=roomType['Count(*)'],
        name=('Amount of Listings per Room Type')
        ),
        row=1, col=2
        )


#last airbnb per review
#query
review = pd.read_sql('Select year(_LastReview), Count(*) FROM Reviews WHERE year(_LastReview) != 0000 GROUP BY year(_LastReview)', conn)
#fig
N = 9
x = review['year(_LastReview)']
y = review['Count(*)']
colors = np.random.rand(N)

fig.add_trace(
    go.Scatter(
        x=review['year(_LastReview)'],
        y=review['Count(*)'],
        mode='markers',
        name='Year of Last Review and How Many Reviews'
        ),
        row=2, col=1
        )

#prices per airbnb roomtype
#query
prices = pd.read_sql('SELECT RoomType, Price FROM AirBnB ORDER BY RoomType', conn)
#fig
N = 9
x = prices['RoomType']
y = prices['Price']
colors = np.random.rand(N)

fig.add_trace(
    go.Scatter(
        x=prices['RoomType'],
        y=prices['Price'],
        mode='markers',
        name=('Price per Airbnb Room Type')
        ),
        row=2, col=2
        )


#most expensive airbnb per location
#query
expensive = pd.read_sql('SELECT NeighbourhoodGroup, MAX(price) FROM AirBnB, NeighbourhoodLocation WHERE NBID = NeighbourhoodID GROUP BY NeighbourhoodGroup', conn)
#fig
fig.add_trace(
    go.Line(
        y=expensive['MAX(price)'],
        x=expensive['NeighbourhoodGroup'],
        name=('Most Expensive Airbnb per Location')
        ),
        row=3, col=1
        )


fig.update_layout(title_font_family="Balto",title_font_size=30,title_font_color='darkred',
height=1000, width=1500, title_text="NYC AirBnB Dashboard")
fig.show()
