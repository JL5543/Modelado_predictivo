
#Clase 1 Modelado predicitivo, aun no vemos codigo, solo fue introduccion y distancias para datos binarios
import pandas as pd


#%% SCALING OF VARIABLES BY NORMALIZATION
data['Refractive_index_scale'] = (data.Refractive_index-
data.Refractive_index.mean())/data.Refractive_index.std()
data['Na_scale'] = (data.Na-data.Na.mean())/data.Na.std()
### Scaling through scikit-learn
#from sklearn import preprocessing
#data['Refractive_index_scale'] = preprocessing.scale(data.Refractive_index)