#importing required libraries
import pandas as pd
import plotly.express as px 

#Reading data from the csv file
data = pd.read_csv('pokemon_data.csv')

# To plot bubble graph with Attack on x - axis and HP on y - axis
px.scatter(data ,x = 'HP', y = 'Attack', color = 'Name')
