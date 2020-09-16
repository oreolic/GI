#%%
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

#%%
def Hierarchy_Clustering(DF):
    ## Column = Gene, Index = Sample
    z = linkage(DF,method='centroid')
    result = dendrogram(z)

    return result


# %%
## AgglomerativeClustering

def Agglomerative_Clustering(df, n_cluster):
    model = AgglomerativeClustering(n_clusters=n_cluster)
    model.fit(df)
    y_predict = model.fit_predict(df)
    df['cluster'] = y_predict
    return df

# %%
def KaplanMeier(df,eventName,TimeName, labelName):
	kmf = KaplanMeierFitter()
	kmf.fit(df[TimeName],df[eventName], label=labelName)
	kmf.plot() ##세부 설정 필요
	return kmf

