import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credito = pd.read_csv('/content/credit_data.csv')

base_credito

# client cliente
# income salario
# age idade
# loan divida
# deafult não pagou

base_credito.head()

base_credito.tail()

base_credito.describe()

base_credito[base_credito['income'] >= 69995.685578]

base_credito[base_credito['loan'] <= 1.377630]

