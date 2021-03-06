import d3py
import geoms
import numpy as np
import pandas

T = 100
df = pandas.DataFrame({
    "time" : range(T),
    "pressure": np.random.rand(T),
    "temp" : np.random.rand(T)
})

fig = d3py.Figure(df, name="basic_example", width=800, height=400) 
point = geoms.Point(x="pressure", y="temp", fill="red")
fig += point
fig.show()
