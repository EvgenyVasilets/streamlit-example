from collections import namedtuple
import altair as alt
import math
import pandas as pd

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from vega_datasets import data

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

#
# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
#
#     Point = namedtuple('Point', 'x y')
#     data = []
#
#     points_per_turn = total_points / num_turns
#
#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))
#
#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))


data = pd.read_csv('data.csv')
data = data[['Ticket ID', 'Origin Channel', 'Closing Channel', 'Mega Region',
       'Brand Name', 'Tier Level', 'Created AT UTC', 'First Reply UTC',
       'Resolved AT UTC', 'Agent ID', 'Customer ID', 'CSAT', 'Issue Type']]

data.columns = [
    'ticket_id',
    'origin_ch',
    'closing_ch',
    'region',
    'brand',
    'tier',
    'created',
    'first_reply',
    'resolved',
    'agent_id',
    'customer_id',
    'csat',
    'issue_type'
]

data.ticket_id = data.ticket_id.astype(str)
data.customer_id = data.customer_id.astype(str)
data.agent_id = data.agent_id.astype('Int64').astype(str)

data.created = data.created.astype('datetime64[ns]')
data.resolved = data.resolved.astype('datetime64[ns]')
data.first_reply = data.first_reply.astype('datetime64[ns]')

issue_columns = ['issue_1', 'issue_2', 'issue_3', 'issue_4']
data[issue_columns] = data['issue_type'].str.split(' :: ', expand=True)
for c in issue_columns:
    data[c] = data[c].str.strip()

number = st.slider("Pick a number", 0, 100)
