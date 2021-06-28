import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
print(__version__)
import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()

pio.renderers.default = 'png'

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Categoria': ['A', 'B', 'C'], 'Valores': [32, 43, 50]})

df[['A', 'B']].iplot(kind='spread')

fig.show()
