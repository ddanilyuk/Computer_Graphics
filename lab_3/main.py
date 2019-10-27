import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def f(x, y):
    return np.sin(x) * np.cos(y)


x = np.linspace(-6, 6, 60)
y = np.linspace(-6, 6, 60)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)
fig = make_subplots(rows=1, cols=1,
                    specs=[[{'is_3d': True}]],
                    subplot_titles=['Lab3'],
                    )
fig.layout.autosize = True

fig.add_trace(go.Surface(x=X, y=Y, z=Z, opacity=0.7, surfacecolor=Z))
fig.update_layout(title_text="Lab3")
fig.show()
