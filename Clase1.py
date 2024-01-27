
#Clase 1 Modelado predicitivo, aun no vemos codigo, solo fue introduccion y distancias para datos binarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATA QUALITY REPORT

def dqr(data):
    
    # List of database variables
    cols = pd.DataFrame(list(data.columns.values),
    columns=['Names'],
    index=list(data.columns.values))
    # List of data types
    dtyp = pd.DataFrame(data.dtypes,columns=['Type'])
    # List of missing data
    misval = pd.DataFrame(data.isnull().sum(),
    columns=['Missing_values'])
    # List of present data
    presval = pd.DataFrame(data.count(),
    columns=['Present_values'])
    # List of unique values
    unival = pd.DataFrame(columns=['Unique_values'])
    # List of min values
    minval = pd.DataFrame(columns=['Min_value'])
    # List of max values
    maxval = pd.DataFrame(columns=['Max_value'])
    for col in list(data.columns.values):
    unival.loc[col] = [data[col].nunique()]
    try:
    minval.loc[col] = [data[col].min()]
    maxval.loc[col] = [data[col].max()]
    except:
    pass
    # Join the tables and return the result
    return
    cols.join(dtyp).join(misval).join(presval).join(unival).join(minval).join(maxval)


#%% SCALING OF VARIABLES BY NORMALIZATION
data['Refractive_index_scale'] = (data.Refractive_index-
data.Refractive_index.mean())/data.Refractive_index.std()
data['Na_scale'] = (data.Na-data.Na.mean())/data.Na.std()
### Scaling through scikit-learn
#from sklearn import preprocessing
#data['Refractive_index_scale'] = preprocessing.scale(data.Refractive_index)
