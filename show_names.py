# data from https://www.ssa.gov/oact/babynames/limits.html
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# add your names to plot here in tic marks or quotes, seperated by commas: 'Joe', 'Joseph'
name_to_plot = ['Sarah', 'Sara']
# M, F, or B for both
sex = "F"

#Change to true/false to show or not show the sum of the names in your list, helpful for spelling variants
show_sum = True

# Set top n to 0 to not display most popular names
show_top_n = 10

# limit the most popular names to a recent timeframe (the most popular names in the 60s were very common)
show_top_n_since = 1880

# Show name neighbors (names that are similar in popularity to the plotted names)
name_neighbors = 0 # will show above and below

name_data = pd.read_csv("name_data.csv")


# Filtere for sex if desired
if sex != "B":
    name_data  = name_data[name_data.sex == sex]

# Filter for the names to plot
filtered_name_data = name_data[name_data.name.isin(name_to_plot)]

# Sum data if desired
if show_sum:
    pivoted = filtered_name_data.pivot_table(index='year', values='count', aggfunc="sum", fill_value=0)
    pivoted.columns.name = None
    pivoted.reset_index(inplace=True)
    pivoted["name"] = "Sum"
    pivoted["rank"] = "n/a"
    pivoted["sex"] = "n/a"
    filtered_name_data = pd.concat([filtered_name_data, pivoted], axis=0)


# if we are looking for name neighbors
if name_neighbors > 0:
    similar = []
    for row in filtered_name_data.itertuples():
        subset = name_data[(name_data['year'] == row.year) & (name_data['rank'] >= row.rank-name_neighbors) & (name_data['rank'] <= row.rank+name_neighbors)]
        similar.append(subset)

    similar = pd.concat(similar, axis=0)
    similar = similar[-similar.name.isin(name_to_plot)]
else:
    similar = pd.DataFrame({"name":[], "year":[], "count":[], "sex":[], "rank":[]})

# plot
fig1 = px.scatter(filtered_name_data, x='year', y='count', color="name", title=",".join(name_to_plot), hover_data=['rank'],symbol='sex')
fig2 = px.scatter(name_data[(name_data["rank"]<=show_top_n) & (name_data["year"] >= show_top_n_since)], x='year', y='count', color="rank", hover_data=["name"])
fig3 = px.scatter(similar, x='year', y='count', hover_data=["name", "rank"], color_discrete_sequence=['grey'], opacity=0.2)
fig = go.Figure(fig3.data + fig1.data + fig2.data)
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
fig.show()