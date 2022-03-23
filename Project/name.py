import pandas as pd
import plotly.express as px

wireframe = pd.read_csv("Project/data.csv")
mean = wireframe.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean,x="student_id", y="level", size = "attempt", color = "attempt")
fig.show()
