import plotly.express as px

df = px.data.gapminder()

fig = px.bar(df, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])

# GUESS ### Slider prebuilt on {'animation_frame':'year', 'animation_group':'country'}
fig.show()


#https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Scatter3d.html

# import plotly.express as px
# df = px.data.iris()
# fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
#                     color='petal_length', symbol='species')
# fig.show()